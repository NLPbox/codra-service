#!/usr/bin/env python3
import os
import sys

from falcon import HTTP_500
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
def call_parser(body, response):
    parser = sh.Command(os.path.join(PARSER_PATH, PARSER_EXECUTABLE))

    if 'input' in body:
        input_file_content = body['input']
        with open(INPUT_FILEPATH, 'wb') as input_file:
            input_file.write(input_file_content)

        try:
            parser_stdout = parser(input_file.name, _cwd=PARSER_PATH)
        
            if body['output_format'] == b'nltk-tree-png':
                dis2png = sh.Command('./convert.sh')
                dis2png(OUTPUT_FILEPATH)
                return OUTPUT_FILEPATH+'.png'
        
            else: # always fall back to the 'original' output format of the parser
                return OUTPUT_FILEPATH
        except sh.ErrorReturnCode_1 as err:
            response.status = HTTP_500
            trace = str(err.stderr, 'utf-8')
            error_msg = "{0}\n\n{1}".format(err, trace).encode('utf-8')

            import tempfile
            temp = tempfile.NamedTemporaryFile(delete=False)
            temp.write(error_msg)
            temp.close()
            return temp.name

    else:
        return {'body': body}
