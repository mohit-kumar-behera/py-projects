from game_data import data 
from art import logo, vs
import random

class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


class higherLower():
	def __init__(self):
		self.game_over = False
		self.choice = ['a','b']

	def random_account(self):
		""" Return a Random account from data """
		return random.choice(data)

	def format_data(self, account):
		""" Takes an account and return a printable representation """
		name = account['name']
		short_bio = account['description']
		country = account['country']
		return f"{name}, a {short_bio}, from {country}"

	def get_followers(self,account):
		""" Takes an account and return followers of that account """
		return account['follower_count']

	def check_answer(self,guess,afc,bfc):
		""" Checks whether user has guessed the account with more followers or not correctly """
		"""
		afc - account A followers
		bfc - account B followers
		"""
		if afc > bfc:
			return guess == "a"
		else:
			return guess == "b"

	def start(self):
		print(logo)
		print("-" * 40)
		
		score = 0
		account_b = self.random_account()
		while not self.game_over:
			account_a = account_b
			account_b = self.random_account()
			
			while  account_a == account_b:
				account_b = self.random_account()
			
			print(bcolors.WARNING + f"Compare A: {self.format_data(account_a)}.")
			print(vs)
			print(f"Against B: {self.format_data(account_b)}" + bcolors.ENDC)
			guess = input(bcolors.OKCYAN + "Who has more followers? Type 'A' or 'B': " + bcolors.ENDC).lower()
			
			while not guess in self.choice:
				guess = input("You have only two choices A or B. Type 'A' or 'B': ").lower()
			
			account_a_followers = self.get_followers(account_a)
			account_b_followers = self.get_followers(account_b)
			is_correct = self.check_answer(guess,account_a_followers,account_b_followers)
			
			if is_correct:
				score += 1
				print(bcolors.OKGREEN + "You're right! Current score: " + bcolors.ENDC + bcolors.WARNING + str(score) + bcolors.ENDC + "\n")
			else:
				self.game_over = True
				print(bcolors.FAIL + "Sorry, that's wrong. Final score: " + bcolors.ENDC + bcolors.WARNING + str(score) + bcolors.ENDC + "\n")

game = higherLower() 
game.start()