#!/usr/bin/env python3
import os
import sys

import hug
import sh

PARSER_PATH = '/opt/codra-rst-parser'
PARSER_EXECUTABLE = 'codra.sh'
INPUT_FILEPATH = '/tmp/input.txt'
OUTPUT_FILEPATH = INPUT_FILEPATH+'.dis'


@hug.response_middleware()
def process_data(request, response, resource):
    """This is a middleware function that gets called for every request a hug API processes.
    It will allow Javascript clients on other hosts / ports to access the API (CORS request).
    """
    response.set_header('Access-Control-Allow-Origin', '*')


@hug.post('/parse', output=hug.output_format.file)
def call_parser(body, output_format):
    parser = sh.Command(os.path.join(PARSER_PATH, PARSER_EXECUTABLE))

#    import pudb; pudb.set_trace()

    if 'input' in body:
        input_file_content = body['input']
        with open(INPUT_FILEPATH, 'wb') as input_file:
            input_file.write(input_file_content)
        
        parser_stdout = parser(input_file.name, _cwd=PARSER_PATH)
        
        if output_format == b'nltk-tree-png':
            dis2png = sh.Command('./convert.sh')
            dis2png(OUTPUT_FILEPATH)
            return OUTPUT_FILEPATH+'.png'
        
        else: # always fall back to the 'original' output format of the parser
            return OUTPUT_FILEPATH
    
    else:
        return {'body': body}
