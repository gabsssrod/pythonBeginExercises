import io
import sys
sys.stdout = buffer = io.StringIO()
import app
import re
import os
import pytest

@pytest.mark.it('1. You need to use the function print()')
def test_for_file_output(capsys):
    path = os.path.dirname(os.path.abspath(__file__))+'/app.py'
    with open(path, 'r') as content_file:
        content = content_file.read()
        regex = r"print\("
        assert re.match(regex, content) != None

@pytest.mark.it('2. Your code needs to print Hello World! on the console')
def test_for_console_log(capsys):
    captured = buffer.getvalue()
    assert captured == "Hello World!\n" #add \n because the console jumps the line on every print

