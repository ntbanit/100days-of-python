# space_1 , space_3, space_5, space_8, space_13
import pandas
import random

class WordLearningDictionary:
    def __init__(self):
        self.current_word = ''
        self.prob_list = [1, 3, 5, 8, 13]

        try :
            # not first time the program runs, read the saved file
            spaced_data_files = [f'data_spaced_{prob}.csv' for prob in self.prob_list]
            spaced_df_list = [pandas.read_csv(file) for file in spaced_data_files]
            self.spaced_dicts = [df.to_dict(orient="records")  for df in spaced_df_list]
        except FileNotFoundError:
            # first time the program runs, read the original file
            self.spaced_dicts = [{}, {}, {}, {}, {}]
            word_df = pandas.read_csv("data/english_ipa_words.csv")
            self.spaced_dicts[0] = word_df.to_dict(orient="records")

        product = 1
        for prob in self.prob_list:
            product *= prob
        self.freq_list = [product // prob for prob in self.prob_list]
    
    def generate_new_word(self):
        combined = [] ;
        for i in range(0, len(self.freq_list)):
            combined += [(item, self.freq_list[i]) for item in self.spaced_dicts[i]]
        items, weights = zip(*combined)
        self.current_word = random.choices(items, weights=weights, k=1)[0]
        return self.current_word
    def save_progress(self):
        for i in range(len(self.spaced_dicts)):
            df = pandas.DataFrame(self.spaced_dicts[i])
            df.to_csv(f"data_spaced_{self.prob_list[i]}.csv", index=False)
            print(f"Saved progress for space_level_{self.prob_list[i]}")
    
    def tick_word_event(self):
        # for spaced repititions
        for i in range(len(self.spaced_dicts)):
            if self.current_word in self.spaced_dicts[i]:
                self.spaced_dicts[i].remove(self.current_word)
                if i < len(self.spaced_dicts) - 1:
                    self.spaced_dicts[i+1].append(self.current_word)
                break