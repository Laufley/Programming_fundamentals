##################################################################
# EXCEPT: does not stop execution
##################################################################

age_str = str(input("input your age: "))

try:
    age_str = int(age_str)
    print(f"your age is {age_str}.")
except ValueError:
    print("Error: name not valid. cannot contain numbers")
print("the program keeps running regardless of exception")


##################################################################
# RAISE: stops execution unless it's caught somewhere else (it's for critical issues)
##################################################################
numer_str = str(input("input your fav number: "))

try:
    numer_str = int(numer_str)
    print(f"your age is {numer_str}.")
except ValueError:
    raise ValueError("Error: name not valid. cannot contain numbers")
print("the program keeps running regardless of exception")