f=open("day2.txt","r")
total=0
for line in f:
    temp=line.split("x")
    #split each line at the x
    l=int(temp[0])
    w=int(temp[1])
    h=int(temp[2])
    #calc area of each side
    s1=l*h
    s2=w*h
    s3=l*w
    #put in a list as easy to find min value but could use ifs instead
    sides=[s1,s2,s3]
    ss=min(sides)
    #calc wrap
    wrap=(2*l*w)+(2*w*h)+(2*h*l)+ss
    total+=wrap
print(total)
f.close()
f=open("day2.txt","r")
total=0
for line in f:
    temp=line.split("x")
    #split each line at the x
    l=int(temp[0])
    w=int(temp[1])
    h=int(temp[2])
    #calc peri of each side
    p1=2*l+2*h
    p2=2*w+2*h
    p3=2*l+2*w
    #put in a list as easy to find min value but could use ifs instead
    peris=[p1,p2,p3]
    sp=min(peris)
    #calc ribbon
    ribbon=sp+(l*w*h)
    total+=ribbon
print(total)
f.close()