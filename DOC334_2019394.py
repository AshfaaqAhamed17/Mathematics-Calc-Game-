import random       #randomly imports integers needed for the game
import operator     #randomly imports operators needed for the game
import time         #randomly imports time

opt = 0
res = []    #list created to store the summary results
g = 0
u = 0
e = 0
m = 0
h = 0

#global variables used inside user defined functions
def games():
    global g    
    g+=1
    
def quick_games():
    global u 
    u+=1

def easy_games():
    global e
    e+=1

def medium_games():
    global m
    m+=1

def hard_games():
    global h
    h+=1

#user defined functions
def start():
    print("---------------MATHS GAME---------------\n")

    
def game_menu():
    print('1. Quick game')
    print('2. Custom game')
    print('3. Display past game details')
    print('4. Exit')
    print('\n')
    opt = input('ENTER YOUR OPTION ( 1 | 2 | 3 | 4 ): ')

      
    End = 0
    
    while End != 'q':   #while loop to ensure the code doesn't crash unless it is said to end the program
        
        try:            #try block to ensure the code doesn't crash when an invalid input is given
        
            if opt == '1':
                count = 0
                cor = 0
                sym="%"
                q_name = input('Enter your name : ')
                
                
                for i in range(1,6):
                    num1 = random.randrange(0,11)   # start from 0. end at 10
                    num2 = random.randrange(0,11)
                        
                    que1 = str(num1)+ ' + ' +str(num2)
                    ans1 = num1 + num2
                    print(que1, end='')
                    result = int(input(" = "))
                    count+=1
                        
                    if result == ans1:
                        print('Answer is correct')
                        cor+=1
                    else:
                        print('Answer is incorrect. The correct answer is : ', ans1)
                    print('')
                print('****GAME RESULTS****','\n')
                print('Your name is ', q_name)
                print('You got', cor, 'questions correct out of', count)
                p = (cor/count)*100
                perc = round(p,2)       #rounding off to 2 decimal places
                print('Your marks :',perc,'%\n')                    

                games()
                quick_games()
                res.append((q_name,perc,sym,cor,count))     #adding data into the list
                End=input('If you want to end this press "q", else press ENTER : ')
                if End == 'q':
                    print('\n---GAME OVER. THANKS FOR PLAYING.---\n')
                            
                else:
                    print('')
                    start()
                    game_menu()
                
            elif opt == '2':

                q_name = input('Enter your name : ')
                print("")
                print('a) Easy  b) Medium  c) Hard')
                diff = input("ENTER DIFFICULTY LEVEL : ")
                    
                if diff == 'a':
                    count=0
                    cor=0
                    sym = "%"
                    print("**You selected Easy mode**")
                    q_no = int(input('How many questions do you want to do : '))
                    print('\n')
                    for i in range(q_no):
                        num1 = random.randrange(0,11)   # start from 0. end at 10
                        num2 = random.randrange(0,11)

                        que1 = str(num1)+ ' + ' +str(num2)
                        ans1 = num1 + num2
                        print(que1, end='')
                        result = int(input(" = "))
                        count+=1

                        if result == ans1:
                            print('Answer is correct')
                            cor+=1
                        else:
                            print('Answer is incorrect. The correct answer is : ', ans1)
                    print('\n','****GAME RESULTS****','\n')
                    print('Your name is ', q_name)
                    print('You have seleced EASY mode')
                    print('You got', cor, 'questions correct out of', count)

                    p = (cor/count)*100
                    perc = round(p,2)       #rounding off to 2 decimal places
                    print('Your marks :',perc,'%\n')
                    
                    games()
                    easy_games()
                    res.append((q_name,perc,sym,cor,count))     #adding data into the list
                    End=input('If you want to end this press "q", else press ENTER : ')
                    if End == 'q':
                        print('\n---GAME OVER. THANKS FOR PLAYING.---\n')
                                
                    else:
                        print('')
                        start()
                        game_menu()
                    
                        
                elif diff == 'b':
                    count=0
                    cor=0
                    sym = "%"
                    print("**You selected Medium mode**")
                    q_no = int(input('How many questions do you want to do : '))
                    print('\n')
                    for i in range(q_no):
                        num1 = random.randrange(0,51)   # start from 0. end at 50
                        num2 = random.randrange(0,51)
                        oper = random.choice(r"+-")     # r is used to make it raw string. it seperates the data which is inside the string
                        # This is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character.
                            
                        que1 = str(num1)+ oper + str(num2)
                        ans1 = eval(str(num1)+ oper + str(num2))
                        print(que1, end='')
                        result = int(input(" = "))
                        count+=1
                        
                        if result == ans1:
                            print('Answer is correct')
                            cor+=1
                        else:
                            print('Answer is incorrect. The correct answer is : ', ans1)
                    print('\n','****GAME RESULTS****','\n')
                    print('Your name is ', q_name)
                    print('You have played the MEDIUM mode')
                    print('You got', cor, 'questions correct out of', count)
                    p = (cor/count)*100
                    perc = round(p,2)       #rounding off to 2 decimal places
                    print('Your marks :',perc,'%\n')

                    games()
                    medium_games()
                    res.append((q_name,perc,sym,cor,count))     #adding data into the list
                    End=input('If you want to end this press "q", else press ENTER : ')
                    if End == 'q':
                        print('\n---GAME OVER. THANKS FOR PLAYING.---\n')
                                
                    else:
                        print('')
                        start()
                        game_menu()           

                elif diff == 'c':
                    sym = "%"
                    count=0
                    cor=0
                    print("**You selected Hard mode**")
                    q_no = int(input('How many questions do you want to do : '))
                    print('\n')
                    for i in range(q_no):
                        num1 = random.randrange(0,101)  # start from 0. end at 100
                        num2 = random.randrange(0,101)
                        oper = random.choice(r"+-*")    # r is used to make it raw string. it seperates the data which is inside the string.
                        # This is useful when we want to have a string that contains backslash and don't want it to be treated as an escape character.

                        que1 = str(num1)+ oper + str(num2)
                        ans1 = eval(str(num1)+ oper + str(num2))
                        
                        print(que1, end='')
                        result = int(input(" = "))
                        count+=1
                            
                        if result == ans1:
                            print('Answer is correct')
                            cor+=1
                        else:
                            print('Answer is incorrect. The correct answer is : ', ans1)
                    print('\n','****GAME RESULTS****','\n')
                    print('Your name is ', q_name)
                    print('You have played the HARD mode')
                    print('You got', cor, 'questions correct out of', count)
                    p = (cor/count)*100
                    perc = round(p,2)       #rounding off to 2 decimal places
                    print('Your marks :',perc,'%\n')

                    games()
                    hard_games()
                    res.append((q_name,perc,sym,cor,count))     #adding data into the list
                    End=input('If you want to end this press "q", else press ENTER : ')
                    if End == 'q':
                        print('\n---GAME OVER. THANKS FOR PLAYING.---\n')
                            
                    else:
                        print('')
                        start()
                        game_menu()                    
                else:
                    print('\n','**Invalid  option**','\n')
                    game_menu()
                

            elif opt == '3':
                print('\n','                      ****GAME SUMMARY****','\n \n')
                print('NAME                  PERCENTAGE    CORRECT    No. OF QUESTIONS')
                print('---------------------------------------------------------------')
                for n,a,s,c,q in res:   #gets the data which has been stored in the list
                    print(n,' '*(22-len(n)),a,s,' '*(11-len(str(a))),c,' '*(11-len(str(c))),q)   #prints the data stored in the list
                print('\n \n')
                time.sleep(2)   #pauses for 2 seconds
                print('Total number of GAMES played -> ', g,'\n')
                time.sleep(1)
                
                print('\t * QUICK GAMES played -> ', u)
                time.sleep(1)
                print('\t * CUSTOM EASY GAMES played -> ', e)
                time.sleep(1)
                print('\t * CUSTOM MEDIUM GAMES played -> ', m)
                time.sleep(1)
                print('\t * CUSTOM HARD GAMES played -> ', h)


                print('\n')
                End=input('If you want to end this press "q", else press ENTER : ')
                if End == 'q':
                    print('\n','---GAME OVER. THANKS FOR PLAYING.---','\n')
                        
                else:
                    print('')
                    start()
                    game_menu() 
                        
                
            elif opt == '4':
                print('You have exited the game. Thank you!')
            
            else:
                print('\n','**Invalid option**','\n')
                game_menu()
                
        
        except ValueError:      #when an invalid term other than the required term is entered, the code doesn't crash
            print('\n',"Integer required. Please paly again",'\n')
            game_menu()
        break
        
        
start()
game_menu()
