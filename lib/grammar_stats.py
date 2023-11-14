class GrammarStats:
    def __init__(self):
        self.correct = 0
        self.total_checked = 0
  
    def check(self, text):
        if len(text) == 0:
            self.total_checked += 1
            return False
        elif text[0].isupper() and text[-1] in '!?.':
            self.total_checked += 1
            self.correct += 1
            return True
        self.total_checked += 1
        return False
    
    def percentage_good(self):
        return int((self.correct/self.total_checked) * 100)