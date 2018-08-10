
#first question
#############################
def fib(nterms):
    n1 = 0
    n2 = 1
    count = 0
    while count < nterms:
       print(n1,end=' , ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
    return

a = lambda nterms: fib(nterms)
print(a(6))

print('\n')
# #second question
# #############################


num = eval(input("enter a value: "))
print(type(num))

print('\n')

# # third question
# ##############################

Xnum = input("enter a number: ")
num = int(Xnum)
if num >= 0:
    while True:
        print("I Love You")
else:
    print("Dude!!!, you have entered a negative number")

print('\n')

# # fourth question
# ##############################

num=1
for i in range(2,22,2):
    num*=i
print(num)


print('\n')

# # fifth question
# ##############################

string = 'innovationwithpython'
x = slice(0,20,2)
print(string[x])

print('\n')

# # sixth question
# ##############################

my = []
for i in range(1,50):
    if i % (2 and 6) == 0:
        my.append(str(i))

y = list(map(int, my))
a = y[-3:]
print(a)
b =sum(a)
print(b)

print('\n')

# # seventh question
# ##############################
# #highest order function reduce to calculate e total sum of first 30 odd values of range 1 to 100

x = []
for i in range(1,61,2):
     x.append(str(i))

y = list(map(int, x))
b =sum(y)
print(b)

print('\n')

# # Eight question
# ##############################

new_list = [1,2,3,4,5,6,["Riyaz","UI","Haque",7],8,9,10]
print(new_list[-4])

# # twelfth  question
# ##############################

i=dict()
n = eval(input("enter a end value for a range:"))
for x in range(1,n):
    i[x]=x*x
print(i)

print('\n')

# # Fourteenth question
# ##############################

values = input("Input some comma seprated numbers : ")
x = values.split(",")
y = tuple(x)
print(x)
print(y)

print('\n')

# # fifteen question
# ##############################

x = input("enter any word of your choice: ")
print(x)
y = x[::-1]
print(y)

print('\n')

# # sixteen question
# ##############################
Xx = input("Enter first word of your choice:")
x =set(Xx)
Yy = input("Enter second word of your choice:")
y =set(Yy)

a = y.intersection(x)
print(a)

print('\n')

# # seventeen question
# ##############################

sen = input("enter a sentence of your choice:")
x = [len(x) for x in sen.split()]
print(x)

print('\n')

# # Eighteen question
# ##############################

dic1 = {1:'a', 2:'b'}
dic2 = {3:'c', 4:'d'}
dic3 = {5:'e', 6:'f'}

dic1.update(dic2)
x = dic1
x.update(dic3)
print(x)

print('\n')

# # Ninteen question
# ##############################

