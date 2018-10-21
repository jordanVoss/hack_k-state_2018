


from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode
from random import randint


##################Include local files################
import programmingIdeas as PI
import worldNews as WN
import listOptions as LO
import defaultAlexaIntents as DAI
import emotions


app = Flask(__name__)
ask = Ask(app, "/")



 



@app.route('/')
def homepage():
    return "hi there, how ya doin?"

@ask.launch
def start_skill():
    welcome_message = [
						'Hello there, what would you like to talk about?',
						'What can I do for you?',
						'I hope you\re haveing a great day, what\'s up?'
					]

    return question(welcome_message[randint(0,len(welcome_message)-1)])

# When the user says yes
@ask.intent("YesIntent")
def yes_intent():
    message = "Sounds good, what would you like?"
    return question(message).reprompt("Let me know if you want me to list your options.")

# Whenever the user says no	
@ask.intent("NoIntent")
def no_intent():
    message = "OK, let me know what you want to do."
    return question(message)

# Test that we are connected to the server, mostly just for fun
@ask.intent("TestConnectionIntent")
def test_connection():
	message = "Well of course I'm running, the circle is lit up isn't it?"
	return question(message).reprompt("Do you still want me on???")

# Give the user a programming project idea	
@ask.intent("ProgrammingIdeaIntent")
def programming_idea():
	idea = PI.get_idea()
	message = ("You could make a " + idea)
	return question(message)

# Tell the 	user what all the bot can do
@ask.intent("ListPossibilitiesIntent")
def list_choices():
	message = LO.list_options()
	return question(message).reprompt("So what will it be?")
	
# When the user compliments the bot
@ask.intent("ComplimentIntent")
def accept_compliment():
	message = emotions.compliment()
	return question(message).reprompt(emotions.giveCompliment())
	
# When the user askes for a compliment
@ask.intent("GetComplimentIntent")
def give_compliment():
	message = emotions.giveCompliment()
	return question(message)

# When the user insults the bot
@ask.intent("InsultIntent")
def accept_insult():
	doILeave = randint(0,1)
	
	if doILeave is 0: #Exit the program
		message = emotions.insult()
		message += "I'm leaving now. Bye."
		return statement(message)
	else: #Stay in the program
		message = emotions.insult()
		return question(message).reprompt(emotions.giveInsult())
		
# When the user asks for an insult
@ask.intent("GetInsultIntent")
def give_insult():
	message = emotions.giveInsult()
	return question(message)
	
# When the user thanks the bot
@ask.intent("ThankedIntent")
def get_thanked():
	message = emotions.thanked()
	return question(message)



#############SET UP THE DEFAULT INTENTS###################
	
@ask.intent("AMAZON.FallbackIntent")
def default_messages():
	return question(DAI.fallback())
	
@ask.intent("AMAZON.CancelIntent")
def cancel_intent():
	return statement(DAI.cancel())
	
@ask.intent("AMAZON.StopIntent")
def stop_intent():
	return statement(DAI.stop())
	
@ask.intent("AMAZON.HelpIntent")
def help_intent():
	list_choices()
	return
	
@ask.intent("AMAZON.NavigateHome")
def navigate_home_intent():
	return statement(DAI.goHome())

	
###########The next two blocks were originally written by Harrison Sentdex as part of a tutorial##########################
@ask.intent("WorldNewsIntent") # I did change the intent name so it fits better wiht this project
def share_headlines():
    message = WN.get_headlines(requests.Session())
    return question(message) # I changed this to question instead of statement so the program would keep running
    
if __name__ == '__main__':
    app.run(debug=True)
	
	
	
	







