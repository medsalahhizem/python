# 
def countdown(a):
  for i in range(a,-1,-1):
   print(i)
countdown(5)
# 
def  print_and_return(list):
  print(list[0])
  return list[1]

print_and_return([1,2])

# 
def First_Plus_Length(list):
  sum=0
  sum+=list[0]
  sum+=len(list)    
  return sum
  
s=First_Plus_Length([1,2,3,4,5])
print(s)

# 
def values_greater_than_second(list):
  ne=0
  l=[]
  for i in list :
    if i > list[1]:
      ne+=1
      l.append(i)
  if ne<2 :
    return False 
  else :
    print(ne)
    return l
l=values_greater_than_second([5,0,3,2,1,4])
print(l)
    
# 
def length_and_value(a, b):
    l = []
    for i in range(a):
        l.append(b)
    return l
  
length_and_value(6,2) 
