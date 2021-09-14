import pytest
from ..Server.Server import app, WORDSTATISTICS_ENDPOINT, WORDCOUNTER_ENDPOINT, WORD, URL, FILE
from ..Server.InputHandler import *
from ..Server.InputHandler import InputHandler, DECODE_TYPE
import json
from pathlib import Path
import sys
## make src dir avlb for cmd operation
src_dir_location = Path(__file__).parents[2]
sys.path.append(str(src_dir_location))

TESTURL = 'https://en.wikipedia.org/wiki/Lemonade,_Inc.'
TESTFILE = "./src/Tests/testfile.txt"
TESTTEXT = "Hi! My name is (what?), my name is (who?), my name is Slim Shady"

@pytest.fixture()
def client():
    with app.test_client() as client:
        app.config["ENV"] = 'TEST'
        app.input_handler = InputHandler(app.config['ENV'])
        yield client

@pytest.mark.run(order=9)
def test_post_word_counter_api_url_return_202(client):
    clean_data()
    res = client.post(WORDCOUNTER_ENDPOINT, json={TYPE:URL, VALUE:TESTURL})
    assert res.status_code == 202

@pytest.mark.run(order=8)
def test_post_word_counter_api_text_return_202(client):
    clean_data()
    res = client.post(WORDCOUNTER_ENDPOINT, json={TYPE:TEXT, VALUE:TESTTEXT})
    assert res.status_code == 202

@pytest.mark.run(order=7)
def test_post_word_counter_api_file_return_202(client):
    clean_data()
    res = client.post(WORDCOUNTER_ENDPOINT, json={TYPE:FILE, VALUE:TESTFILE})
    assert res.status_code == 202

@pytest.mark.run(order=10)
def test_get_word_statistics_api_input_lemonade_should_return_115(client):
    res = client.get(WORDSTATISTICS_ENDPOINT+"?word=lemonade")
    expected_res_dict = {WORD_STRING: "lemonade", COUNTER_STRING: 115}
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