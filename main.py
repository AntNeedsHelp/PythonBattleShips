
import os
import random

#creating both boards
pBoard = [["  ", "\033[1;34;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
#i got the text formatting to change the color from ozzmaker.com
#https://ozzmaker.com/add-colour-to-text-in-python/#:~:text=To%20make%20some%20of%20your,right%20into%20the%20print%20statement.&text=32%20%3D%20Text%20colour%2C%2032%20for%20bright%20green.
cBoard = [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],[],[],[],[],[],[],[],[],[],[]]
sBoard = [["  ", "\033[1;31;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
dBoard1 = [["  ", "\033[1;34;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
dBoard2 = [["  ", "\033[1;31;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
for i in range(11):
  pBoard[i].append("\033[1;34;48m"+str(i-1)+"|\033[0;37;48m")
  dBoard1[i].append("\033[1;34;48m"+str(i-1)+"|\033[0;37;48m")
  cBoard[i].append(str(i-1)+"|")
  sBoard[i].append("\033[1;31;48m"+str(i-1)+"|\033[0;37;48m")
  dBoard2[i].append("\033[1;31;48m"+str(i-1)+"|\033[0;37;48m")
  for j in range(1,11):
    pBoard[i].append("-")
    dBoard1[i].append("-")
    cBoard[i].append("-")
    sBoard[i].append("-")
    dBoard2[i].append("-")

#making a function to display board
def drawBoard(board):
  for i in range(11):
    for j in range(11):
      print(board[i][j], end=" ")
      # I got the | end=" " | from tutorialspoint.com:
      # https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
    print("\n")


#making a procedure to set the coordinates of the player'ships
def setShip(length, board):
  print("\n")
  xCord = 11
  yCord = 11
  ship = input("Input the coordinate of where you want to put the top/left of your ship that is "+str(length)+ " spaces big: \n")
  if(len(ship) == 2):
    xCord = ord(ship[0].upper())-64 #changes the character inputed into a number so I can set the 
    #coordinate
    yCord = int(ship[1])+1

  #making sure the coordinates they inputed were valid
  while (xCord > 10 or xCord < 0) or (yCord > 10 or yCord < 0) or len(ship) != 2:
    ship = input("Invalid coordinate. Input the coordinate of where you want to put the top/left of your ship that is "+str(length)+ " spaces big: \n")
    if len(ship) == 2:
      xCord = ord(ship[0].upper())-64
      yCord = int(ship[1])+1

  direction = input("Would you like it to be horizontal or vertical (v or h)? ")
  while(direction != "v" and direction != "h"):
    direction = input("Not valid direction, would you like it to be horizontal or vertical (v or h)? \n")
  


  vPossible = True
  hPossible = True
  possible = False

  #checks if inputed coordinate will collide with another ship or will go off te board
  for i in range(length):
    if (yCord+i) > 10 or board[yCord+i][xCord] != "-":
      vPossible = False

  for i in range(length):
    if (xCord+i) > 10 or board[yCord][xCord+i] != "-":
      hPossible = False


  while(possible == False):
    if direction == "v" and (yCord+(length-1)) <= 10 and vPossible == True:
      possible = True
      for i in range(length):
        board[yCord][xCord] = str(length)
        yCord += 1
    elif direction == "h" and (xCord+(length-1)) <= 10  and hPossible == True:
      possible = True
      for i in range(length):
        board[yCord][xCord] = str(length)
        xCord += 1
    else:
      ship = input("Ship won't fit there. Please choose a coordinate: ")
      xCord = ord(ship[0].upper())-64
      yCord = int(ship[1])+1
      direction = input("Please choose a direction that will stay on the board (v or h): ")

      vPossible = True
      hPossible = True
      for i in range(length):
        if (yCord+i) > 10 or board[yCord+i][xCord] != "-":
          vPossible = False

      for i in range(length):
        if (xCord+i) > 10 or board[yCord][xCord+i] != "-":
          hPossible = False


#directions
print("Welcome to Battleships! ")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
#got "os.system("clear")" from Geeks for Geeks at:
#https://www.geeksforgeeks.org/clear-screen-python/#:~:text=How%20to%20clear%20screen%20in%20python%3F%201%20From,...%205%20Call%20the%20function%20we%20defined.%20
print("\nI am sure that you already know the rules, so I will only explain the basics of this program.")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThe blue board will show YOUR board, with where your ships are, which ones have been hit, and where the AI has shot ")
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nRed numbers on your board indicate that the oppenent has hit that coordinate ")
dBoard1[3][4] = "2"
dBoard1[3][5] = "\033[1;31;48m2\033[0;37;48m"
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA green '\033[1;32;48mo\033[0;37;48m' shows where your opponent has shot and missed ")
dBoard1[9][9] = "\033[1;32;48mo\033[0;37;48m"
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThe red board indicates the area where you will guess where your opponent's ships are ")
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA red '\033[1;31;48mx\033[0;37;48m' indicates that you have hit one of the opponent's ships at that coordinate ")
dBoard2[3][3] = "\033[1;31;48mx\033[0;37;48m"
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA green '\033[1;32;48mo\033[0;37;48m' indicates that you have shot that coordinate, but missed  ")
dBoard2[5][7] = "\033[1;32;48mo\033[0;37;48m"
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nTo input a coordinate, simply type the letter and then the number. Ex: e1")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThats about it for the rules. Have fun!")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")

drawBoard(pBoard)

setShip(2, pBoard)
os.system("clear") 
drawBoard(pBoard)

setShip(3, pBoard)
os.system("clear")
drawBoard(pBoard)

setShip(4, pBoard)
os.system("clear")
drawBoard(pBoard)

setShip(5, pBoard)
os.system("clear")
drawBoard(pBoard)

cont = input('\nPress "Enter" to begin playing: ')
os.system("clear")

# example of my procedure that uses iteration, sequencing, and selection
def setComputerShip(length, board):
  vPossible = False
  hPossible = False
  while(vPossible == False and hPossible == False):
    cordX = random.randint(1,10)
    cordY = random.randint(1,10)
    vPossible = True
    hPossible = True

    for i in range(length):
      if (cordY+i) > 10 or board[cordY+i][cordX] != "-":
        vPossible = False

    for i in range(length):
      if (cordX+i) > 10 or board[cordY][cordX+i] != "-":
        hPossible = False

  #randomly selects whether the ship is placed vertically or horizonatally
  if vPossible == True and hPossible == True:
    if random.randint(1,2) == 1:
      for i in range(length):
        board[cordY][cordX] = str(length)
        cordX += 1
    else: 
      for i in range(length):
        board[cordY][cordX] = str(length)
        cordY += 1

  elif vPossible == True and hPossible == False:
    for i in range(length):
        board[cordY][cordX] = str(length)
        cordY += 1
        
  elif vPossible == False and hPossible == True:
    for i in range(length):
        board[cordY][cordX] = str(length)
        cordX += 1


#calls to my procedure
setComputerShip(2, cBoard)
setComputerShip(3, cBoard)
setComputerShip(4, cBoard)
setComputerShip(5, cBoard)

won = False

num2 = 2
num3 = 3
num4 = 4
num5 = 5

nump2 = 2
nump3 = 3
nump4 = 4
nump5 = 5

possibleXHits = []
possibleYHits = []
shipsHit = []
toDelete = []

while won == False:
  shipHit = 0
  hit = False
  drawBoard(sBoard) #drawBoard function is an example of user output as it displays the grid
  xCord = 11
  yCord = 11
  #taking user input
  shotCord = input("What coordinate do you want to shoot at? ")
  if len(shotCord) == 2:
    xCord = ord(shotCord[0].upper())-64
    yCord = int(shotCord[1])+1

  while (xCord > 10 or xCord < 0) or (yCord > 10 or yCord < 0) or sBoard[yCord][xCord] != "-" or len(shotCord) != 2:
    shotCord = input("Invalid coordinate or you have already shot there. What coordinate do you want to shoot at? \n")
    if len(shotCord) == 2:
      xCord = ord(shotCord[0].upper())-64
      yCord = int(shotCord[1])+1

  os.system("clear")
  #checks if the coordinate inputed by the user hit the ship
  if cBoard[yCord][xCord] == "2":
    print("You hit my battleship of length 2!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m" 
    num2 -= 1
    if num2 == 0:
      "You sunk my battleship!"
  elif cBoard[yCord][xCord] == "3":
    print("You hit my battleship of length 3!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num3 -= 1
    if num3 == 0:
      print("\nYou sunk my battleship!")
  elif cBoard[yCord][xCord] == "4":
    print("You hit my battleship of length 4!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num4 -= 1
    if num4 == 0:
      print("You sunk my battleship!")
  elif cBoard[yCord][xCord] == "5":
    print("You hit my battleship of length 5!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num5 -= 1
    if num5 == 0:
      print("You sunk my battleship!")
  else:
    sBoard[yCord][xCord] = "\033[1;32;48mo\033[0;37;48m"
    print("You missed!")
  print("\n")
  drawBoard(sBoard)
  cTurn = input('Press "Enter" to continue! ')

  os.system("clear")
  if len(possibleXHits) == 0:
    xCord = random.randint(1,10)
    yCord = random.randint(1,10)

    while pBoard[yCord][xCord] == "\033[1;32;48mo\033[0;37;48m" or pBoard[yCord][xCord] == "\033[1;31;48m2\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m3\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m4\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m5\033[0;37;48m":
      xCord = random.randint(1,10)
      yCord = random.randint(1,10)
  else:
    randomChosen = random.randint(0, len(possibleXHits)-1)
    xCord = possibleXHits[randomChosen]
    yCord = possibleYHits[randomChosen]
    del possibleXHits[randomChosen] #i got the delete function from stackabuse.com
    #https://stackabuse.com/remove-element-from-an-array-in-python/
    del possibleYHits[randomChosen]
    del shipsHit[randomChosen]

  if pBoard[yCord][xCord] == "2":
    pBoard[yCord][xCord] = "\033[1;31;48m2\033[0;37;48m"
    nump2 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 2
  elif pBoard[yCord][xCord] == "3":
    pBoard[yCord][xCord] = "\033[1;31;48m3\033[0;37;48m"
    nump3 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 3
  elif pBoard[yCord][xCord] == "4":
    pBoard[yCord][xCord] = "\033[1;31;48m4\033[0;37;48m"
    nump4 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 4
  elif pBoard[yCord][xCord] == "5":
    pBoard[yCord][xCord] = "\033[1;31;48m5\033[0;37;48m"
    nump5 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 5
  else:
    pBoard[yCord][xCord] = "\033[1;32;48mo\033[0;37;48m"
    print("I shot at " + chr(xCord+64) + str(yCord-1)+ " and missed!")
  print("\n")
  drawBoard(pBoard)

  if hit == True:
    if xCord+1 <= 10 and (pBoard[yCord][xCord+1]== "-" or pBoard[yCord][xCord+1] == "2" or pBoard[yCord][xCord+1] == "3" or pBoard[yCord][xCord+1] == "4" or pBoard[yCord][xCord+1] == "5"):
      #adding elements to my lists. This helps the AI keep track of possible places where the rest of the ship could be
      possibleXHits.append(xCord+1)
      possibleYHits.append(yCord)
      shipsHit.append(shipHit)
    if xCord-1 >= 1 and (pBoard[yCord][xCord-1] == "-" or pBoard[yCord][xCord-1] == "2" or pBoard[yCord][xCord-1] == "3" or pBoard[yCord][xCord-1] == "4" or pBoard[yCord][xCord-1] == "5"):
      possibleXHits.append(xCord-1)
      possibleYHits.append(yCord)
      shipsHit.append(shipHit)
    if yCord+1 <= 10 and (pBoard[yCord+1][xCord] == "-" or pBoard[yCord+1][xCord] == "2" or pBoard[yCord+1][xCord] == "3" or pBoard[yCord+1][xCord] == "4" or pBoard[yCord+1][xCord] == "5"):
      possibleYHits.append(yCord+1)
      possibleXHits.append(xCord)
      shipsHit.append(shipHit)
    if yCord-1 >= 1 and (pBoard[yCord-1][xCord] == "-" or pBoard[yCord-1][xCord] == "2" or pBoard[yCord-1][xCord] == "3" or pBoard[yCord-1][xCord] == "4" or pBoard[yCord-1][xCord] == "5"):
      possibleYHits.append(yCord-1) #lists managing complexity
      possibleXHits.append(xCord)
      shipsHit.append(shipHit)

  if shipHit == 2 and nump2 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 2:
        toDelete.append(i) #list managing complexity
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]] #list data being used to clear other lists of useless cases
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 3 and nump3 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 3:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]]
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 4 and nump4 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 4:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]]
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 5 and nump5 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 5:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]] 
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()

  
  cTurn = input('Press "Enter" to continue! ')
  os.system("clear")
  #checks if someone won
  if num2 == 0 and num3 == 0 and num4 == 0 and num5 == 0:
    print("\n")
    print("\033[1;33;48m You Win!")
    won = True
    if nump2 == 0 and nump3 == 0 and nump4 == 0 and nump5 == 0:
      print("\n")
      print("\033[1;32;48m It's a draw!")
      won = True
  elif nump2 == 0 and nump3 == 0 and nump4 == 0 and nump5 == 0:
    print("\n")
    print("\033[1;32;48m You Lose!")
    won = True
  




import os
import random

#creating both boards
pBoard = [["  ", "\033[1;34;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
#i got the text formatting to change the color from ozzmaker.com
#https://ozzmaker.com/add-colour-to-text-in-python/#:~:text=To%20make%20some%20of%20your,right%20into%20the%20print%20statement.&text=32%20%3D%20Text%20colour%2C%2032%20for%20bright%20green.
cBoard = [["  ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],[],[],[],[],[],[],[],[],[],[]]
sBoard = [["  ", "\033[1;31;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
dBoard1 = [["  ", "\033[1;34;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
dBoard2 = [["  ", "\033[1;31;48mA", "B", "C", "D", "E", "F", "G", "H", "I", "J\033[0;37;48m"],[],[],[],[],[],[],[],[],[],[]]
for i in range(11):
  pBoard[i].append("\033[1;34;48m"+str(i-1)+"|\033[0;37;48m")
  dBoard1[i].append("\033[1;34;48m"+str(i-1)+"|\033[0;37;48m")
  cBoard[i].append(str(i-1)+"|")
  sBoard[i].append("\033[1;31;48m"+str(i-1)+"|\033[0;37;48m")
  dBoard2[i].append("\033[1;31;48m"+str(i-1)+"|\033[0;37;48m")
  for j in range(1,11):
    pBoard[i].append("-")
    dBoard1[i].append("-")
    cBoard[i].append("-")
    sBoard[i].append("-")
    dBoard2[i].append("-")

#making a function to display board
def drawBoard(board):
  for i in range(11):
    for j in range(11):
      print(board[i][j], end=" ")
      # I got the | end=" " | from tutorialspoint.com:
      # https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
    print("\n")


#making a procedure to set the coordinates of the player'ships
def setShip(length, board):
  print("\n")
  xCord = 11
  yCord = 11
  ship = input("Input the coordinate of where you want to put the top/left of your ship that is "+str(length)+ " spaces big: \n")
  if(len(ship) == 2):
    xCord = ord(ship[0].upper())-64 #changes the character inputed into a number so I can set the 
    #coordinate
    yCord = int(ship[1])+1

  #making sure the coordinates they inputed were valid
  while (xCord > 10 or xCord < 0) or (yCord > 10 or yCord < 0) or len(ship) != 2:
    ship = input("Invalid coordinate. Input the coordinate of where you want to put the top/left of your ship that is "+str(length)+ " spaces big: \n")
    if len(ship) == 2:
      xCord = ord(ship[0].upper())-64
      yCord = int(ship[1])+1

  direction = input("Would you like it to be horizontal or vertical (v or h)? ")
  while(direction != "v" and direction != "h"):
    direction = input("Not valid direction, would you like it to be horizontal or vertical (v or h)? \n")
  


  vPossible = True
  hPossible = True
  possible = False

  #checks if inputed coordinate will collide with another ship or will go off te board
  for i in range(length):
    if (yCord+i) > 10 or board[yCord+i][xCord] != "-":
      vPossible = False

  for i in range(length):
    if (xCord+i) > 10 or board[yCord][xCord+i] != "-":
      hPossible = False


  while(possible == False):
    if direction == "v" and (yCord+(length-1)) <= 10 and vPossible == True:
      possible = True
      for i in range(length):
        board[yCord][xCord] = str(length)
        yCord += 1
    elif direction == "h" and (xCord+(length-1)) <= 10  and hPossible == True:
      possible = True
      for i in range(length):
        board[yCord][xCord] = str(length)
        xCord += 1
    else:
      ship = input("Ship won't fit there. Please choose a coordinate: ")
      xCord = ord(ship[0].upper())-64
      yCord = int(ship[1])+1
      direction = input("Please choose a direction that will stay on the board (v or h): ")

      vPossible = True
      hPossible = True
      for i in range(length):
        if (yCord+i) > 10 or board[yCord+i][xCord] != "-":
          vPossible = False

      for i in range(length):
        if (xCord+i) > 10 or board[yCord][xCord+i] != "-":
          hPossible = False


#directions
print("Welcome to Battleships! ")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
#got "os.system("clear")" from Geeks for Geeks at:
#https://www.geeksforgeeks.org/clear-screen-python/#:~:text=How%20to%20clear%20screen%20in%20python%3F%201%20From,...%205%20Call%20the%20function%20we%20defined.%20
print("\nI am sure that you already know the rules, so I will only explain the basics of this program.")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThe blue board will show YOUR board, with where your ships are, which ones have been hit, and where the AI has shot ")
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nRed numbers on your board indicate that the oppenent has hit that coordinate ")
dBoard1[3][4] = "2"
dBoard1[3][5] = "\033[1;31;48m2\033[0;37;48m"
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA green '\033[1;32;48mo\033[0;37;48m' shows where your opponent has shot and missed ")
dBoard1[9][9] = "\033[1;32;48mo\033[0;37;48m"
drawBoard(dBoard1)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThe red board indicates the area where you will guess where your opponent's ships are ")
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA red '\033[1;31;48mx\033[0;37;48m' indicates that you have hit one of the opponent's ships at that coordinate ")
dBoard2[3][3] = "\033[1;31;48mx\033[0;37;48m"
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nA green '\033[1;32;48mo\033[0;37;48m' indicates that you have shot that coordinate, but missed  ")
dBoard2[5][7] = "\033[1;32;48mo\033[0;37;48m"
drawBoard(dBoard2)
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nTo input a coordinate, simply type the letter and then the number. Ex: e1")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")
print("\nThats about it for the rules. Have fun!")
cont = input('\nPress "Enter" to continue: ')
os.system("clear")

drawBoard(pBoard)

setShip(2, pBoard)
os.system("clear") 
drawBoard(pBoard)

setShip(3, pBoard)
os.system("clear")
drawBoard(pBoard)

setShip(4, pBoard)
os.system("clear")
drawBoard(pBoard)

setShip(5, pBoard)
os.system("clear")
drawBoard(pBoard)

cont = input('\nPress "Enter" to begin playing: ')
os.system("clear")

# example of my procedure that uses iteration, sequencing, and selection
def setComputerShip(length, board):
  vPossible = False
  hPossible = False
  while(vPossible == False and hPossible == False):
    cordX = random.randint(1,10)
    cordY = random.randint(1,10)
    vPossible = True
    hPossible = True

    for i in range(length):
      if (cordY+i) > 10 or board[cordY+i][cordX] != "-":
        vPossible = False

    for i in range(length):
      if (cordX+i) > 10 or board[cordY][cordX+i] != "-":
        hPossible = False

  #randomly selects whether the ship is placed vertically or horizonatally
  if vPossible == True and hPossible == True:
    if random.randint(1,2) == 1:
      for i in range(length):
        board[cordY][cordX] = str(length)
        cordX += 1
    else: 
      for i in range(length):
        board[cordY][cordX] = str(length)
        cordY += 1

  elif vPossible == True and hPossible == False:
    for i in range(length):
        board[cordY][cordX] = str(length)
        cordY += 1
        
  elif vPossible == False and hPossible == True:
    for i in range(length):
        board[cordY][cordX] = str(length)
        cordX += 1


#calls to my procedure
setComputerShip(2, cBoard)
setComputerShip(3, cBoard)
setComputerShip(4, cBoard)
setComputerShip(5, cBoard)

won = False

num2 = 2
num3 = 3
num4 = 4
num5 = 5

nump2 = 2
nump3 = 3
nump4 = 4
nump5 = 5

possibleXHits = []
possibleYHits = []
shipsHit = []
toDelete = []

while won == False:
  shipHit = 0
  hit = False
  drawBoard(sBoard) #drawBoard function is an example of user output as it displays the grid
  xCord = 11
  yCord = 11
  #taking user input
  shotCord = input("What coordinate do you want to shoot at? ")
  if len(shotCord) == 2:
    xCord = ord(shotCord[0].upper())-64
    yCord = int(shotCord[1])+1

  while (xCord > 10 or xCord < 0) or (yCord > 10 or yCord < 0) or sBoard[yCord][xCord] != "-" or len(shotCord) != 2:
    shotCord = input("Invalid coordinate or you have already shot there. What coordinate do you want to shoot at? \n")
    if len(shotCord) == 2:
      xCord = ord(shotCord[0].upper())-64
      yCord = int(shotCord[1])+1

  os.system("clear")
  #checks if the coordinate inputed by the user hit the ship
  if cBoard[yCord][xCord] == "2":
    print("You hit my battleship of length 2!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m" 
    num2 -= 1
    if num2 == 0:
      "You sunk my battleship!"
  elif cBoard[yCord][xCord] == "3":
    print("You hit my battleship of length 3!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num3 -= 1
    if num3 == 0:
      print("\nYou sunk my battleship!")
  elif cBoard[yCord][xCord] == "4":
    print("You hit my battleship of length 4!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num4 -= 1
    if num4 == 0:
      print("You sunk my battleship!")
  elif cBoard[yCord][xCord] == "5":
    print("You hit my battleship of length 5!")
    sBoard[yCord][xCord] = "\033[1;31;48mx\033[0;37;48m"
    num5 -= 1
    if num5 == 0:
      print("You sunk my battleship!")
  else:
    sBoard[yCord][xCord] = "\033[1;32;48mo\033[0;37;48m"
    print("You missed!")
  print("\n")
  drawBoard(sBoard)
  cTurn = input('Press "Enter" to continue! ')

  os.system("clear")
  if len(possibleXHits) == 0:
    xCord = random.randint(1,10)
    yCord = random.randint(1,10)

    while pBoard[yCord][xCord] == "\033[1;32;48mo\033[0;37;48m" or pBoard[yCord][xCord] == "\033[1;31;48m2\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m3\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m4\033[0;37;48m"  or pBoard[yCord][xCord] == "\033[1;31;48m5\033[0;37;48m":
      xCord = random.randint(1,10)
      yCord = random.randint(1,10)
  else:
    randomChosen = random.randint(0, len(possibleXHits)-1)
    xCord = possibleXHits[randomChosen]
    yCord = possibleYHits[randomChosen]
    del possibleXHits[randomChosen] #i got the delete function from stackabuse.com
    #https://stackabuse.com/remove-element-from-an-array-in-python/
    del possibleYHits[randomChosen]
    del shipsHit[randomChosen]

  if pBoard[yCord][xCord] == "2":
    pBoard[yCord][xCord] = "\033[1;31;48m2\033[0;37;48m"
    nump2 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 2
  elif pBoard[yCord][xCord] == "3":
    pBoard[yCord][xCord] = "\033[1;31;48m3\033[0;37;48m"
    nump3 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 3
  elif pBoard[yCord][xCord] == "4":
    pBoard[yCord][xCord] = "\033[1;31;48m4\033[0;37;48m"
    nump4 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 4
  elif pBoard[yCord][xCord] == "5":
    pBoard[yCord][xCord] = "\033[1;31;48m5\033[0;37;48m"
    nump5 -= 1
    print("I hit your battleship at "+ chr(xCord+64) + str(yCord-1)+"! ")
    hit = True
    shipHit = 5
  else:
    pBoard[yCord][xCord] = "\033[1;32;48mo\033[0;37;48m"
    print("I shot at " + chr(xCord+64) + str(yCord-1)+ " and missed!")
  print("\n")
  drawBoard(pBoard)

  if hit == True:
    if xCord+1 <= 10 and (pBoard[yCord][xCord+1]== "-" or pBoard[yCord][xCord+1] == "2" or pBoard[yCord][xCord+1] == "3" or pBoard[yCord][xCord+1] == "4" or pBoard[yCord][xCord+1] == "5"):
      #adding elements to my lists. This helps the AI keep track of possible places where the rest of the ship could be
      possibleXHits.append(xCord+1)
      possibleYHits.append(yCord)
      shipsHit.append(shipHit)
    if xCord-1 >= 1 and (pBoard[yCord][xCord-1] == "-" or pBoard[yCord][xCord-1] == "2" or pBoard[yCord][xCord-1] == "3" or pBoard[yCord][xCord-1] == "4" or pBoard[yCord][xCord-1] == "5"):
      possibleXHits.append(xCord-1)
      possibleYHits.append(yCord)
      shipsHit.append(shipHit)
    if yCord+1 <= 10 and (pBoard[yCord+1][xCord] == "-" or pBoard[yCord+1][xCord] == "2" or pBoard[yCord+1][xCord] == "3" or pBoard[yCord+1][xCord] == "4" or pBoard[yCord+1][xCord] == "5"):
      possibleYHits.append(yCord+1)
      possibleXHits.append(xCord)
      shipsHit.append(shipHit)
    if yCord-1 >= 1 and (pBoard[yCord-1][xCord] == "-" or pBoard[yCord-1][xCord] == "2" or pBoard[yCord-1][xCord] == "3" or pBoard[yCord-1][xCord] == "4" or pBoard[yCord-1][xCord] == "5"):
      possibleYHits.append(yCord-1) #lists managing complexity
      possibleXHits.append(xCord)
      shipsHit.append(shipHit)

  if shipHit == 2 and nump2 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 2:
        toDelete.append(i) #list managing complexity
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]] #list data being used to clear other lists of useless cases
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 3 and nump3 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 3:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]]
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 4 and nump4 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 4:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]]
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()
  elif shipHit == 5 and nump5 == 0:
    for i in range(0, len(shipsHit)):
      if shipsHit[i] == 5:
        toDelete.append(i)
    for i in range(0, len(toDelete)):
      toDelete[i] -= i
      del shipsHit[toDelete[i]] 
      del possibleXHits[toDelete[i]]
      del possibleYHits[toDelete[i]]
    toDelete.clear()

  
  cTurn = input('Press "Enter" to continue! ')
  os.system("clear")
  #checks if someone won
  if num2 == 0 and num3 == 0 and num4 == 0 and num5 == 0:
    print("\n")
    print("\033[1;33;48m You Win!")
    won = True
    if nump2 == 0 and nump3 == 0 and nump4 == 0 and nump5 == 0:
      print("\n")
      print("\033[1;32;48m It's a draw!")
      won = True
  elif nump2 == 0 and nump3 == 0 and nump4 == 0 and nump5 == 0:
    print("\n")
    print("\033[1;32;48m You Lose!")
    won = True
  




