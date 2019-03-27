first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
rev = []
for i in range(1,len(last_name)+1):
    rev.append((last_name[len(last_name)-i]))
rev.append(" ")
for i in range(1,len(first_name)+1):
    rev.append((first_name[len(first_name)-i]))
print(''.join(rev))