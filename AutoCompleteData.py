from dataclasses import dataclass
from typing import List



class AutoCompleteData:
    def __init__(self, completed_sentence, source_text, offset, score):
        self.completed_sentence = completed_sentence
        self.source_text = source_text
        self.offset = offset
        self.score = score
    def __str__(self):
        return("complete sentence: "+str(self.completed_sentence)+ " source: "+self.source_text+" offset: "+str(self.offset)+" score: "+str(self.score)+"\n")

    # methods