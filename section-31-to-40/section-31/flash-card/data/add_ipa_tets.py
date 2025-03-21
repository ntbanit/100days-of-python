import os
import nltk
from nltk.corpus import cmudict

# Download the CMU Pronouncing Dictionary
nltk.download('cmudict', quiet=True)

# Initialize the CMU Pronouncing Dictionary
prondict = cmudict.dict()

# ARPAbet to IPA conversion dictionary
arpa_to_ipa_dict = {
    'AA': 'ɑ', 'AE': 'æ', 'AH': 'ʌ', 'AO': 'ɔ', 'AW': 'aʊ', 'AY': 'aɪ', 'B': 'b', 'CH': 'tʃ',
    'D': 'd', 'DH': 'ð', 'EH': 'ɛ', 'ER': 'ɝ', 'EY': 'eɪ', 'F': 'f', 'G': 'ɡ', 'HH': 'h',
    'IH': 'ɪ', 'IY': 'i', 'JH': 'dʒ', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'NG': 'ŋ',
    'OW': 'oʊ', 'OY': 'ɔɪ', 'P': 'p', 'R': 'r', 'S': 's', 'SH': 'ʃ', 'T': 't', 'TH': 'θ',
    'UH': 'ʊ', 'UW': 'u', 'V': 'v', 'W': 'w', 'Y': 'j', 'Z': 'z', 'ZH': 'ʒ'
}

def convert_arpa_to_ipa(arpa):
    ipa = []
    for phoneme in arpa:
        base = ''.join([c for c in phoneme if c.isalpha()])
        if base in arpa_to_ipa_dict:
            ipa.append(arpa_to_ipa_dict[base])
    return ''.join(ipa)

def get_ipa(word):
    word = word.lower()
    if word in prondict:
        arpa = prondict[word][0]
        return '/' + convert_arpa_to_ipa(arpa) + '/'
    return "N/A"  # Return N/A if no pronunciation is found

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Read words from the input file
input_file = os.path.join(current_dir, "test_data_output.txt")
output_file = os.path.join(current_dir, "words_with_ipa.txt")

# Check if input file exists
if not os.path.exists(input_file):
    print(f"Error: Input file '{input_file}' not found.")
else:
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for word in infile:
                word = word.strip()
                ipa = get_ipa(word)
                outfile.write(f"{word},{ipa}\n")

        print(f"IPA pronunciations have been added to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")