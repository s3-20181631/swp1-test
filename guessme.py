import random
class guessme:
	def __init__(self):
		self.trials = 0
		self.secret = 0
	def newgame(self,start_num):
		self.secret = random.randint(1,start_num+1)
		self.trials = 0
	def guess(self,guess_num):
		self.trials += 1
		if guess_num < self.secret:
			return "HIGH"
		elif guess_num > self.secret:
			return "LOW"
		else:
		
			return "SUCCESS!!",self.trials

