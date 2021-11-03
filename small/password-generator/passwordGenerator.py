import random

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
L_ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
U_ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
SYMBOLS = ['@', '#', '$', '_', '?', '-', '*']

class generatePassword:	
	def __init__(self, min_length=15, max_length=30, uk=random.randint(1111, 9999)):
		if max_length < min_length:
			min_length, max_length = max_length, min_length
		self.unique_key = str(uk)
		self.min_length = min_length
		self.max_length = max_length

	def appendRandomData(self, password, rd, rla, rua, rs):
		_l = [rua, rs, rla, rd] 
		for i in _l:
			password.append(i)

	def randomPickup(self, pwd, pwd_length):
		for i in range(0, pwd_length, 4):
			r_digit = str(random.choice(DIGITS))
			r_u_alphabets = random.choice(U_ALPHABETS)
			r_l_alphabets = random.choice(L_ALPHABETS)
			r_symbol = random.choice(SYMBOLS)
			self.appendRandomData(pwd, r_digit, r_l_alphabets, r_u_alphabets, r_symbol)
		pwd.append(self.unique_key)
		random.shuffle(pwd)
		password_str = ''.join(pwd)
		return password_str

	def generate(self):
		password = []
		unique_key__len = len(self.unique_key)
		max_length__new = self.max_length - unique_key__len
		password_length = random.randint(self.min_length, max_length__new)
		g_password = self.randomPickup(password, password_length)
		return g_password

gp = generatePassword()
password = gp.generate()
print(password)