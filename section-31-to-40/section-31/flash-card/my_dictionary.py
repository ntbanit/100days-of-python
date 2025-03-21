# space_1 , space_3, space_5, space_8, space_13
import pandas
import random
"""
Read the data from the english_ipa_words.csv file in the data folder.
Pick a random word/IPA pronunciation and put the word into the flashcard.
"""
class WordLearningDictionary:
    def __init__(self):
        self.current_word = ''
        self.prob_list = [1, 3, 5, 8, 13]
        self.spaced_words_list = [[], [], [], [], []]

        # not first time the program runs, read the saved file
        cnt_data_file = 0
        for i in range(len(self.prob_list)) :
            try:
                prob = self.prob_list[i]
                spaced_df = pandas.read_csv(f'data/data_spaced_{prob}.csv')
                self.spaced_words_list[i] = spaced_df.to_dict(orient="records")
                cnt_data_file += 1
            except Exception:
                print(f"Warning: No data for probability {prob} found. Skipping...")
                continue
        if cnt_data_file == 0:
            # first time the program runs, read the original file    
            word_df = pandas.read_csv("data/english_ipa_words.csv")
            self.spaced_words_list[0] = word_df.to_dict(orient="records")

        product = 1
        for prob in self.prob_list:
            product *= prob
        self.freq_list = [product // prob for prob in self.prob_list]
    
    def generate_new_word(self):
        combined = [] ;
        for i in range(0, len(self.freq_list)):
            combined += [(item, self.freq_list[i]) for item in self.spaced_words_list[i]]
        items, weights = zip(*combined)
        self.current_word = random.choices(items, weights=weights, k=1)[0]
        print(f"debug current_word: {self.current_word}")
        # print(f"debug English: {self.current_word["English"]}")
        # print(f"debug IPA: {self.current_word["IPA"]}")
        return self.current_word
    def save_progress(self):
        for i in range(len(self.spaced_words_list)):
            if len(self.spaced_words_list[i]) == 0:
                continue
            df = pandas.DataFrame(self.spaced_words_list[i])
            if df.columns.to_list() == list(range(df.shape[1])):
                df.columns = ['English', 'IPA']
            df.to_csv(f"data/data_spaced_{self.prob_list[i]}.csv", index=False)
            print(f"Saved progress for space_level_{self.prob_list[i]}")
    
    def tick_word_event(self):
        # for spaced repititions
        for i in range(len(self.spaced_words_list)):
            current_list = self.spaced_words_list[i]
            if self.current_word in current_list:
                current_list.remove(self.current_word)
                if i < len(self.spaced_words_list) - 1:
                    next_list = self.spaced_words_list[i+1]
                    next_list.append(self.current_word)
                break