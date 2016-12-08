"""Tests trigrams.py."""

import io
import re
import pytest

story_file = io.open('short_sherlock.txt', 'r+')
story_file_read = story_file.read()
story_file_split = story_file_read.split('\W\s\d')

PARAMS_TABLE_STORY_FILE = [
    ['short_sherlock.txt', story_file_split]
]


@pytest.mark.parametrize('f, result', PARAMS_TABLE_STORY_FILE)
def test_open_file(f, result):
    """Running the function should equal the result"""
    from trigrams import open_file
    assert open_file(f) == result
