# Wordle Bot

Every iteration, we go through each of the 12000 words
* For every word, we go through each of the possible resulting 243 configurations if we guessed that word and get the “word_score"
    * For every configuration, we have to find the number of words that we could limit the problem to if it were true (“configuration score")
        * We do this by making dictionaries for “contains” and “not contains”
        * Dict contains = {“a”: {arise, arose, abash, …}, “b”: {bring, …}, …}
        * Take intersections for both the contains and not contains (and treat yellow and green the same), so if the word is “arise” and the “a” and “r” are yellow/green, we take the intersection of the sets of contains[“a”], contains[“r”], not_contains[“I”], not_contains[“s”] and not_contains[“e”]
    * Score for that word is the entropy (summation log whatever) of the configuration scores
* Choose the word with the highest word_score
