name = input('Hi, what is your Name? ')
print(f"Hello {name}! Let's play a game!")
max = 101; min = 0; guess = 50; count = 0
print("Think of random number from 1 to 100, and I'll try to guess it!")

while True:
    count += 1
    answer = input(f"Is it {str(guess)}? (yes/no): ")
    if answer == "no": 
        reply = input(f"Is the number larger than {str(guess)}? (yes/no): ")
        
        if reply == 'yes':  
            min = guess
            guess = (max + guess)//2 
        elif reply == 'no':
            max = guess
            guess = (min + guess)//2   
    elif answer == "yes":  
        print(f"Yeey! I got it in {str(count)} tries") 
        nextGame = input('Do you want to play more? ')
        if nextGame == 'yes':  
            count = 0; max = 100; min = 0; guess=50   
            print("Think of random number from 1 to 100, and I'll try to guess it!")
        else:
            print("Bye-Bye")
            break

