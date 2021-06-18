# Python3 program to count words
# in a given string
OUT = 0
IN = 1


# Returns number of words in string
def countWords(string):
    state = OUT
    wc = 0

    # Scan all characters one by one
    for i in range(len(string)):

        # If next character is a separator,
        # set the state as OUT
        if (string[i] == ' ' or string[i] == '\n' or
                string[i] == '\t'):
            state = OUT

        # If next character is not a word
        # separator and state is OUT, then
        # set the state as IN and increment
        # word count
        elif state == OUT:
            state = IN
            wc += 1

    # Return the number of words
    return wc

import pandas as pd
df = pd.read_csv("Tokenized3.csv")

#counts the words in a song and returns the word count as a row in dataset 
df['counted'] = df.apply(lambda row: countWords(row['lyrics']), axis=1)

df.to_csv('Tokenized3.csv')