#!/usr/bin/python3
""" fucntion that prints a text with 2 new lines after/
    each of these characters: ., ?, and : """


ErrMsg = "text must be a string"


def text_indentation(text):
    """ function that prints a text with 2 new lines after/
        each of these characters: ., ?, and : """
    if type(text) is not str:
        raise TypeError(ErrMsg)
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            print(text[i], end="")
