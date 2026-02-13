import random

def hangman():
    random_individual_word = []
    words_list = ["summer", "fall", "winter", "spring", "monster", "skeletons", "mermaid", "robot"
             "cigars", "cig", "hot", "giasfclfebrehber", "horror", "sans", "papyrus", "swap", "fell", "fresh", "nightmare", "edge", "reaper", "geno", "gaster", "gasterblastermasterdisaster", "spaghetti", "ink" "error", "dust", "killer", "swapfell", "birdtale", "mafiatale"]
    
    words_random_word = random.choice(words_list)
    length_of_random_word = len(words_random_word)
    the_little_positions = length_of_random_word * " _ "
    the_split_positions = the_little_positions.split()
    

    for word in words_random_word:
        random_individual_word.append(word)
    
    # print("<^>")
    # print(random_individual_word)

    lives_left = 6
    users_guess = []
    while True:
        print(the_little_positions)
        guess = input("Guess a letter!: ")
        if guess in random_individual_word:
            for i, char in enumerate(random_individual_word):
                if char == guess:
                    the_split_positions[i] = guess
                    # idx = random_individual_word.index(guess) #index get the postion of the character 
                    
            print(f"{guess} is in the word!")
            users_guess.append(guess)
            print(the_split_positions)
            print(f"Current guessed words {users_guess}")
            if the_split_positions == random_individual_word:
                print(f"You win! the word is {words_random_word}")
                break

        else:
            lives_left -= 1
            print(f"{guess} is not in the word! {lives_left} lives left")
            if lives_left == 0:
                print(f"You lose! the word was {words_random_word}")
                break

hangman()
            
