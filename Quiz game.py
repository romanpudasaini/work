print("Welcome to my quiz game")


playing= input("Do you want to play the game? ") 
if playing.lower() == "yes":
    print("let's start the game")
else:
    exit() 
score =0    
answer = input(" Q1) The term Computer is derived from……….? ") 
if answer.lower()== "latin":     
    print("Correct")
    score+=1
else:
    print("Incorrect")    
answer = input(" Q2) Who is the father of Computer science? ") 
if answer.lower()== "allen turing":     
    print("Correct")
    score+=1
else:
    print("Incorrect")  
answer = input(" Q3)  The first computers were programmed using? ") 
if answer.lower()== "machine language":     
    print("Correct")
    score+=1
else: 
    print("Incorrect")  
answer = input(" Q4) VGA is? ") 
if answer.lower()== "video graphics array":     
    print("Correct")
    score+=1
else:
    print("Incorrect")  
answer = input(" Q5)  How many heritage properties are listed in the World Heritage List? ") 
if answer== "10":     
    print("Correct")
    score+=1
else:
    print("Incorrect")  
answer = input(" Q6) Who was the first to use the word Jai Nepal? ") 
if answer.lower()== "shukraraj shastri":     
    print("Correct")
    score+=1
else:
    print("Incorrect") 
answer = input(" Q7) What percentage of the total land area of nepal is cultivatable? ") 
if answer == float(17.97):     
    print("correct")
    score+=1
else:
    print("Incorrect")
answer = input(" Q8) Who is the Zero Inventor? ") 
if answer.lower()== "arya bhatt":     
    print("Correct")
    score+=1
else:
    print("Incorrect")  
answer = input(" Q9) When is earthquake day celebrated in Nepal? ") 
if answer.lower()== "magh 2":     
    print("Correct")
    score+=1
else:
    print("Incorrect")
answer = input(" Q10) Which is the tallest temple in Nepal? ") 
if answer.lower()== "muktinath":     
    print("Correct")
    score+=1
else:
    print("Incorrect")
print("You have "+str(score)+" correct answer"
" You got "+str(score)+" points" ) 

