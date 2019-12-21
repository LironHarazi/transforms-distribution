from flask import Flask
from flask import request
from flask import jsonify
import torch.nn.functional as F
import sys
import optparse
import torch
from transformers import BertTokenizer, BertModel, BertForMaskedLM

GPU = False

def GetDist(sentence):
	# Load pre-trained model tokenizer (vocabulary)
	tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

	# Tokenize input
	text = "The phrases sound similar, but in certain"
	tokenized_text = tokenizer.tokenize(text)
	# Mask predicted token
	tokenized_text.append('[MASK]')
	masked_index = len(tokenized_text) - 1
	# Convert token to vocabulary indices
	indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)

	# Define as one sentence
	segments_ids = [0] * len(tokenized_text)

	# Convert inputs to PyTorch tensors
	tokens_tensor = torch.tensor([indexed_tokens])
	segments_tensors = torch.tensor([segments_ids])

	# Load pre-trained model (weights)
	model = BertForMaskedLM.from_pretrained('bert-base-uncased')
	model.eval()

	# If you have a GPU, put everything on cuda
	if GPU == True:
	    tokens_tensor = tokens_tensor.to('cuda')
	    segments_tensors = segments_tensors.to('cuda')
	    model.to('cuda')

	# Predict all tokens
	with torch.no_grad():
	    outputs = model(tokens_tensor, token_type_ids=segments_tensors)
	    predictions = outputs[0]

	dist = F.softmax(predictions[0, masked_index],0)
	dist = list(dist.numpy())
	dist = ['{:.3f}'.format(x) for x in dist]
	return dist



app = Flask(__name__)



@app.route('/dist', methods=['GET'])
def returnAll():
    sentence =  request.args.get('sentence')
    print(sentence)
    dist = GetDist(sentence)
    return jsonify({'distribution' : dist})

@app.route('/dist', methods=['POST'])
def addOne():
    val = request.get_json(force = True)
    sentence = val['sentence']
    print(sentence)
    dist = GetDist(sentence)
    return jsonify({'distribution' : dist})





if __name__ == '__main__':
    parser = optparse.OptionParser(usage="python distributionServer.py -p ")
    parser.add_option('-p', '--port', action='store', dest='port', help='The port to listen on.')
    (args, _) = parser.parse_args()
    if args.port == None:
        print ("Missing required argument: -p/--port")
        sys.exit(1)
    app.run(host='0.0.0.0', port=int(args.port), debug=False)







