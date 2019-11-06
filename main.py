 #normal string: "Theres no one here" 
  #'\t' #tab
  #'\n' #newline
  #'\a' #beeping noise
import random
import time

alert = '\a' + '\a' + '\a' + '\a' + '\a' + '\a' + '\a' #creates an alert sound for input

x = 'y'

while x == 'y':
  question = input('Ask a question' + '\t' + alert)
  responses = [
    "Yes",
    "No",
    "Maybe",
    "Try again later",
    "I don't understand, try again.",
    "You will be fine.",
    "Be careful today",
    ]
  
  specificResponses = [
    "I feel great, thanks for asking!",
    "If you try hard enough.",
    
  ]
  
  if question == "How do you feel today" or question == "How u feelin" or question == "How are you feeling":
    time.sleep(3.5)
    print(specificResponses[0] + alert) #Example of fine tuning the question
  elif question == "Will I pass Mrs. Miller":
    time.sleep(3.5)
    print(specificResponses[1] + alert) 
  elif question == "Am I sexy" or question == "Do I look good":
    answer = random.randrange(0, 3)
    time.sleep(3.5)
    print(responses[answer] + alert)
  elif question == 'Is cheerleading a sport':
    answer = random.randrange(0, 3)
    time.sleep(3.5)
    print(responses[answer] + alert)
  else:
    time.sleep(3.5)
    print(random.choice(responses) + alert)
  
  time.sleep(3.5)
  x=input('Do you wanna ask another question? y=yes, n=no' + '\t' + alert)