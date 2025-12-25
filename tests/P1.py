import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../P1')))

from helloworld import greet

def test_helloworld():
    assert greet() == "Hello, World!"

def test_helloworld_type():
    assert isinstance(greet(), str)
