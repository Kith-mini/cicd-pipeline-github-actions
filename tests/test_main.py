import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app.main import add, greet

def test_add():
    assert add(2, 3) == 5

def test_greet():
    assert greet("Kith") == "Hello, Kith!"
