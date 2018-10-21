import random


def get_idea():
	with open('Data\Cleaned\programmingIdeas.txt', 'r') as file:
		ideas = file.readlines()
			
		return ideas[random.randint(0,len(ideas)-1)]

		