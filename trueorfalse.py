x = True
y = False

def truthy(x,y):
    if x == y:
        print("False")
    elif x != y:
        print("True")
truthy(x,y)   
 
 #if glitch in code what to do?
x = 3454567
y = False
print(x)
def truthy(x,y):
   if type(x) == bool or type(y) == bool:
      print("Glitch!!!")
   else:
      if x == y:
         print("False")
      elif x != y:
         print("True")