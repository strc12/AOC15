f=open("day3.txt","r")
grid=[[0,0]]
santapos=[0,0]
for line in f:
    
    #examine each instruction in turn
    for inst in line:
        mover = santapos
        if inst=="^":
            mover=[mover[0],mover[1]+1]
        elif inst=="v":
            mover=[mover[0],mover[1]-1]
        elif inst=="<":
            mover=[mover[0]-1,mover[1]]
        elif inst==">":
            mover=[mover[0]+1,mover[1]]
        #print(mover)
        
        if mover not in grid:
            grid.append(mover)
        santapos=mover
print(len(grid))
