#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Arne Neumann <nlpbox.programming@arne.cl>

import pytest
import requests


INPUT_TEXT = "Altough they didn't like him, they accepted the offer."
EXPECTED_OUTPUT = """( Root (span 1 3)
  ( Nucleus (span 1 2) (rel2par Same-Unit)
    ( Satellite (leaf 1) (rel2par Attribution) (text _!Altough_!) )
    ( Nucleus (leaf 2) (rel2par span) (text _!they did n't like him ,_!) )
   )
  ( Nucleus (leaf 3) (rel2par Same-Unit) (text _!they accepted the offer ._!) )
)"""


def test_api_plaintext():
    """The codra-service API produces the expected plaintext parse output."""
    res = requests.post(
        'http://localhost:8000/parse',
        files={'input': INPUT_TEXT},
        data={'output_format': 'output'})
    assert res.content.decode('utf-8') == EXPECTED_OUTPUT

