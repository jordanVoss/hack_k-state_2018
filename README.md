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
   
   
<ul>
  <ls>TODO:  </ls></br>
  <ls>Implement Google Maps API:</ls></br>
    <ul><ls>Get local destiniations</ls></br>
      <ls>Sort these destination to the most likely to be wanted</ls></br>
      <ls>Build a path from current location to somewhere else  </ls></br>
        <ul><ls>Find intresting destinations on path*  </ls></ul>
      <ls>Send directions to users phone*</ls></ul></br>
    <ls>Implement Alexa API:  </ls></br>
      <ul><ls>Take in user information </ls> </br>
      <ls>Send the information to the Google Maps controller </ls></br> 
      <ls>Respond to the user </ls></ul> </br>
    <ls>Implement User control from the alexa  </ls></br>
      <ul><ls>The commands needed to get travel information  </ls></br>
        <ul><ls>How far away  </ls>
        <ls>Categories ("old","sight-seeing", "art", etc.)  </ls></ul>  </br>
      <ls>Alexa Intents  </ls></br>
      
</ul>  
  * items are stretch goals  
  
  
