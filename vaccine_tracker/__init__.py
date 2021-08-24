from dotenv import load_dotenv
from pathlib import Path

__version__ = "0.1.0"

DOTENV_PATH = Path(__file__).parent.with_name(".env")

if DOTENV_PATH.is_file():
    load_dotenv(DOTENV_PATH)
