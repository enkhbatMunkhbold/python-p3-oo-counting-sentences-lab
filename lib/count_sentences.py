#!/usr/bin/env python3

class MyString:

  def __init__(self, value=""):
    self._value = value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")

  def is_sentence(self):
    return self._value[-1] == '.'
  
  def is_question(self):
    return self._value[-1] == '?'
  
  def is_exclamation(self):
    return self._value[-1] == '!'
  
  def count_sentences(self):
    sum = 0
    if(len(self._value) == 0):
      return sum
    else:
      sentence_list = self.value.split(' ')
    
      for sentence in sentence_list:
        if sentence[-1] == '.' or sentence[-1] == '?' or sentence[-1] == '!':
          sum += 1
      return sum
