##################################################################
# LIST: Homogenous, mutable, []
##################################################################

language = ["Python", "JS", "Java"]
print(language[0])
print(language[-1])
language.append("Go")
print(language[-1])
language.remove("JS")
print(language)


##################################################################
# TUPLE Tuple: Heterogenous, immutable, ()
##################################################################

coordinates = (10.5, 20.1)
# coordinates.add(2) # this gives an error cause i can't mutate


##################################################################
# SET: # Mutable but no duplicates, {}
##################################################################

s = {1,2,3}
s.add(4)
s.add(2) # no error, but wont add a duplicate of 2
print(s)
s.remove(2)
s.add(2)
s.discard(10) # no error, but wont delete because a 10 does not exist
s.pop() # delete random element
print(s)
s.clear() # empties the set

# Additionally, sets are unnordered collections, which means we can use those operations (Union, Intersection, Dif, Simetric dif)
A= {1, 2, 3}
B= {3, 4, 5}

# UNION operation
print("2 unions: ")
print(A | B) #same
print(A.union(B)) #same

# INTERSECTION (common elements)
print( A & B ) 
print(A.intersection(B))

# Difference (elements that are in on the first colection but are not on the second colection)
print(A - B)
print(A.difference(B))

# Simetric difference (elements that both colections don't share)
print(A ^ B)
print(A.symmetric_difference(B))

##################################################################
# DICT: Colection. key-value, {}
##################################################################

student = {
    "name" : "Bob",
    "age" : 23,
    "course" : "IT"
}
print(student["name"])

# to iterate over a dict, we use .items()

for key, value in student.items() :
    print(f"{key.capitalize()} : {value}")