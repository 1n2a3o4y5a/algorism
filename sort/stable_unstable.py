# stable unstable sort

l1 = [(1, "a"), (5, "e"), (2, "c"), (4, "d"), (2, "b")]
l2 = [(1, "a"), (5, "e"), (2, "c"), (4, "d"), (2, "b")]

# stable
def func1(l): 
    l[1], l[2] = l[2], l[1]
    l[2], l[4] = l[4], l[2]
    print(l)
  
#unstable
def func2(l):
    l[1], l[4] = l[4], l[1]
    print(l)
    
func1(l1)
func2(l2)