from EarleyParser import *


def test_True_1():
    word = 'g'
    grammar = {'^' : 'S', 'S' : 'g'}
    e = EarleyParser(grammar, word)
    assert e.earley() == True


def test_True_2():
    word = 'zxc'
    grammar = {'^' : 'S', 'S' : 'zA', 'A' : 'xB', 'B' : 'c'}
    e = EarleyParser(grammar, word)
    assert e.earley() == True


def test_False_1():
    word = '1'
    grammar = {'^' : 'S', 'S' : 'a'}
    e = EarleyParser(grammar, word)
    assert e.earley() == False


def test_False_2():
    word = 'abab'
    grammar = {'^' : 'S', 'S' : 'aB', 'B' : 'bA', 'A' : 'ba'}
    e = EarleyParser(grammar, word)
    assert e.earley() == False
