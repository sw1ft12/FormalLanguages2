from EarleyParser import *


def main():
    grammar = {'^' : 'S'}
    number_of_rules = int(input())
    for k in range(number_of_rules):
        inp = input()
        outp = input()
        grammar[inp] = outp

    word = input()
    e = EarleyParser(grammar, word)
    if(e.earley()):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()


