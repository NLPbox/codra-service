#!/usr/bin/env python3
import os
import sys
from tempfile import NamedTemporaryFile

import hug
import sh

PARSER_PATH = '/opt/codra-rst-parser'


@hug.post('/parse', output=hug.output_format.file)
def call_parser(body, output_format: hug.types.text):
    codra = sh.Command(os.path.join(PARSER_PATH, 'codra.sh'))

    if 'input' in body:
        input_file_content = body['input']
        with open('/tmp/input.txt', 'wb') as input_file:
            input_file.write(input_file_content)
        
        parser_stdout = codra(input_file.name, _cwd=PARSER_PATH)
        print(os.listdir('/tmp'))
        return '/tmp/input.txt.dis'
    
    else:
        return {'body': body}
