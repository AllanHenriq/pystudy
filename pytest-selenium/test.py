import pytest

@pytest.mark.nondestructive
def test_example(selenium):
    selenium.get('http://www.example.com')