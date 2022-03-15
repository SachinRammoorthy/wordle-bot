# Wordle Bot

## Strategy

Every iteration, we go through each of the 12000 words
* For every word, we go through each of the possible resulting 243 configurations if we guessed that word and get the “word_score"
    * For every configuration, we have to find the number of words that we could limit the problem to if it were true (“configuration score")
        * We do this by making dictionaries for “contains” and “not contains”
            * Dict is further broken down by if a character is in a specific position in the word
            * Dict contains = {“a”: {0: {arise, arose, abash, …}, 1: {catch, …}, …}, “b”: {1:{bring, …}, …}, …}
        * Take intersections for both the contains and not contains (and treat yellow and green the same), so if the word is “arise” and the “a” and “r” are yellow/green, we take the intersection of the sets of contains[“a”][0], contains[“r”][0], not_contains[“i”], not_contains[“s”] and not_contains[“e”]
    * Score for that word is the entropy (summation log whatever) of the configuration scores
* Choose the word with the highest word_score


## Tasks

1. Preprocessing (make contains and not contains dictionaries)
2. Find the best first word
3. Logic of the workflow




## Wordle Simulator
* Game Class
    * guess_and_check_word(): input: Arise - apple, output:GNNNG - function to check the word 
    * Member variables
        * words guessed so far 

## Handling Edge Cases
    # problem: how to handle double letters
    
    # word = LEAAL
    # answer = HELLO
    # config = YG__Y
    # intersect: contains[l][1234], contains[e][1], not_contains[a], not_contains[a], contains[l][0123]
    # case: works
    
    #word = aboat
    #answer = abate
    #config = GG_YY
    # intersect: contains[a][0], contains[b][1], not_contains[o], contains[a][0] [1] [2] [4], contains[t][0] [1] [2] [3]
    # diagnosis: works
    
    #word = aboot
    #answer = about
    #config = GGG_G
    # intersect: cont[a][0], cont[b][1], cont[o][2], not_contain[o], cont[t][4]
    # case _G or G_ or Y_ you cannot intersect the not contains that the blank character gave

    #word = abuxu
    #anser = about
    # config = GGY__

    #word = abuut
    #answer = about
    # config = GG_GG

    #similar to GGY_G
    
    #word = aboot
    #answer = abate
    #config = GG__Y
    # diagnosis: works

    #word = aboto
    #answer = aboot
    #config = GGGYY
    # case: works


