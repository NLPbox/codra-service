# build

docker build -t codra-service .

# run

docker run -p 8000:8000 -ti codra-service

# Usage Examples

## CURL

```
$ cat test.txt 
Altough they didn't like him, they accepted the offer.

$ curl -X POST -F "input=@test.txt" http://localhost:8000/parse -F output_format=original
( Root (span 1 3)
  ( Nucleus (span 1 2) (rel2par Same-Unit)
    ( Satellite (leaf 1) (rel2par Attribution) (text _!Altough_!) )
    ( Nucleus (leaf 2) (rel2par span) (text _!they did n't like him ,_!) )
   )
  ( Nucleus (leaf 3) (rel2par Same-Unit) (text _!they accepted the offer ._!) )
)
```

## Javascript

```
>>> var xhr = new XMLHttpRequest();

>>> xhr.open("POST", "http://localhost:8000/parse")

>>> var data = new FormData();
>>> data.append('input', 'Altough they didn\'t like him, they accepted the offer.');
>>> data.append('output_format', 'original');

>>> xhr.send(data);
>>> console.log(xhr.response);
( Root (span 1 3)
  ( Nucleus (span 1 2) (rel2par Same-Unit)
    ( Satellite (leaf 1) (rel2par Attribution) (text _!Altough_!) )
    ( Nucleus (leaf 2) (rel2par span) (text _!they did n't like him ,_!) )
   )
  ( Nucleus (leaf 3) (rel2par Same-Unit) (text _!they accepted the offer ._!) )
)
```
