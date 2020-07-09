class Questions:
    def __init__(self,question,answers,item,correct):
        self.question= question
        self.answers = answers
        self.correct = correct
        self.items = item
    def callQuestion(self):
        print(self.question)
        for i in self.answers:
            print(i)
        return 'chose a answer'
    