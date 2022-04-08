from operator import contains
import random
import time
import contains_dict
import not_contains_dict
import gen_perms
import math

class Game:
    
    guesses = []
    guess_results = []
    
    actual_word = None
    in_play = True
    won = False


    def __init__(self, words_guess):
        
        num = random.randrange(0, 2315, 1)
        #self.actual_word = words_guess[num]
        self.actual_word = "groin"

    def guess_and_check_word(self, guess):
        # return a string/array GNNNY

        # SMILS
        # SASSY

        answer_letters = {}
        for i in range(5):
            if self.actual_word[i] in answer_letters:
                answer_letters[self.actual_word[i]] += 1
            else:
                answer_letters[self.actual_word[i]] = 1


        output = ''
        for i in range(5):
            if self.actual_word[i] == guess[i]:
                output += 'G'
                answer_letters[self.actual_word[i]] -= 1
                
            elif guess[i] in answer_letters and answer_letters[guess[i]] > 0:
                output += 'Y'
                answer_letters[guess[i]] -= 1

            else:
                output += '_'
        
        self.guess_results.append(output)

        if guess == self.actual_word:
            self.in_play = False
            self.won = True
            print("You won in " + str(len(self.guess_results)) + " guesses!")
            print(self.guess_results)
        
        if len(self.guess_results) == 10 and self.won == False:
            self.in_play = False
            self.won = False
            print("You lost")
            print(self.actual_word)

        return output


class Bot:

    all_perms = gen_perms.all_perms
    
    # def __init__():
    #     pass
    
    def get_guess(self, possible_guesses):
        # go through all possible words 
        
        '''
        Every iteration, we go through each of the 12000 words
        * For every word, we go through each of the possible resulting 243 configurations if we guessed that word and get the “word_score"
            * For every configuration, we have to find the number of words that we could limit the problem to if it were true (“configuration score")
                * We do this by making dictionaries for “contains” and “not contains”
                    * Dict is further broken down by if a character is in a specific position in the word
                    * Dict contains = {“a”: {0: {arise, arose, abash, …}, 1: {catch, …}, …}, “b”: {1:{bring, …}, …}, …}
                * Take intersections for both the contains and not contains (and treat yellow and green the same), so if the word is “arise” and the “a” and “r” are yellow/green, we take the intersection of the sets of contains[“a”][0], contains[“r”][0], not_contains[“i”], not_contains[“s”] and not_contains[“e”]
            * Score for that word is the entropy (summation log whatever) of the configuration scores
        * Choose the word with the highest word_score
        '''
        
        max_entropy = 0
        best_guess = ""
        
        count = 0
        entropy_arr = []
        words_arr = []

        if len(possible_guesses)==1:
            return list(possible_guesses)[0]

        for word in possible_guesses:
            count += 1
            print(count)

            entropy = 0
            for config in self.all_perms:
                config_words = set()
            
                for i in range(len(config)):
                    char = config[i]
                    char_words = set()
                    
                    if char == 'G':
                        char_words = contains_dict.contains_dict[word[i]][i]
                    elif char == 'Y':
                        for x in range(5):
                            if x != i:
                                char_words = char_words.union(contains_dict.contains_dict[word[i]][x])
                    elif (len(set(word)) == len(word)):
                        char_words = not_contains_dict.not_contains_dict[word[i]]
                    
                    if i==0:
                        config_words = char_words
                    
                    config_words = config_words.intersection(char_words)
                    
                
                config_words = config_words.intersection(possible_guesses)

                
                if len(config_words) == 0:
                    config_words.add("xxxxx")

                if len(config_words) > len(possible_guesses):
                    print(word)
                    print(len(config_words))
                    print("NOT WORKING")
                    exit()

                #print(-1*(len(config_words)/len(possible_guesses) * math.log(len(config_words)/len(possible_guesses), 2)))
                entropy += -1*(len(config_words)/len(possible_guesses) * math.log(len(config_words)/len(possible_guesses), 2))

                
            entropy_arr.append(entropy)
            words_arr.append(word)
            #print(entropy)

            if entropy > max_entropy:
                best_guess = word
                max_entropy = entropy
        
        
        #print([x for _, x in sorted(zip(entropy_arr, words_arr))])
        #print(sorted(entropy_arr))


        return best_guess
            
def get_word_set(word, guess_result, word_space):
    
    config_words = {}
    
    for i in range(5):
        char = guess_result[i]
        char_words = set()

        if char == 'G':
            char_words = contains_dict.contains_dict[word[i]][i]
        elif char == 'Y':
            for x in range(5):
                if x != i:
                    char_words = char_words.union(contains_dict.contains_dict[word[i]][x]) 
        elif (len(set(word)) == len(word)): 
            char_words = not_contains_dict.not_contains_dict[word[i]]
            
        if i==0:
            config_words = char_words
        
        config_words = config_words.intersection(char_words)
    
    return config_words.intersection(word_space)


def simulate(num_simulations, answer_list, all_words):

    bot = Bot()
    wins = 0
    losses = 0

    # print(bot.get_guess(all_words))
    # boney

    for i in range(num_simulations):
        game = Game(answer_list)
        
        # first guess = arise
        counter = 0
        word_space = all_words

        while game.in_play and game.won == False:
            if counter == 0:
                bot_guess = "shiny"
            else:
                bot_guess = bot.get_guess(word_space)
            #bot_guess = bot.get_guess(word_space)
            print(bot_guess)
            guess_result = game.guess_and_check_word(bot_guess)
            print(guess_result)

            # use guess_result to filter the list of possible words

            word_space = get_word_set(bot_guess, guess_result, word_space)
            
            if bot_guess in word_space:
                word_space.remove(bot_guess)

            print("SIZE OF WORD_SPACE: " + str(len(word_space)))
            if len(word_space) == 1 or len(word_space)==2:
                print(word_space)
            print(word_space)
            counter += 1
            



def main():
    
    start_time = time.time()


    possible_answers = []
    all_words = []
    with open("words-guess.txt", "r", encoding="UTF-8") as in_file:
        for line in in_file:
            possible_answers.append(line.strip())
            all_words.append(line.strip())

    with open("words-all.txt", "r", encoding="UTF-8") as in_file:
        for line in in_file:
            all_words.append(line.strip())
    
    simulate(1, possible_answers, possible_answers)

    print (f"Time: {time.time()-start_time}")

if __name__ == "__main__":

    # Game length (the game will go on, but it will affect the % of wins)
    MAX_TURNS = 6

    main()
