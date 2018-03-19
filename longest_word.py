# Jacob Meadows
# 4th Period, Computer Programming
# March 6th, 2018
"""
What is the longest word in Alice in Wonderland? How many characters does it have?
"""


def longest_word():
    alice_text = open("alice.txt", "r")
    alice_text = alice_text.read()
    alice_text = alice_text.split()
    longest_word = ""
    for x in alice_text:
        if len(x) > len(longest_word):
            longest_word = x
    print("%s\n%i" % (longest_word, len(longest_word)))


longest_word()
