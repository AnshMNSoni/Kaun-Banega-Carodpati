# kaun Banega Karodpati (KBC):

# Thanks for playing:

# Rules
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
print("Please Read the Rules and Information carefully")
print("\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
print(":: Rules and Information ::\n")
print("-> Total 7 Questions and 2 Lifelines")
print("-> To each Question their are 4 options")
print("-> Especially, In 6th and 7th question, for wrong answer $1000 and $2000 would deducted respectively\n")
print("-> To Take lifeline Press '*' in place of [Enter your option here: ]")
print(":: Lifeline-1 = (50/50) means out of 4 options 2 options filter out")
print(":: Lifeline-2 = (Hint) means Some Hint will given regarding correct answer\n")
print("-> You can use each lifeline for single time\n")
print("-> You can't use both lifeline in a single question\n")

print("-> Best of luck!\n")

import time

def lifeline_left(n):
    if (n == 0):
        print("\n=== Lifeline Available ===\n")
        print("Press -> 1 :: For 50/50")
        print("Press -> 2 :: For Hint\n")
        
    elif (n == 1):
        print("\n=== Lifeline Available ===\n")
        print("Press -> 1 :: For 50/50\n")
    
    else:
        print("\n=== Lifeline Available ===\n")
        print("Press -> 2 :: For Hint\n")
        
# Decison making + Give 5 seconds gap while changing questions:

def Decision(dollars):
    print("\n$ Sahi Jawab $")
    
    print("Inbox :: $", dollars, '\n')
    
    print("Next Question!")
    print("On your screen in", end = ' ')

    for i in range(5, 0, -1):
        time.sleep(1)
        print(i, end = ' ')
        
    print('\n')
    
amount = 0
Lifeline_1 = 0
Lifeline_2 = 0

print("Start in ::", end = ' ')
for i in range(25, 0, -1):
    time.sleep(1)
    print(i, end = ' ')
print('\n')

print("*************************************************************************\n")

for i in range(1, 8):
    
# 1 ::
    
    if (i == 1):
        print("# Question 1 of $1000 ->\n")
        
        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("What is the capital city of France?")
        print("a) Berlin")
        print("b) London")
        print("c) Paris")
        print("d) Madrid")    
            
        ans1 = input("\nEnter your option here: ")

        if (ans1 == 'c'):
            Decision(amount + 1000)
            amount = amount + 1000
        
        # Lifeline start:
        
        # Lifeline :: 1
        
        elif (ans1 == '*'):
            lifeline_left(0)
            
            Press = int(input("Enter here: "))
            
            if (Press == 1):
                Lifeline_1 = 1
                
                print("\nWhat is the capital city of France?")
                print("b) London")
                print("c) Paris")
                
                ans1 = input("\nEnter your option here: ")

                if (ans1 == 'c'):
                    Decision(amount + 1000)
                    amount = amount + 1000
                
                else:
                    print("\nx Galat Jawab x")
            
                    print("Won :: $0\n")
            
                    break
                
        # Lifeline :: 2
               
            else:
                Lifeline_2 = 1
                
                print("\nWhere is eiffel tower located?\n")
                
                ans1 = input("Enter your option here: ")

                if (ans1 == 'c'):
                    Decision(amount + 1000)
                    amount = amount + 1000
                
                else:
                    print("\nx Galat Jawab x")
            
                    print("Won :: $0\n")
            
                    break
                
        # Lifeline Over:
        
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $0\n")
            
            break
        
# 2 ::   
    
    elif (i == 2):
        print("# Question 2 of $2000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("Which planet is known as the 'Red Planet'?")
        print("a) Venus")
        print("b) Mars")
        print("c) Jupiter")
        print("d) Saturn")       
    
        ans2 = input("\nEnter your option here: ")
        
        if (ans2 == 'b'):
            Decision(amount + 2000)
            amount = amount + 2000
            
        # Lifeline start:
        
        elif (ans2 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWhich planet is known as the 'Red Planet'?")
                    print("a) Venus")
                    print("b) Mars")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'b'):
                        Decision(amount + 2000)
                        amount = amount + 2000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nIt is the fourth planet from the sun in our solar system!\n")
                
                    ans2 = input("Enter your option here: ")

                    if (ans2 == 'b'):
                        Decision(amount + 2000)
                        amount = amount + 2000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWhich planet is known as the 'Red Planet'?")
                    print("a) Venus")
                    print("b) Mars")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'b'):
                        Decision(amount + 2000)
                        amount = amount + 2000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nIt is the fourth planet from the sun in our solar system!")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'b'):
                        Decision(amount + 2000)
                        amount = amount + 2000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break
                
            
        # Lifeline Over:
            
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount, '\n')
            
            break
    
