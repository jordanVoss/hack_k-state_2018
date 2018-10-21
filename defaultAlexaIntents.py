from random import randint


def fallback():
	message = [
				'I\'m afaid I don\'t understand. Could you please say that again?',
				'Could you repeat yourself for me?',
				'I\'m sorry, I didn\'t catch that',
				'I\'m not quite sure how to respond to that'
			]
	return chooseResponse(message)

def cancel():
	return endConversation()
	
def stop():
	return endConversation()
	
def goHome():
	message = [
				'Alright, I\'m sending you back. Have a safe trip and don\'t be a stranger!',
				'Enjoy the rest of your day!',
				'And off you go.',
				'Well if that\'s what you really want, I won\'t stop you'
			]
	return chooseResponse(message)
	
def help():
	return #in this one it will call the list function
	
	
#For both the cancel and stop intents	
def endConversation():
	message = [
				'I hope I was able to help.',
				'Don\'t forget to visit!',
				'It\'s been wonderful talking to you!',
				'And off you go now, you don\'t want to be late to whatever your next thing is!'
			]
	return chooseResponse(message)
	
# Choose a random response
def chooseResponse(messages):
	return messages[randint(0,len(messages)-1)]
	
	

	
	
	
	