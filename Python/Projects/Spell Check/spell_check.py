# Import the textblob library 
from textblob import TextBlob

t = 1
while t:

    # Input the incorrect word
    a = input("Enter the word to be checked: ")	 
    print("Original text: "+str(a))     

    b = TextBlob(a) 

    # Print the correct spelling of word
    print("Corrected text: "+str(b.correct()))
    print("Lemmatization: ")
    t = int(input("Try Again? 1 : 0 "))
