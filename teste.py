import os
from pathlib import Path
from time import sleep

from dotenv import load_dotenv


load_dotenv()


teste = os.environ.get('AWS_ACCESS_KEY_ID')
print(teste)
