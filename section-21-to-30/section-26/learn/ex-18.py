sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Split the sentence into words separated by spaces

words = sentence.split()
result = {word:len(word) for word in words}
print( result)