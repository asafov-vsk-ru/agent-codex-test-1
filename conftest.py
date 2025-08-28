import sys
from pathlib import Path

from dotenv import load_dotenv

# Load variables from .env if present
load_dotenv()

# Ensure project root is importable
ROOT_DIR = Path(__file__).resolve().parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
