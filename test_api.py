#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import pexpect
import pytest
import requests
import sh

INPUT_TEXT = "Altough they didn't like him, they accepted the offer."

EXPECTED_OUTPUT = """( Root (span 1 3)
  ( Nucleus (span 1 2) (rel2par Same-Unit)
    ( Satellite (leaf 1) (rel2par Attribution) (text _!Altough_!) )
    ( Nucleus (leaf 2) (rel2par span) (text _!they did n't like him ,_!) )
   )
  ( Nucleus (leaf 3) (rel2par Same-Unit) (text _!they accepted the offer ._!) )
)
"""

EXPECTED_RS3 = """<?xml version='1.0' encoding='UTF-8'?>
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
"""


@pytest.fixture(scope="session", autouse=True)
def start_api():
    print("starting API...")
    child = pexpect.spawn('hug -f codra_hug_api.py')
    yield child.expect('(?i)Serving on :8000') # provide the fixture value
    print("stopping API...")
    child.close()

def test_api_plaintext():
    """The codra-service API produces the expected plaintext parse output."""
    res = requests.post(
        'http://localhost:8000/parse',
        files={'input': INPUT_TEXT},
        data={'output_format': 'original'})
    assert res.content.decode('utf-8') == EXPECTED_OUTPUT

def test_api_rs3():
    """The codra-service API produces the expected parse output in .rs3 format."""
    res = requests.post(
        'http://localhost:8000/parse',
        files={'input': INPUT_TEXT},
        data={'output_format': 'rs3'})
    assert res.content.decode('utf-8') == EXPECTED_RS3
