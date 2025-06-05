# setup_db.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

from config import engine
from models import Base