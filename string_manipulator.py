#!/usr/bin/env python3
"""
String Manipulator - Daily Coding Practice
Date: September 10, 2025

A comprehensive string manipulation class for daily coding practice.
This file will be updated with additional features through multiple commits.
"""

class StringManipulator:
      """A class for various string manipulation operations."""

    def __init__(self):
              self.operations_count = 0

    def reverse_string(self, text):
              """Reverse a given string."""
              self.operations_count += 1
              return text[::-1]

    def count_vowels(self, text):
              """Count the number of vowels in a string."""
              self.operations_count += 1
              vowels = 'aeiouAEIOU'
              return sum(1 for char in text if char in vowels)

    def capitalize_words(self, text):
                  """Capitalize the first letter of each word."""
                  self.operations_count += 1
                  return ' '.join(word.capitalize() for word in text.split())

    def count_consonants(self, text):
                  """Count the number of consonants in a string."""
                  self.operations_count += 1
                  vowels = 'aeiouAEIOU'
                  return sum(1 for char in text if char.isalpha() and char not in vowels)

    def is_palindrome(self, text):
                  """Check if a string is a palindrome (ignoring case and spaces)."""
                  self.operations_count += 1
                  cleaned = ''.join(char.lower() for char in text if char.isalnum())
                  return cleaned == cleaned[::-1]

if __name__ == '__main__':
      # Demo functionality
      manipulator = StringManipulator()

    test_string = 'Hello World'
    print(f'Original: {test_string}')
    print(f'Reversed: {manipulator.reverse_string(test_string)}')
    print(f'Vowels: {manipulator.count_vowels(test_string)}')
    print(f'Operations performed: {manipulator.operations_count}')

    # Test new methods added in second commit
    print(f'Capitalized: {manipulator.capitalize_words(test_string)}')
    print(f'Consonants: {manipulator.count_consonants(test_string)}')
    print(f'Is palindrome: {manipulator.is_palindrome("racecar")}')
    print(f'Total operations: {manipulator.operations_count}')
