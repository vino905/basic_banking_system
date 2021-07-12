def sq(*a):
    c=1
    print(type(a))
    for i in a:
        c=c*i

    print(c)    
sq(4,3,2,4)    
print(type(sq))