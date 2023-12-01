class EarleyParser:

    class Situation:
        input = ''
        output = ''
        index = 0
        point = 0


        def __init__(self, input, output, index, point):
            self.input = input
            self.output = output
            self.index = index
            self.point = point


        def __eq__(self, s):
            return (self.output == s.output and self.input == s.input and 
            self.point == s.point and self.index == s.index)


        def __hash__(self):
            return hash((self.input, self.output, self.point, self.index))


    grammar_rules = dict()
    situations = dict()
    word = ''


    def __init__(self, rules, word):
        self.situations = {i : set() for i in range(len(word) + 1)}
        situation = self.Situation('^', 'S', 0, 0)
        self.situations[0].add(situation)
        self.grammar_rules = rules
        self.word = word


    def scan(self, index, letter):
        for s in self.situations[index]:
            if s.output[s.point] == letter:
                self.situations[index + 1].add(self.Situation(s.input, 
                s.output, s.index, s.point + 1))


    def predict(self, index):
        lst = []
        for s in self.situations[index]:
            if s.point < len(s.output):
                for nonTerm in self.grammar_rules.keys():
                    if nonTerm == s.output[s.point]:
                        lst.append(self.Situation(s.output[s.point], 
                        self.grammar_rules[nonTerm], index, 0))

        for s in lst:
            self.situations[index].add(s)


    def complete(self, index):
        lst = []
        for s in self.situations[index]:
            if s.point == len(s.output):
                for s_ in self.situations[s.index]:
                    lst.append(self.Situation(s_.input, s_.output, 
                    s_.index, s_.point + 1))

        for s in lst:
            self.situations[index].add(s)


    def changeDi(self, start, end, index):
        while start != end:
            start = end
            self.predict(index)
            self.complete(index)
            end = len(self.situations[index])        


    def earley(self):
        start = len(self.situations[0])
        self.predict(0)
        self.complete(0)
        end = len(self.situations[0])

        self.changeDi(start, end, 0)

        for i in range(1, len(self.word) + 1):
            self.scan(i - 1, self.word[i - 1])
            start = len(self.situations[i])
            self.predict(i)
            self.complete(i)
            end = len(self.situations[i])

            self.changeDi(start, end, i) 

        for s in self.situations[len(self.word)]:
            if s.input == '^' and s.output == 'S' and s.index == 0 and s.point == 1:
                return True

        return False
