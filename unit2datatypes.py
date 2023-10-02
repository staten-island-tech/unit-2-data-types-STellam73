x = 3
y = float(3)
print(x,y)

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values: 
    print(i)

print(values[0])
print(values[6])

"test"
["t","e","s","t"]

x = "this is a thing"
y = x.split()
z = y[0]
print(y)
print(z)

x = input
x = input("Create a sentence.")
print("The sentince is" + x)

y = x.split( )
print(y)
z = len(y)
print(z)

day_of_week = input("what day is it? ")
if day_of_week == "Thursday":
    print("correct")
else:
    print("incorrect")



a = input("Determine if this number is odd or even") 
b = int(a)
print(type(b))
x = b % 2
if x == 0:
    print("even")
elif x > 0 :
    print("odd")
else:
    print("odd")

b = input("Bill Value?")
print(b)
service = input("Was the service bad,okay,good,or great?")
if service == "bad":
    print("0% tip")
elif service == "okay":
    print("15% tip")
elif service == "good":
    print("20% tip")
elif service == "great":
    print("25% tip")
else:
    ("no tip")


x = int(input("eneter a number to be factored"))
factors = []
for i in range(1, x+1):
    if x % i == 0:
        factors.append(i)
print(factors)


y = int(input("eneter a number to be factored"))
greatestcf = []
for i in range(1, y+1):
    if y % i == 0:
        greatestcf.append(i)
print(greatestcf)

#for example if ur factroign 10 and 12 the factors of 10 are 1 2 5 10 and if 12 the factors are 1 2 3 4 6 12 
# and if we assume 

if len(factors ) > len(greatestcf):
    z = len(factors)
else:
     z = len(greatestcf)
 
gcf = 5
for i in range(z):
    if factors[i] in greatestcf:
        gcf = factors[i]
print(gcf)