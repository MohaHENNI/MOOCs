def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    
    score = 0
    for letter in word:
        score+= SCRABBLE_LETTER_VALUES [letter]
    
    score *= len (word)
    if len (word) == n:
        score += 50
    
    return score

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    dict = {}
    for elem in hand.keys ():
        dict [elem] = hand[elem]
    
    for letter in word:
        dict [letter] -= 1
        
        
    return dict

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    freq = getFrequencyDict(word)
    for letter in freq.keys():
        if letter not in hand or freq[letter] > hand [letter]:
            return False
    
    return word in wordList

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    length = 0
    
    for letter in hand.keys():
        length += hand[letter]
        
    return length

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
        # Keep track of the total score
    score = 0
    word = ''
    
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0 :
    
        # Display the hand
        print "Current Hand:",
        displayHand (hand)
        
        # Ask user for input
        word = str (raw_input('Enter word, or a "." to indicate that you are finished: '))
        # If the input is a single period:
        if word == ".":
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if not isValidWord (word, hand, wordList):
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
                print
            # Otherwise (the word is valid):
            else:
                word_score = getWordScore (word, n)
                score += word_score
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print ('"' + word+'" earned '+str(word_score) +' points. Total: '+str(score)+' points' )
                # Update the hand 
                hand = updateHand (hand, word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print (" Run out of letters. Total score: "+ str(score)+ " points.")


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    command = ""
    first_time = True
    
    while command != 'e':
        command = str (raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        
        if command == 'n':
            first_time = False
            hand = dealHand (HAND_SIZE)
            hand_save = hand.copy ()
            playHand (hand, wordList, HAND_SIZE)
        elif command == 'r':
            if not first_time:
                hand = hand_save
                playHand (hand, wordList, HAND_SIZE)
            else:
                print "You have not played a hand yet. Please play a new hand first!"
        elif command == "e":
            #EndGame
            break
        else:
            print "Invalid command."

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
   
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord (word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore (word,n)

            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
                
    # return the best word you found.
    return best_word


    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
   
    # Create a new variable to store the maximum score seen so far (initially 0)
    max_score = 0

    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None

    # For each word in the wordList
    for word in wordList:

        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord (word, hand, wordList):
            # Find out how much making that word is worth
            score = getWordScore (word,n)

            # If the score for that word is higher than your best score
            if score > max_score:
                # Update your best score, and best word accordingly
                max_score = score
                best_word = word
                
    # return the best word you found.
    return best_word
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score  = 0
    while calculateHandlen(hand) > 0 :
    
        # Display the hand
        print "Current Hand:",
        displayHand (hand)
        
        # Ask computer for input
        word = compChooseWord (hand, wordList, n)
        # If the word is None
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # Otherwise (the word is valid):
            word_score = getWordScore (word, n)
            score += word_score
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            print ('"' + word+'" earned '+str(word_score) +' points. Total: '+str(score)+' points' )
            # Update the hand 
            hand = updateHand (hand, word)
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print ("Total score: "+ str(score)+ " points.")