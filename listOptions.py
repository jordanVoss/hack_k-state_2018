from random import randint


				
def list_options():
	# All of the possible functions for the user to call
	possibilities = [
					'Get programming ideas, ',
					'Tell you the world news, ',
					'Test the connection to the server, ',
					'Accept compliments , ',
					'Give you compliments, ',
					'Receive insults, ',
					'Insult you right back, ',
					'List all of my capabilities, '
					]
				
	# A list of phrases to go inbetween the list, so it sounds more natural (hopefully)
	conjunctions = [
					'and',
					'and',
					'plus',
					'I will',
					'or',
					'perhaps even',
					'I suppose I could',
					'just because I like you, I\'ll help you'
				]
			
	#How many items go into the list before it gets dumped 
	MAX_ARRAY_SIZE = 3
	#So it's less likely that a conjunction is used repeaditly
	conjunctionList = []

	
			
	response = "Here's what I can do for you: I can " + possibilities[0]
	for i in possibilities:
		if i is possibilities[0]:
			continue
			
			
		conjunct = randint(0,len(conjunctions)-1)
		while conjunct in conjunctions:
			conjunct = randint(0,len(conjunctions)-1)
		conjunctionList.append(conjunct)
		
		if len(conjunctionList) is MAX_ARRAY_SIZE:
			conjunctionList.pop(0)
		
		response += (conjunctions[conjunct] + " " + i)
		
	response += ("...And that's all I can do for now.")
	
	return response
	
