print("Game of Life!")
print("\n")

ans = input("Do you wish to use an Empty seed or a Line Seed? (e/l) ")
print("\n")
  
#I'm denoting alive cells with 1's and dead cells with 0's.
#I feel like using a binary choice was an obvious one for this game.

#The game specification does state that this is an infinite 2D-grid of cells, but I've only used a 5x5 array.
#This is due to several reasons. 
#One of them is that if you can proof an empty seed produces an empty universe with a small array it must work for one that is infinite.
#Another reason is that the Line seed will only have be 3 alive cells that go back and forth. 
#In fact, this seed is called an Oscillating seed due to this behaviour.
#The interesting thing is that I used a 5x5 array instead of a 3x3 that would conceptually also work.
#That is indeed true but my way of generating the evolutions required a slightly bigger array to work.
#This will be explained in a comment below.

if ans in ("E", "e"):
  Z = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
elif ans in ("L", "l"): 
  Z = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,1,1,1,0],
       [0,0,0,0,0],
       [0,0,0,0,0]]
else:
  print("Error! Reload Code!")

#As the function implies by its name, I'm trying to find the neighbours of every cell.
#Initially I generate an array called N that is defined by the size of my seed Z.
#My for statements allow me to check every cell in the array.
#I like to think of my array as a grid or matrix defined by (x, y) coordinates.
#My use of n-1 for my range limits is used due how index selection starts from the zero-th position.
#I deliberately formatted my code for my N[x][y] array to visually show how I'm collecting my neighbour values.
#Every time I find a neighbour I update my N array to count the number of neighbours for each cell.
#For example, for my Line seed I'll get values in N that will vary from 0 to 3 neighbours.
#This also explains why I'm using a 5x5 array instead of a 3x3 array. 
#I'm basically doing (n+2)x(n+2) arrays.
#The reason why is that I need an empty border for every edge of the seed.
#This is to allow my code to count the neighbours of the very extreme edges of my array. 
#If I did not have this extra padding my code would not be able to add the surrounding cells because they would simply not exist. 
#Meaning I need extra columns and rows of cells for all four edges of my array.

def neighbours(Z):
    N  = [[0,]*len(Z) for i in range(len(Z))]
    for x in range(1, len(Z)-1):
        for y in range(1, len(Z)-1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                    + Z[x-1][y]            +Z[x+1][y]   \
                    + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N

#My iteration function works in a similar way to my neighbour function.
#This is where I have told the program all the rules to allow the game of life to work.
#The rules revolve around two possible starting points, whether the cells are either alive or dead.
#When a cell is alive you have three rules to consider. As stated in the game specification.
#Z[x][y] array allows me to check the status of each cell and the inclusion of N[x][y] in the if statements allows me to check their corresponding neighbour counts.
#For the first if statement I'm either checking if there is over or underpopulation and if so the cell dies.
#The lovely thing about my first if statement is that it allows me to not need to write a rule for when there are 2 or 3 neighbours.
#This is because my code would just leave the cell alive if the first if statement did not produce any results.
#My second if statement checks if the cell is dead and has three neighbours and as you can see this produces a living cell.

def iterate(Z):
    N = neighbours(Z)
    for x in range(1, len(Z)-1):
        for y in range(1, len(Z)-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z

#My display function allows me to do two things. 
#Bring the super long Z array to a nicer looking matrix of numbers and to secondly reduce my 5x5 array to a more useful and efficient 3x3 array.

def display(Z):
    for j in Z[1:-1]:
        print(j[1:-1])

#This code simply shows the initial state all the way to the third evolution.
#I don't even bother to show any more because the empty seed would be forever dead so by the third evolution this becomes an obvious fact.
#And the Line seed becomes quickly obvious that it is an oscillating seed. Meaning it keeps repeating itself to infinity.
#If I just allowed the code to go to infinity I would just end up with an infinite output that would be both unreadable and would stall your IDE until someone forces the program to stop.
#The great thing about my code is that if another seed was to be checked it would require very little maintenance to show them using this code.

print("Initial state:")
display(Z)
iterate(Z)
print("\n")
print("First evolution:")
display(Z)
iterate(Z)
print("\n")
print("Second evolution:")
display(Z)
print("\n")
print("Third evolution:")
display(Z)