'''In Python, a list is a collection of ordered, mutable and heterogeneous elements,
separated by commas and enclosed in square brackets. Lists are dynamically-sized,
meaning that elements can be added or removed from the list at any time.
They are also zero-indexed, meaning that the first element has an index of 0,
the second element has an index of 1, and so on.'''

friends=['sathvi','pardhi','aravind','shyam','ranjith']
print(friends)

print(friends[0])  # i can access individual elements in a list using indexing.

friends[2]="pardhiva"
print(friends)

#remove(x): Removes the first occurrence of an element x from the list.
friends.remove("ranjith")
print(friends)

# pop([i]): Removes and returns the element at position i in the list.
# If i is not specified, it defaults to the last element.
friends.pop()
print(friends)

# append(x): Adds an element x to the end of the list.
friends.append("shyam")

# extend(iterable): Extends the list by appending all the elements from the iterable.
more_friends=['surya','venkat','thaheer']
friends.extend(more_friends)
print(friends)



# insert(i, x): Inserts an element x at position i in the list.
friends.insert(7,'jyothi')
print(friends)










