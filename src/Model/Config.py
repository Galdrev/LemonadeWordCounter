import configparser
from pathlib import Path

config = configparser.ConfigParser()
config.sections()
persistent_file = str(Path(__file__).parent.parent.parent)
config.read(persistent_file+'/ConfigurationParameters/config.ini')
