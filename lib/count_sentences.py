#!/usr/bin/env python3

import re
import re

import re

class MyString:
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        if not isinstance(self.value, str):
            print("The value must be a string.")
            return 0

        if not self.value:
            return 0

        # Split the string on '.', '?', and '!' and remove empty strings
        sentences = [sentence for sentence in re.split(r'[.!?]', self.value) if sentence.strip()]
        return len(sentences)


