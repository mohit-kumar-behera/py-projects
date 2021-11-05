from collections import deque

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Flames:
	def __init__(self, yourName, partnerName):
		self.yourName = yourName
		self.partnerName = partnerName
		self.FLAMES = {
			'F':'Friendship',
			'L':'Love',
			'A':'Affection',
			'M':'Marriage',
			'E':'Enemy',
			'S':'Sibling'
		}

	def introGame(self):
		print("Welcome, " + bcolors.OKGREEN + self.yourName.upper() + bcolors.ENDC)
		print(bcolors.HEADER + "#" * 30 + bcolors.ENDC)
		print(bcolors.OKCYAN + "Flames game is very popular for kids and 99 percent off students in their playschool has played this game with their friends. They used to believe this game decides their future with their crush or best buddies. We still remember how good we laugh when we get Marriage after calculating Flames for our name and our best friend of the same gender. Good olden days right?" + bcolors.ENDC)
		print(bcolors.HEADER + "#" * 30 + bcolors.ENDC)
		
		for k,v in self.FLAMES.items():
			print(bcolors.OKGREEN + k + bcolors.ENDC + " -- " + bcolors.WARNING + v + bcolors.ENDC)
		
		print("-" * 30)
		print("\n")

	def formatName(self, yn, pn):
		yn, pn = yn.strip(), pn.strip() #strip forward and backword whitespaces
		yn, pn = yn.lower(), pn.lower() #lower all the cases
		yn, pn = yn.replace(" ",""), pn.replace(" ","") #delete any whitespace between the string
		return yn, pn

	def flameCount__func(self, yn__s, pn__s):
		uniqueChar__set = yn__s.symmetric_difference(pn__s)
		commonChar__set = yn__s.intersection(pn__s)
		len_uniqueChar__set = len(uniqueChar__set)
		len_commonChar__set = len(commonChar__set)
		if len_uniqueChar__set != 0:
			return len_uniqueChar__set  # if there is some unique characters in both the names
		return len_commonChar__set  # if there is no unique characters in both the names

	def strikeFLAMES(self,flc):
		deq = deque()
		for c in "FLAMES":
			deq.append(c)
		while len(deq) > 1:
			deq.rotate(-(flc-1))
			deq.popleft()
		return deq.pop()

	def displayFlamesResult(self, flr):
		flamesRelation = self.FLAMES.get(flr)
		print(bcolors.HEADER + "#" * 30 + bcolors.ENDC)
		print("Flames Result")
		print("-" * 30)
		print("The relationship between " + bcolors.WARNING + self.yourName.upper() + bcolors.ENDC +  " and " + bcolors.WARNING + self.partnerName.upper() + bcolors.ENDC + " is : " + bcolors.WARNING + flamesRelation + bcolors.ENDC)
		print(bcolors.HEADER + "#" * 30 + bcolors.ENDC)
		print("\n")	

	def test(self):
		self.introGame()
		yourName, partnerName = self.formatName(self.yourName, self.partnerName)
		yourName__set, partnerName__set = set(yourName), set(partnerName) #converting string name to a set
		flameCount = self.flameCount__func(yourName__set, partnerName__set)
		flameResult = self.strikeFLAMES(flameCount)
		self.displayFlamesResult(flameResult)


if __name__ == "__main__":
	print(bcolors.HEADER + "Flames Calculator" + bcolors.ENDC)
	print("-"*30)
	yourName = input("What is your Name ? -- ")
	partnerName = input("What is your Partner Name ? -- ")
	print("\n")
	flameTest = Flames(yourName, partnerName)
	flameTest.test()

