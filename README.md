# codra-service

[![Travis Build Status](https://travis-ci.org/NLPbox/codra-service.svg?branch=master)](https://travis-ci.org/NLPbox/codra-service)
[![Docker Build Status](https://img.shields.io/docker/build/nlpbox/codra-service.svg)](https://hub.docker.com/r/nlpbox/codra-service/)

This docker container allows you to build, install and run the
[CODRA RST discourse parser](http://alt.qcri.org/tools/discourse-parser/)
(Joty et al. 2015) in a docker container with an added REST API.

## build

docker build -t codra-service .

## run

docker run -p 8000:8000 -ti codra-service

## Usage Examples

### CURL

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

$ curl -X POST -F "input=@test.txt" http://localhost:8000/parse -F output_format=rs3
<?xml version='1.0' encoding='UTF-8'?>
<rst>
  <header>
    <relations>
      <rel name="Attribution" type="rst"/>
      <rel name="Same-Unit" type="multinuc"/>
    </relations>
  </header>
  <body>
    <segment id="5" parent="7" relname="Attribution">Altough</segment>
    <segment id="7" parent="3" relname="span">they did n't like him ,</segment>
    <segment id="9" parent="1" relname="Same-Unit">they accepted the offer .</segment>
    <group id="1" type="multinuc"/>
    <group id="3" type="span" parent="1" relname="Same-Unit"/>
  </body>
</rst>
```

### Javascript

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
