# normal for loop:

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for i in fruits :
    print (f"I like {fruits[0]} . {i}")

# for loop with enumerate() which returns the index and the item:

for index, fruit in enumerate(fruits, 1) :
    print(f"I like {index}. {fruit}")

# RANGE

question = int(input(f"what's the temperature now?: "))

def weatherAction (temperature) :
   
   print(f"I see, temperature is {temperature}")
    
   for i in range(temperature, -1, -1) :
        print(f"a storm is comming. Temperature has droped a point and is now {i}")

        if i > 25:
            print("it's hot, turning on fan")
        elif i >= 22:
            print("kinda hot, but no need to turn on the fan")
        elif i > 17 and i < 21 :
            print("good temp")
        elif i == 0 :
            print("too cold. stopped funcioning")
            break
        else :
            print("it's cold, turning on the heater")

weatherAction(question)

# RANGE to loop
print("Start of FOR loop:")
for i in range(3) :
    print(f"step {i}")

# RANGE and append to loop but only print a list of evens
evens = []
for i in range(1, 100):
    if i %2 != 0:
        continue
    if i %2 == 0 :
        evens.append(i) # if it's not an iterable, use append.
print(evens)

# range but printing each even one by one as it iterates:
for number in range(1, 10):
    if number % 2 == 0:
        continue
    print(number)    



# += (+= is used for iterables)
list_1 = [1,2,3]
list_2 = [4,5,6]
new_list = []

new_list += list_1
new_list += list_2
print(new_list)



# If, input and function

age = int(input("what's your age?: " ))

def ageFunction(age) :

    if age < 5 :
        print("free")
    elif age in range(5, 17) :
        print("child ticket")
    elif age in range(18, 64):
        print("adult ticket")
    else :
        print("senior discount")

ageFunction(age)

# MATCH - Python doesn't have SWITCH
def ageFunctionWithMatchBlock(age) :
   match(age):
        case a if a <5 :
            print("free")
        case b if b in range(5, 17) :
            print("child ticket")
        case c if c in range(5, 17) :
            print("child ticket")
        case _ :
            print("senior discount")   

ageFunctionWithMatchBlock(age)

# FLAGS!

password = str(input("input a password: "))

def passwordCheck(password) :
    special_chars = "£, !, @, #, +, -, ="
 
    if len(password) < 6 :
        print("weak, has to be > 6 characters")

    has_letter = False
    has_number = False
    has_special = False

    for char in password :
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_number = True
        if char in special_chars :
            has_special = True

    if not has_letter or not has_number :
        print("it has to contain letters AND numbers")
    elif not has_special :
        print("has to contain at least one special character")
    else :
        print("thanks, that's a safe password")

passwordCheck(password)

# Match

temp_answer = int(input("what's the temperature?: "))

def chooseClothes(temp_answer) :
    match(temp_answer):
        case a if a >=20 :
            print("T-shirt")
        case b if b >=14 :
            print("jacket")
        case c if c <=13:
            print("coat")
        case _:
            print("stay indoors")

chooseClothes(temp_answer)

# WHILE

counter = 0

while counter <3 :
    print(f"iteration number {counter}")
    counter +=1 # same as counter = counter +1
