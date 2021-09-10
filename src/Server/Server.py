import flask
import argparse
import json
import sys
from http import HTTPStatus
from flask import request, jsonify
from pathlib import Path

## make src dir avlb for cmd operation
src_dir_location = Path(__file__).parents[2]
sys.path.append(str(src_dir_location))

from src.Server.InputHandler import InputHandler
from src.Model.Constants import *


# Command line arguments:
#   -module (required): name of data extraction module to execute on each request from Unity.
#   -host_name (optional): ip address of host server runs on (defaults to "localhost").
#   -port (optional): port which server socket will bind to (defaults to 5555).
parser = argparse.ArgumentParser(description='Server to handle data extraction requests from Unity.')
parser.add_argument('-host_name', dest='host', default='localhost', help='host address. default is set localhost')
parser.add_argument('-port', dest='port', type=int, default=5555,
                    help='port for server to bind to. default is set to 5555')

app = flask.Flask(__name__)
app.config["DEBUG"] = False




@app.route(WORDCOUNTER_ENDPOINT, methods=['POST'])
def wordCounter():
    if request.content_type == CONTENT_JSON:
        try:
            parsed_json = request.get_json()
            if (FILE in parsed_json):
                res = input_handler.fileHandler(parsed_json[FILE])
            else:
                res = input_handler.uriHandler(parsed_json[URL])
        except Exception:
            ret = "ERROR: "+str(sys.exc_info()[0])
            return sendResponse(HTTPStatus.FORBIDDEN)
    elif request.content_type == CONTENT_TEXT:
        text = request.data
        res = input_handler.textHandler(text)
    return sendResponse(HTTPStatus.ACCEPTED) if res else sendResponse(HTTPStatus.CONFLICT)

@app.route(WORDSTATISTICS_ENDPOINT, methods=['GET'])
def wordStatistics():
    assert(request.content_type == CONTENT_JSON)
    parsed_json = request.get_json()
    word_counter = input_handler.wordCount(parsed_json[WORD])
    if (word_counter == -1):
        return sendResponse(HTTPStatus.BAD_REQUEST, message="The server encountered a problem during the search")
    else:
        return jsonify(word_counter), HTTPStatus.OK

def sendResponse(code, message=""):
    response = app.response_class(
        response=json.dumps(message),
        status=code,
        mimetype=CONTENT_JSON
    )
    return response


if __name__ == "__main__":
    args = parser.parse_args()
    app.config["ENV"] = DEFAULT
    input_handler = InputHandler(app.config['ENV'])
    app.run(host=args.host, port=args.port)

else:
    app.config["ENV"] = TEST
    input_handler = InputHandler(app.config['ENV'])