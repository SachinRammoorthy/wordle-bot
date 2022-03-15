from operator import contains
import random
import time
import contains_dict
import not_contains_dict
import gen_perms

class Game:
    
    guesses = []
    guess_results = []
    
    actual_word = None
    in_play = True
    won = False


    def __init__(self, words_guess):
        
        num = random.randrange(0, 2315, 1)
        #self.actual_word = words_guess[num]
        self.actual_word = "scoop"

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
            print("You won")
        
        if len(self.guess_results) == 6 and self.won == False:
            self.in_play = False
            self.won = False
            print("You lost")
            print(self.actual_word)

        return output


class Bot:

    all_perms = gen_perms.all_perms
    
    def __init__():
        pass
    
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
        #for word in possible_guesses:
            

        

        pass
        


def simulate(num_simulations, answer_list):

    bot = Bot()
    wins = 0
    losses = 0
    for i in range(num_simulations):
        game = Game(answer_list)

        while game.in_play and game.won == False:
            bot_guess = bot.get_guess(game)
            guess_result = game.guess_and_check_word(bot_guess)
            


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
    
    simulate(1, possible_answers, all_words)

    print (f"Time: {time.time()-start_time}")

if __name__ == "__main__":

    # Game length (the game will go on, but it will affect the % of wins)
    MAX_TURNS = 6

    main()
