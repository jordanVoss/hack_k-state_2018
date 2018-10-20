# hack_k-state_2018
For K-States hackathon Fall 2018

Members:
Jordan Voss
Parker ---
----

Idea: Travel Planning App for Google Home/Alexa
  
Functionality Ideas:
  1. Locate intresting destinations within X miles. Where X is determined by the users choice.
  2. Ask it to plan a trip from X to Y
    2.1 Find Z extra things to do on the way. Where Z is defined by the users choice.
    2.2 Send path to google maps for the user
    
  Goals:
    Implement 1, 2.1
    
  Stretch Goals:
    2.2
    
  Whats Needed:
    Find database of locations to visit
      Possibly make one by scraping information off of a website
    Get the google home API to work
      Get the Alexa API to work
    Work with the google maps API
    
    
    
  API Sources:
    Get paces from google maps: https://github.com/slimkrazy/python-google-places
    
    Alexa interaction: https://github.com/alexa/alexa-skills-kit-sdk-for-python
    
  TODO:  
    Implement Google Maps API:  
      Get local destiniations  
      Sort these destination to the most likely to be wnated  
      Build a path from current location to somewhere else  
        Find intresting destinations on path*  
      Send directions to users phone*  
    Implement Alexa API:  
      Take in user information  
      Send the information to the Google Maps controller  
      Respond to the user  
    Implement User control from the alexa  
      The commands needed to get travel information  
        How far away  
        Categories ("old","sight-seeing", "art", etc.)  
        Alexa Intents  
  * items are stretch goals  
  
  
