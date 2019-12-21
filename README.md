# transforms-distribution

1.run bash command: sudo docker build -t transforms:latest .
2.create GET/POST request:

GET:
localhost:5000/dist?sentence=how are you

POST:
url - http://localhost:5000/dist
body:
{
 "sentence":"how are you"
}
