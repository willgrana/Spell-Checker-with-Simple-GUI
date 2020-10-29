###Spell Checker with GUI integration
###CS-21 Final Project
###Will Grana


def main ():
    
    def LiveSpellChecker ():
        response= 'Y'
        dictopen= open ('wordlistLive.txt', 'r')    #Open dictionary of words
        dictionary= dictopen.read()                 #read words within dictionary
        
        print ('If you give me a word, I can check if it is spelled correctly.')    
        while response== 'Y':
            userin= input('Give me a word (lowercase characters):')   #Get word to check spelling
            word= userin + ' '
            if word in dictionary:                                  #Compare word to acceptible words in dictionary
                print (userin,'is spelled correctly.')
                response= input ('Would you like to try another word? (Y/N):')
            else:
                print (userin,'is not spelled correctly.')
                response= input ('Would you like to try another word? (Y/N):')
            while response != 'Y':
                if response != 'Y' and response != 'N':                 #Avoid unacceptable responses
                    response= input('Enter either "Y" for yes or "N" for no:')
                if response== 'N':
                    dictopen.close()        #close dictionary
                    print ('You can choose another function or you can quit using the designated buttons in the menu.')
                    break
                
            
            

    def txtSpellChecker ():
        import string
        var= 1
        response= 'Y'
        dictopen= open ('wordlist.txt', 'r')    #Open dictionary of words
        dictionary= dictopen.read()             #read words within dictionary
        print ('//////////////////////////Welcome to my spell checker!//////////////////////////')
        print ('Given a file in .txt format, I can check the spelling of the words in the file!.')
        while response== 'Y':
            userin= input('What is the name of the file?:')     #Get name of file to check
            try:
                fileopen= open (userin, 'r')                        #open file
            except FileNotFoundError:
                print ('That file name could not be located. Try again.')
                userin= input('What is the name of the file?:')
                fileopen= open (userin, 'r') 
            lines= fileopen.read()                              #read lines in file
            wordstring= lines.split()                           #split lines into words
            str1 = ' '.join(wordstring)                         #Get words into string
            table = str.maketrans({key: None for key in string.punctuation})   #Establish what punctuation to remove
            new_s = str1.translate(table)                                       #remove punctuation
            y= new_s.lower()          #make characters lowercase
            x= y.split()            #split string by word
            count = 0
            print ('Here are a list of words with spelling errors:')
            for word in x:                      #Compare words to accetable words in dictionary
                if word not in dictionary:
                    print (word)                #print misspelled words
                    count = count + 1
            if count > 1:
                print ('There were',count,'errors found.', sep= ' ')    #display number of mispelled words
                response= input('Would you like to check another text file? (Y/N):')   #ask for another run
            elif count == 0:
                print ('There were',count,'errors found.', sep= ' ')    #display number of mispelled words
                response= input('Would you like to check another text file? (Y/N):')   #ask for another run
            else:
                print ('There was',count,'error found.', sep= ' ')     #display number of mispelled words
                response= input('Would you like to check another text file? (Y/N):')    #ask for another run
            while response != 'Y':
                if response != 'Y' and response != 'N':                 #Avoid unacceptable responses
                    response= input('Enter either "Y" for yes or "N" for no:')
                if response== 'N':
                    dictopen.close()        #close dictionary
                    print ('You can choose another function or you can quit using the designated buttons in the menu.')
                    break
            fileopen.close ()    #close user's file
           
            
                
                
                
    def Quit ():
        import sys
        sys.exit ()  #exit program
            
                
    import tkinter
    
    root = tkinter.Tk()
    welcome= tkinter.Label(root, text="Welcome to my spell checker!")    #welcome label
    welcome2= tkinter.Label(root, text="I have a couple functions. I can check spelling of a text file or")    #instructions label
    welcome3=tkinter.Label(root, text="you can give me words on the go to check! Select from below.")
    buttontxt= tkinter.Button(root, text="Spell Checker For .txt Files", fg="red", command=txtSpellChecker)    #button for .txt spell checker
    buttonlive= tkinter.Button(root, text="Live Spell Checker", fg="green", command=LiveSpellChecker)      #button for live spell checker
    buttonquit= tkinter.Button(root, text="Quit", fg="blue", command=Quit)    #button to quit
    welcome.grid(row=0, column=1)    #window layout
    welcome3.grid(row=2, column=1)
    welcome2.grid(row=1, column=1)
    buttontxt.grid(row=3, column=0)
    buttonlive.grid(row=3, column=2)
    buttonquit.grid(row=3, column=1)
    tkinter.mainloop()     #enter main loop


main ()
