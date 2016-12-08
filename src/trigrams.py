"""A program that takes a txt file input and creates new similar new file."""

import io
from random import choice, randint


def open_file(text_file):
    """Open and read source text file."""
    source_file = io.open(text_file, 'r+')
    story = source_file.read().split('\W\s\d')
    source_file.close()
    return story


def build_dictionary(story):
    """Build a dictonary for trigram analysis."""
    trigrams_dict = {}
    for i in range(len(story) - 2):
        new_key = " ".join(story[i:i + 2])
        if new_key in trigrams_dict:
            trigrams_dict[new_key].append(story[i + 2])
        else:
            trigrams_dict[new_key] = [story[i + 2]]
    return trigrams_dict


def write_story(words, trigrams_dict):
    """Use trigram dictonary to build a new story."""
    new_story = choice(trigrams_dict.keys()).split(" ")
    while len(new_story) < words:
        if " ".join(new_story[-2:]) in trigrams_dict:
            key_number = " ".join(new_story[-2:])
            new_story += [choice(trigrams_dict[key_number])]
        else:
            new_story += choice(trigrams_dict.keys()).split(" ")
    return " ".join(new_story)


if __name__ == '__main__':
    print("Please pick a story, and I will make another just like it.")
    story_choice = str(input("Please enter a file path for your story. "))
    print("How many words should your story be?")
    length_choice = int(input("Please enter a number. "))
    write_story(length_choice, build_dictionary(open_file(story_choice)))
