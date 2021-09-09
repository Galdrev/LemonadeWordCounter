import pytest
from ..Server.Server import app, WORDSTATISTICS_ENDPOINT, WORDCOUNTER_ENDPOINT, WORD, URL, FILE
from ..Server.InputHandler import *
from ..Server.InputHandler import InputHandler, DECODE_TYPE
import json


TESTURL = 'https://en.wikipedia.org/wiki/Lemonade,_Inc.'
TESTFILE = "./testfile.txt"
TESTTEXT = "Hi! My name is (what?), my name is (who?), my name is Slim Shady".encode(DECODE_TYPE)

@pytest.fixture()
def client():
    with app.test_client() as client:
        app.config["ENV"] = 'TEST'
        app.input_handler = InputHandler(app.config['ENV'])
        yield client

@pytest.mark.run(order=9)
def test_post_word_counter_api_url_return_202(client):
    clean_data()
    res = client.post(WORDCOUNTER_ENDPOINT, json={URL:TESTURL})
    assert res.status_code == 202

@pytest.mark.run(order=8)
def test_post_word_counter_api_text_return_202(client):
    clean_data()
    text_type = 'text/plain'
    headers = {
        'Content-Type': text_type,
        'Accept': text_type
    }
    res = client.post(WORDCOUNTER_ENDPOINT, data=TESTTEXT, headers=headers)
    assert res.status_code == 202

@pytest.mark.run(order=7)
def test_post_word_counter_api_file_return_202(client):
    clean_data()
    res = client.post(WORDCOUNTER_ENDPOINT, json={FILE:TESTFILE})
    assert res.status_code == 202

@pytest.mark.run(order=10)
def test_get_word_statistics_api_input_lemonade_should_return_32(client):
    res = client.get(WORDSTATISTICS_ENDPOINT, json={WORD:"lemonade"})
    expected_res_dict = {WORD_STRING: "lemonade", COUNTER_STRING: 32}
    res_json = res.data.decode(DECODE_TYPE).rstrip('\n')
    res_dict = json.loads(res_json)
    clean_data()
    assert res_dict == expected_res_dict


def clean_data():
    yield
    try:
        ws = WordStatistics.WordStatistics()
        ws.empty_statistics()
    except Exception:
        ae = AssertionError
        ae.args += "NOT RAN: Test could not empty InputHandler instance"
        raise ae