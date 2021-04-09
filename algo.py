import unidecode

'''
Algorithm made by ARRZ.DEV
Thanks <3
'''

def similarity_algo(string1, string2): #returns a probability
    if not string1 or not string2:
        return 'missing parameter'

    def sort_funct(string): #function to sort each word by a 'unique' id
        id_ = 0

        for letter in string: #add to the id the ordinal of each letter in that string
            id_ += ord(letter)

        #this is to make it even more 'unique' --
        id_ += ord(string[0]) #add to the id the ordianal of the first letter in that string
        id_ += len(string) #add to the id the lenght of the string
        
        return id_

    #normalize both strings
    string1 = unidecode.unidecode(string1).lower().strip()
    string2 = unidecode.unidecode(string2).lower().strip()

    #create both 'words' dictionary's
    string1Words = sorted(string1.split(), key=sort_funct)
    string2Words = sorted(string2.split(), key=sort_funct)

    #calculate the max score and the score per letter
    max_score = (5*len(string1Words))
    score_per_letter = max_score/len("".join(string1Words))

    #init score as 0
    score = 0

    for word_index in range(len(string1Words)):
        try:

            if string2Words[word_index] == string1Words[word_index]:
                score += len(string2Words[word_index])*score_per_letter

            else: #if the word isnt 100% equal divide in letters and test it!
                #loop trough letters

                for letter_index in range(len(string1Words[word_index])):
                    #print(f'L: {string1Words[word_index][letter_index]}')

                    if string2Words[word_index][letter_index] == string1Words[word_index][letter_index]:
                        score += score_per_letter

                    else:
                        #add the penalty here for each letter
                        pass

        except:
            pass

    #calculate the similarity %% (probability)
    probability = (score/max_score) * 100

    return probability
