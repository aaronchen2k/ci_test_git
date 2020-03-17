import pytest

def test_upper():
    assert 'foo'.upper() == 'FOO'

class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x