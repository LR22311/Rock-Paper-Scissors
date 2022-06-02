from random import randint
player= input('paper(p),rock(r),scissor(s)')
chosen = randint(1,3)
#print(chosen)
if chosen == 1:
 computer = 'r'
elif chosen == 2:
 computer = 'p'
else: 
 computer = 's'
#this will convert the numbers yout get for the randint generater and convert it into r,p or s
print(player,"vs", computer)
if player == computer:
 print("tie")
elif player == 'r' and computer == 's':
 print('Player wins!!')
elif player == 'r' and computer == 'p':
  print('Computer Wins')
elif player == 'p' and computer == 'r':
 print('Player Wins')
elif player == 'p' and computer == 's':
 print('Computer wins')
elif player == 's' and computer == 'r':
 print('Computer Wins')
elif player == 's' and computer == 'p':
 print('Player Wins')