# 3 ::
      
    elif (i == 3):
        print("# Question 3 of $3000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("In which year did the Titanic sink?")
        print("a) 1905")
        print("b) 1912")
        print("c) 1920")
        print("d) 1931")       
    
        ans3 = input("\nEnter your option here: ")
        
        if (ans3 == 'b'):
            Decision(amount + 3000)
            amount = amount + 3000
            
        # Lifeline start:
        
        elif (ans3 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nIn which year did the Titanic sink?")
                    print("b) 1912")
                    print("d) 1931")
                
                    ans3 = input("\nEnter your option here: ")

                    if (ans3 == 'b'):
                        Decision(amount + 3000)
                        amount = amount + 3000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nRepublic Year of China!\n")
                
                    ans3 = input("Enter your option here: ")

                    if (ans3 == 'b'):
                        Decision(amount + 3000)
                        amount = amount + 3000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nIn which year did the Titanic sink?")
                    print("b) 1912")
                    print("d) 1931")
                
                    ans3 = input("\nEnter your option here: ")

                    if (ans3 == 'b'):
                        Decision(amount + 3000)
                        amount = amount + 3000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nRepublic Year of China!")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'b'):
                        Decision(amount + 3000)
                        amount = amount + 3000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break    
            
        # Lifeline Over:
        
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount, '\n')
            
            break
    
# 4 ::
    
    elif (i == 4):
        print("# Question 4 of $4000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("Who wrote the play 'Romeo and Juliet'?")
        print("a) William Wordsworth")
        print("b) Charles Dickens")
        print("c) William Shakespeare")
        print("d) Jane Austen")       
    
        ans4 = input("\nEnter your option here: ")
        
        if (ans4 == 'c'):
            Decision(amount + 4000)
            amount = amount + 4000
            
        # Lifeline start:
        
        elif (ans4 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWho wrote the play 'Romeo and Juliet'?")
                    print("c) William Shakespeare")
                    print("d) Jane Austen")
                
                    ans4 = input("\nEnter your option here: ")

                    if (ans4 == 'c'):
                        Decision(amount + 4000)
                        amount = amount + 4000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nOften referred as the 'Bard of Avon'")
                
                    ans4 = input("\nEnter your option here: ")

                    if (ans2 == 'c'):
                        Decision(amount + 4000)
                        amount = amount + 4000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWho wrote the play 'Romeo and Juliet'?")
                    print("c) William Shakespeare")
                    print("d) Jane Austen")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'c'):
                        Decision(amount + 4000)
                        amount = amount + 4000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nOften referred as the 'Bard of Avon'")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'c'):
                        Decision(amount + 4000)
                        amount = amount + 4000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break
                
            
        # Lifeline Over:
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount, '\n')
            
            break
    
# 5 ::
    
    elif (i == 5):
        print("# Question 5 of $5000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("Which element has the chemical symbol 'W'?")
        print("a) Tungsten")
        print("b) Vanedium")
        print("c) Rutherfodium")
        print("d) Antimony")       
    
        ans5 = input("\nEnter your option here: ")
        
        if (ans5 == 'a'):
            Decision(amount + 5000)
            amount = amount + 5000
            
        # Lifeline start:
        
        elif (ans5 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWhich element has the chemical symbol 'W'?")
                    print("a) Tungsten")
                    print("d) Antimony")
                
                    ans2 = input("\nEnter your option here: ")

                    if (ans2 == 'a'):
                        Decision(amount + 5000)
                        amount = amount + 5000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nThis element is known for its exceptional hardness and high melting point")
                
                    ans5 = input("\nEnter your option here: ")

                    if (ans5 == 'a'):
                        Decision(amount + 5000)
                        amount = amount + 5000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nWhich element has the chemical symbol 'W'?")
                    print("a) Tungsten")
                    print("d) Antimony")
                
                    ans5 = input("\nEnter your option here: ")

                    if (ans5 == 'a'):
                        Decision(amount + 5000)
                        amount = amount + 5000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nThis element is known for its exceptional hardness and high melting point")
                
                    ans5 = input("\nEnter your option here: ")

                    if (ans5 == 'a'):
                        Decision(amount + 5000)
                        amount = amount + 5000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break
                
            
        # Lifeline Over:
        
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount, '\n')
            
            break
    
# 6 ::
    
    elif (i == 6):
        print("# Question 6 of $6000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")
        
        print("Name of Raja Dashratha's Mother is?")
        print("a) Rupwati")
        print("b) Indumati")
        print("c) Sumitra")
        print("d) Kaushaliya")       
        print("\n=== Be aware from money Deduction ===")
        
        ans6 = input("\nEnter your option here: ")
        
        if (ans6 == 'b'):
            Decision(amount + 6000)
            amount = amount + 6000
        
        # Lifeline start:
        
        elif (ans6 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nName of Raja Dashratha's Mother is?")
                    print("a) Rupwati")
                    print("b) Indumati")
                
                    ans6 = input("\nEnter your option here: ")

                    if (ans6 == 'b'):
                        Decision(amount + 6000)
                        amount = amount + 6000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 1000, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nSanskrit word associated with purity and beauty")
                
                    ans6 = input("\nEnter your option here: ")

                    if (ans6 == 'b'):
                        Decision(amount + 6000)
                        amount = amount + 6000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 1000, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nName of Raja Dashratha's Mother is?")
                    print("a) Rupwati")
                    print("b) Indumati")
                
                    ans6 = input("\nEnter your option here: ")

                    if (ans6 == 'b'):
                        Decision(amount + 6000)
                        amount = amount + 6000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 1000, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nSanskrit word associated with purity and beauty")
                
                    ans6 = input("\nEnter your option here: ")

                    if (ans6 == 'b'):
                        Decision(amount + 6000)
                        amount = amount + 6000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 1000, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break
                
            
        # Lifeline Over:
        
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount - 1000, '\n')
            
            break
    
# 7 ::
    
    else:
        print("# Question 7 of $7000 ->\n")

        print("-> To Take lifeline Press '*' in place of [Enter your option here: ]\n")

        print("How many verses are their in 'Bhagavad Geeta?'")
        print("a) 520")
        print("b) 600")
        print("c) 910")
        print("d) 700")       
        print("\n=== Be aware from money Deduction ===")
        
        ans7 = input("\nEnter your option here: ")
        
        if (ans7 == 'd'):
            print("\n$ Sahi Jawab $")

            amount = amount + 7000
            print("Inbox :: $", amount, '\n')
            
        # Lifeline start:
        
        elif (ans7 == '*'):
            
            # Both lifeline available ::
            
            # lifeline-1
            
            if (Lifeline_1 == 0 and Lifeline_2 == 0):
                lifeline_left(0)
            
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nHow many verses are their in 'Bhagavad Geeta?'")
                    print("c) 910")
                    print("d) 700")
                
                    ans7 = input("\nEnter your option here: ")

                    if (ans7 == 'd'):
                        Decision(amount + 7000)
                        amount = amount + 7000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 2000, '\n')
            
                        break
                
            # Lifeline-2
               
                else:
                    Lifeline_2 = 1
                
                    print("\nIt is divisble by 100")
                
                    ans7 = input("\nEnter your option here: ")

                    if (ans7 == 'd'):
                        Decision(amount + 7000)
                        amount = amount + 7000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 2000, '\n')

                        break
                
            # lifeline 1 available ::
            
            # Lifeline-1 
            
            elif (Lifeline_1 == 0 and Lifeline_2 == 1):
                lifeline_left(1)
                
                Press = int(input("Enter here: "))
            
                if (Press == 1):
                    Lifeline_1 = 1
                
                    print("\nHow many verses are their in 'Bhagavad Geeta?'")
                    print("c) 910")
                    print("d) 700")
                
                    ans7 = input("\nEnter your option here: ")

                    if (ans7 == 'd'):
                        Decision(amount + 7000)
                        amount = amount + 7000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 2000, '\n')
                             
                        break
                
            # Lifeline-2
        
                else:
                    print("\n:: You Have already Used lifeline-2 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break

            # lifeline 2 available ::
            
            # lifeline-2
            
            elif (Lifeline_1 == 1 and Lifeline_2 == 0):
                lifeline_left(2)
                
                Press = int(input("Enter here: "))
            
                if (Press == 2):
                    Lifeline_2 = 1
                
                    print("\nIt is divisble by 100")
                
                    ans7 = input("\nEnter your option here: ")

                    if (ans7 == 'd'):
                        Decision(amount + 7000)
                        amount = amount + 7000
                
                    else:
                        print("\nx Galat Jawab x")
            
                        print("Won :: $", amount - 2000, '\n')
                             
                        break
                
            # Lifeline-1
        
                else:
                    print("\n:: You Have already Used lifeline-1 ::\n")
                    
                    print("Won :: $", amount, '\n')
                    
                    break
                
            
        # Lifeline Over:
        
        else:
            print("\nx Galat Jawab x")
            
            print("Won :: $", amount - 2000, '\n')
            
            break