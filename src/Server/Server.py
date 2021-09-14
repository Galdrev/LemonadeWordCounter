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
    res = None
    if request.content_type == CONTENT_JSON:
        try:
            parsed_json = request.get_json()
            if not checkJsonValidity(parsed_json):
                return sendResponse(HTTPStatus.BAD_REQUEST,
                                    "Invalid input - the input should created as JSON object with type and value attributes")
            type, value = parsed_json[TYPE], parsed_json[VALUE]
            if type == FILE:
                res = input_handler.fileHandler(value)
            elif type == URL:
                res = input_handler.uriHandler(value)
            elif type == TEXT:
                res = input_handler.textHandler(value)
        except Exception:
            ret = "ERROR: "+str(sys.exc_info()[0])
            return sendResponse(HTTPStatus.FORBIDDEN, ret)
    return sendResponse(HTTPStatus.ACCEPTED, "Accepted") if res else sendResponse(HTTPStatus.CONFLICT, "Could not load data to the server")

@app.route(WORDSTATISTICS_ENDPOINT, methods=['GET'])
def wordStatistics():
    if (request.args.get(WORD_QUERY) is None) or (not request.args.get(WORD_QUERY)):
        return sendResponse(HTTPStatus.BAD_REQUEST, message="The server could not locate the word input")
    word = request.args.get(WORD_QUERY)
    word_counter = input_handler.wordCount(word)
    if (word_counter == -1):
        return sendResponse(HTTPStatus.BAD_REQUEST, message="The server encountered a problem during the search")
    else:
        return sendResponse(HTTPStatus.OK, word_counter)

def sendResponse(code, message=""):
    response = app.response_class(
        response=json.dumps(message),
        status=code,
        mimetype=CONTENT_JSON
    )
    return response

def checkJsonValidity(json_data):
    if (TYPE in json_data and VALUE in json_data):
        return True
    return False

if __name__ == "__main__":
    args = parser.parse_args()
    app.config["ENV"] = DEFAULT
    input_handler = InputHandler(app.config['ENV'])
    app.run(host=args.host, port=args.port)

else:
    app.config["ENV"] = TEST
    input_handler = InputHandler(app.config['ENV'])