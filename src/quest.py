class Questions:
    def __init__(self,question,answers,items,correct):
        self.question= question
        self.answers = answers
        self.correct = correct
        self.items = items
    def callQuestion(self):
        print(self.question)
        for i in self.answers:
            print(i)
        return 'chose a answer'
    