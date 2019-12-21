# transforms-distribution

1.run bash command: sudo docker build -t transforms:latest .

2.After creating the image,run bash commamd: sudo docker run -p 5000:5000/tcp transforms

3.create GET/POST request:

GET:
  http://localhost:5000/dist?sentence=how are you

POST:

  url - http://localhost:5000/dist

  body:

  {
  "sentence":"how are you"
  }
