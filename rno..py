import random
print('Welcome to the number guessing game')
number_to_guess= random.randint(1,10)
number_of_tries=1
guess=int(input('Please guess the number'))
while number_of_tries<=1:
      print("chance",number_of_tries,"\n")
      if number_to_guess==guess:
         print('Well done, you win!')
         print('You took', number_of_tries, 'goes to complete the game')
         print('Sorry! wrong number')
      elif guess<number_to_guess :
         print('your guess was lower than the number')  
      else:
         print('your guess was higher than the number')
      guess=int(input('please guess again'))
      number_of_tries +=1

if number_to_guess == guess:
    print('Well done, you win!')
    print('You took', number_of_tries, 'goes to complete the game')
else:
     print('sorry you lose')
     print('the number you needed to guess was', number_to_guess)
     print('Game over')
