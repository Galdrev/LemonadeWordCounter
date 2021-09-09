import pytest
from ..Model.WordStatistics import WordStatistics
from ..Server.InputHandler import InputHandler, DECODE_TYPE
from ..Model import Trie
from ..Model.Config import config
from pathlib import Path
import os
import pickle
import unittest
from unittest.mock import patch
import module

STATISTICSFILEPATH = "statisticsfilepathtest"
TESTFILE = "./testfile.txt"
TESTURI = "https://en.wikipedia.org/wiki/Lemonade,_Inc."
TESTTEXT = "Hi! My name is (what?), my name is (who?), my name is Slim Shady".encode(DECODE_TYPE)
config_env = config['TEST']
file_path = config_env[STATISTICSFILEPATH]
full_persistent_file_path = (Path(__file__).parent.parent).joinpath(file_path)
ih = InputHandler('TEST')

@pytest.mark.run(order=4)
def test_file_handler(clean_inputHandler_instance):
    test_file_path = Path(TESTFILE)
    assert ih.fileHandler(test_file_path) == True

@pytest.mark.run(order=5)
def test_uri_handler(clean_inputHandler_instance):
    assert ih.uriHandler(TESTURI) == True

@pytest.mark.run(order=6)
def test_text_handler(clean_inputHandler_instance):
    assert ih.textHandler(TESTTEXT) == True

@pytest.fixture()
def clean_inputHandler_instance():
    yield
    try:
        ih.word_stat.empty_statistics()
    except Exception:
        raise AssertionError
