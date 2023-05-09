a = "John Doe"
age = 56
Religion = "Sikh"
Salary = 45000.56


# Approach 1 ---> using the % operator to print the data (Over here type is important)

print("Name: %s Age: %d Caste: %s Salary: %f" % (a,age,Religion,Salary))

# Approach 2 ----> using the {} braces (Over here the value is important)

print ("Name: {} Age: {} Caste: {} Salary: {}".format(a,age,Religion,Salary))

# Approach 3 ----> Using the {} braces with passing the Indexing values (Over here the value and the indexing is important)
# Indexing starts from the 0 value

print("Name: {0} Age: {1} Caste: {2} Salary: {3}".format(a,age,Religion,Salary))