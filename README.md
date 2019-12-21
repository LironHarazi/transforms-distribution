# transforms-distribution

1.Download\clone Dockerfile,distributionServer.py to your local machine 

2.run bash command: sudo docker build -t transformserver:latest .

3.After creating the image,run bash command: sudo docker run -p 5000:5000/tcp transformserver

4.create GET/POST request:

GET:
  http://localhost:5000/dist?sentence=How are you

POST:

  url - http://localhost:5000/dist

  body:

  {
  "sentence":"How are you"
  }
