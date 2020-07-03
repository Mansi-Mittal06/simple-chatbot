from chatterbot import chatbot
from chatterbot.trainers import ListTrainer
 
#creating a new chatbot
chatbot = Chatbot('Rosy')
trainer = ListTrainer(chatbot)
trainer.train([ 'hi, how can I help you!?'])
 
#getting a response from the chatbot
response = chatbot.get_response("I want a course")
print(response)
