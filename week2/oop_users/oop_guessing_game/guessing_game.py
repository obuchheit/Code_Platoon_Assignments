class GuessingGame:

    def __init__ (self, answer):
        self.answer = answer
        self.isfalse = False

    def guess(self, user_guess):
        self.user_guess = user_guess
        if self.user_guess == self.answer: 
            self.isfalse = True
            return "correct"
        if self.user_guess > self.answer: 
            return "high"
        if self.user_guess < self.answer:
            return "low" 
        
    def solved(self):
        return self.isfalse

  