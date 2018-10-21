Hack K-State Fall 2018</br>
Project: </br>
My Conversationalist</br>
This is a bot made to interact with the user and have a very general conversation with them. It’s able to give the top news stories (from r/worldnews), give programming project ideas from a list of 100 ideas, and compliment/insult the user if they so wish. 
</br></br>
A large focus for this project was learning how Amazon Alexa skills work and how to interact with them. The initial push for this project, and getting the server built is thanks to a tutorial from Harrison Sentdex (tutorial found here: https://pythonprogramming.net/intro-alexa-skill-flask-ask-python-tutorial/) . I was able use this as a stepping stone to develop the rest of the project. </br></br>
The second focus of this project was expansibility. I wanted to be able to easily expand this project to allow for more skills and abilities to be brought in. I found that a lot of the projects I had been looking at to learn what to do just weren’t built to be expanded very easily. Because of this, I wrote my program so that the main file would only have the methods to catch intents from Alexa. They then called external files to get responses, this way there is no dependency on the Alexa script that would clutter it up.
</br></br>
Dependencies</br>
You will need the following libraries: </br>
•	Flask
•	Flask-ask*
•	Unicode
•	Json
•	Random
•	Requests
•	Time
</br>*In order to get this one to install I had to downgrade pip to 9.14
</br>You will also need ngrok to run the server locally. The Alexa API allows for use with a https server, but not http. Ngrok is a simple tunneling service that will give you a local certificate and so you will be able to run https. Note: Because of this you cannot make your skill public, only you will be able to access it. In order to make it public you need an actual https server.
</br></br>
Setting Up</br>
</br>You will need a free amazon developers account as well. Sign into this account and go to the Alexa console. Here you can select to make a new custom skill. Once you have the skill made, copy the contents of IntentsSchema.json into the “json” section of the build tab. This will set up all of the intents on the Alexa side. Next you will need to open a terminal and run ngrok in the same directory as your skills code. Use the command ngrok http 5000 this will bind it to http on port 5000. Then you can copy the https address that is showing in the terminal and go back to the amazon developer’s webpage. Under “endpoints,” select the https option and paste the url in the first box. Then click the drop down right below it and select the option that says your server key is from a “wildcard” certificate authenticator. Then you can go back to the build tab and click “Build Model.” This will set up the model for you the rest of the way. Once that its done, you can run the “alexaGetIdeas.py” script and test out your new conversational agent.

Sources</br>
Tutorial: https://pythonprogramming.net/intro-alexa-skill-flask-ask-python-tutorial/</br>
List of Programming Ideas: https://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/</br>
List of Compliments: https://www.verywellmind.com/positivity-boosting-compliments-1717559</br>
List of Insults: http://pun.me/pages/funny-insults.php</br>
</br>
Other Useful Links</br>
Flask-ask documentation: https://flask-ask.readthedocs.io/en/latest/</br>
Alexa Skill Development: https://developer.amazon.com/docs/ask-overviews/build-skills-with-the-alexa-skills-kit.html</br>

