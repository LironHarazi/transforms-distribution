# transforms-distribution

1.Download\clone Dockerfile,distributionServer.py,transPythonRequirements.txt to your ךocal machine 

2.run bash command: sudo docker build -t transforms:latest .

3.After creating the image,run bash command: sudo docker run -p 5000:5000/tcp transforms

4.create GET/POST request:

GET:
  http://localhost:5000/dist?sentence=how are you

POST:

  url - http://localhost:5000/dist

  body:

  {
  "sentence":"how are you"
  }
