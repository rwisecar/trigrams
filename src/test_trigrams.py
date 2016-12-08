"""Tests trigrams.py."""

import io
import re
import pytest

story_file = io.open('short_sherlock.txt', 'r+')
story_file_read = story_file.read()
story_file_split = story_file_read.split(' ')

PARAMS_TABLE_STORY_FILE = [
    ['short_sherlock.txt', story_file_split]
]

PARAMS_TABLE_DICT = [
    [['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog'],
        {'the quick': ['brown'],
            'quick brown': ['fox'],
            'brown fox': ['jumped'],
            'fox jumped': ['over'],
            'jumped over': ['the'],
            'over the': ['lazy'],
            'the lazy': ['dog']}]
]


@pytest.mark.parametrize('f, result', PARAMS_TABLE_STORY_FILE)
def test_open_file(f, result):
    """Running the function should equal the result."""
    from trigrams import open_file
    assert open_file(f) == result


@pytest.mark.parametrize('s, result', PARAMS_TABLE_DICT)
def test_build_dictionary(s, result):
    """Test that building a dictionary works properly."""
    from trigrams import build_dictionary
    assert build_dictionary(s) == result


def test_build_write():
    from trigrams import write_story
    input_dict = {'the quick': ['brown', 'red']}
    stored = write_story(3, input_dict)
    assert stored == 'the quick brown' or stored == 'the quick red'


def test_build_write_length():
    from trigrams import write_story
    input_dict = {'the quick': ['brown', 'red']}
    assert len(write_story(3, input_dict).split()) == 3
