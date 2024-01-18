# A ∪ B - +sum

# A ∩ B  -  Intersection of sets

# A∖B, A−B  - difference

# A △ B, A -B -Symmetric difference

num_set = {1, 2, 3, 4, 5, 6}
string_set = {"Nicholas", "Michelle", "John", "Mercy"}
string_set2 = {"Nicfdholas", "Micfdhelle", "Johgdn", "Mdgercy"}

num_set1 = set([1, 2, 3, 4, 5, 6])
print("num_set1: %s" %(num_set1))

months = set(["Jan", "Feb", "March", "Apr", "May", "June", "July", "Aug", "Sep", "Oct", "Nov", "Dec"])
print("May" in months)

# A ∪ B
sum = string_set.union(string_set2)
print("sum: %s" %(sum))

# A ∩ B
x = {1, 2, 3}
y = {4, 3, 6}
print(x & y)

# A∖B, A−B 
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
diff_set = set_a.difference(set_b)
print(diff_set)

# A △ B, A -B
print(set_a ^ set_b)