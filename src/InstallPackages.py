import sys
import subprocess


subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pathlib'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'configparser'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'flask'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'argparse'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pytest'])


