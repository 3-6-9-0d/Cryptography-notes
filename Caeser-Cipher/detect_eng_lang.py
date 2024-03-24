# we store the english words in a list (maybe a dictionary would be better)
ENGLISH_WORDS = []

# load the english words
def get_data():

    dictonary = open('eng.txt','r')

    # initialize the ENGLISH_WORDS list with the words present in the file
    # every word is in a distinct line so that why we have to split('\n')
    for word in dictonary.read().split('\n'):
        ENGLISH_WORDS.append(word)

    dictonary.close()

def count_words(text):

    #upper case letters are needed
    text = text.upper()
    #tranform the letters into a list of words(split by spaces)
    words = text.split(' ')
    #matches counts the number of english words in text
    matches = 0

    #consider all the words in the text and check whether the 
    #fgiven word is enlgish or not 

    for word in words:
        #Optimize the data structure !!
        if word in ENGLISH_WORDS:
            matches += 1

    return matches


#decides whether a given text is english or not
def is_text_english(text):
    #number of English words in a given
     matches = count_words(text)

     #define your algorithm
     #this case im assuming if 75% of the words in the text are
     #english words then it is an english text :)
     if(float(matches)/len(text.split(' ')))*100 >= 75:
         return True
     
     #else not an english text
     return False

if __name__ == '__main__':

        get_data()
        plain_text = 'My name Blazas Holcer form budapest, hungary.i am blah blah blah'
        print(is_text_english(plain_text))

