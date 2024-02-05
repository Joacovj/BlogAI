import openai
from os import remove
from dotenv import dotenv_values
from playsound import playsound

config = dotenv_values(".env")
keep_writing = True
openai.api_key = config['API_KEY']

# Using AI Voice to read the text by creating a .mp3 file

def textToSpeech(retrieve_blog):        
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=retrieve_blog
    )

    response.stream_to_file("output.mp3")
    

# Generating the paragraph with AI

def generate_blog(paragraph_topic):
    response = openai.completions.create(
        model = "gpt-3.5-turbo-instruct",
        prompt = "Write a paragraph about the following topic. " + paragraph_topic,
        max_tokens = 400,
        temperature = 0.3
    )

    retrieve_blog = response.choices[0].text    
    return retrieve_blog

generated_text = generate_blog("Music")
textToSpeech(generated_text)
print(generated_text)
playsound("output.mp3")
remove("output.mp3")


# Asking if program should keep writing other paragraph

while(keep_writing == True):
    answer = input("Write a paragraph? Y for yes, anything else for no. ")
    if(answer == 'Y'):
        paragraph_topic = input("What should this paragraph talk about? ")
        texto = generate_blog(paragraph_topic)
        textToSpeech(texto)
        print(texto)
        playsound("output.mp3") 
        remove("output.mp3")       
        
    else:
        keep_writing = False
        




    