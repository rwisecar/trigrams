"""A program that takes a txt file input and creates new similar new file."""

import io
from random import randint

story = []
trigrams_dict = {}


def open_file(text_file):
    """Open and read source text file."""
    source_file = io.open(text_file, 'r+')
    story.append(source_file.read().split())
    source_file.close()


def build_dictionary():
    """Build a dictonary for trigram analysis."""
    for i in range(len(story)):
        new_key = " ".join(story[i:i + 2])
        if new_key in trigrams_dict:
            trigrams_dict[new_key].append(story[i + 2])
        else:
            trigrams_dict[new_key] = [story[i + 2]]


def write_story(words):
    """Use trigram dictonary to build a new story."""
    new_story = trigrams_dict.keys()[randint(0, len(trigrams_dict) - 1)].split(" ")
    while len(new_story) < words:
        if " ".join(new_story[-2:]) in trigrams_dict:
            new_story.append(trigrams_dict[" ".join(new_story[-2:])])
        else:
            break
    return new_story
