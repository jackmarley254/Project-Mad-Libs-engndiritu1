#from gtts import gTTS
#from replit2 import audio as a


#hello = "I am a Jackson"


#input("I live in a city called:")
#tts = gTTS(hello)
#tts = gTTS(city)
#("hello.mp3".mp3"1)
#tts.save("hello.mp3")

#c
#tts.save("city.mp3")

#print(hello)
#print(city)

from gtts import gTTS
from replit2 import audio as a
#import playsound

# Story template with blanks
story = """
Once upon a time, there was a [adjective] [noun] named [name]. 
[name] lived in a [adjective] [place]. 
One day, [name] decided to [verb] to [place].
"""

# Prompting user for words
adjective1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
name = input("Enter a name: ")
place_adjective = input("Enter an adjective for a place: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")

# Filling in the blanks in the story
story = story.replace("[adjective]", adjective1)
story = story.replace("[noun]", noun1)
story = story.replace("[name]", name)
story = story.replace("[place]", place_adjective)
story = story.replace("[place]", place)
story = story.replace("[verb]", verb)

# Printing the completed story
print(story)

# Converting the story to speech
tts = gTTS(story)
tts.save("mad_libs_story.mp3")

# Playing the speech
#playsound.playsound("mad_libs_story.mp3")
player = a.play_file("mad_libs_story.mp3", 1)