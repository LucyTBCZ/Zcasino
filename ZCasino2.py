import os
import random
import math

gain=1000
start_one=True
while start_one==True:
	print("Welcome to the Z Casino!")
	print("You have", gain, "$! Would you play?")
	os.system("pause")
	start_two=True
	while start_two==True:
		choice=input("Yes or No? ")
		if choice=="Yes" or choice=="yes":
			start_three=True
			while start_three==True:
				try:
					print("You have", gain, "$")
					mise=input("How many would you play? ")
					mise=int(mise)
					if mise>gain:
						print("Sorry, you have not enought money.")
						start_three=True
					elif mise<=gain:
						print("You play", mise, "$")
						start_three=False
						start_four=True
						while start_four==True:
							try:
								number=input("Enter a number between 0 and 49: ")
								number=int(number)
								if number>=0 and number<=49 and number%2==0:
									print("You have selected", number, "BLACK")
									os.system("pause")
									croupier=random.randrange(50)
									print("The Roulette turn...")
									os.system("pause")
									if croupier%2==0:
										print("And it\'s the", croupier, "BLACK")
										os.system("pause")
									else:
										print("And it\'s the", croupier, "RED")
										os.system("pause")
									if number==croupier:
										thune=math.ceil(mise*3)
										print("You win", thune, "$! Congratulations!")
										gain+=thune
										os.system("pause")
									elif number%2==0 and croupier%2==0 or number%2==1 and croupier%2==1:
										flouz=math.ceil(mise/2)
										print("You win", flouz, "$! Congratulations!")
										gain+=flouz
										os.system("pause")
									else:
										print("Sorry, you loose this time!")
										gain-=mise
										os.system("pause")
									start_four=False
									start_three=False
									start_two=False
									start_one=True
								elif number>=0 and number<=49 and number%2==1:
									print("You have selected", number, "RED")
									os.system("pause")
									croupier=random.randrange(50)
									print("The Roulette turn...")
									os.system("pause")
									if croupier%2==0:
										print("And it\'s the", croupier, "BLACK")
										os.system("pause")
									else:
										print("And it\'s the", croupier, "RED")
										os.system("pause")
									if number==croupier:
										thune=math.ceil(mise*3)
										print("You win", thune, "$! Congratulations!")
										gain+=thune
										os.system("pause")
									elif number%2==0 and croupier%2==0 or number%2==1 and croupier%2==1:
										flouz=math.ceil(mise/2)
										print("You win", flouz, "$! Congratulations!")
										gain+=flouz
										os.system("pause")
									else:
										print("Sorry, you loose this time!")
										gain-=mise
										os.system("pause")
									start_four=False
									start_three=False
									start_two=False
									start_one=True
								else:
									print("Sorry, your number isn\'t between 0 and 49. Select another number, please.")
									start_four=True
							except ValueError:
								pass
								print("Sorry, I don\'t understand. Repeat your number, please.")
								start_four=True
							except TypeError:
								pass
								print("TypeError")
								start_one=True
				except ValueError:
					pass
					print("Sorry, I don\'t understand. Repeat, please.")
					start_one=False
					start_two=False
					start_three=True			
		elif choice=="No" or choice=="no":
			print("I wish to see you soon!")
			os.system("pause")
			start_one=True
			start_two=False
		else:
			print("Sorry, I don't understand your choice. Repeat please.")
			start_one=False
			start_two=True	