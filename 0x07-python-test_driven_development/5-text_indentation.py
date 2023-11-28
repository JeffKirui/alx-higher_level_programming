#!/usr/bin/python3

""" Method for tex_indentation method. """


def text_indentation(text):
    """ Method for adding 2 new lines after '.?:' chars. """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ Check if the text contains any of this characters. """
    text = text.replace(".", ".\n\n")
    text = text.replace(":", ":\n\n")
    text = text.replace("?", "?\n\n")
    text = text.split("\n")

    for line in range(0, len(text)):
        print("{}".format(text[line].strip()), end=(
            "" if (line == len(text) - 1) else "\n"))
