# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
my_dict = nato_df.to_dict(orient="records")
# print(dict)
format_dict = {item["letter"]: item["code"] for item in my_dict}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = input("Enter a word: ").upper()
    try:
        # Remove duplicates while preserving order
        unique_word = ''.join(dict.fromkeys(word))
        word_codes = [format_dict[letter] for letter in unique_word]
        # print(f"Original word: {word}")
        # print(f"Word with duplicates removed: {unique_word}")
        print(f"NATO phonetic codes: {word_codes}")
        break 
    except KeyError:
        print("Sorry. Please try again with only alphabet letters.")

