# Compulsory Task 1
'''
define the string
define update string
create for loop for length of index
if the unit in the index is even make it upper case
else make it lower
'''

string = "Hello World"
new_string = ""

# making each alternate letter upper vs lower case
for i in range(len(string)):
    if i % 2 != 0:
        new_string += string[i].upper()
    else:
        new_string += string[i].lower()

print(new_string)

# making each alternate word upper vs lower case
'''
create new variable which splits string
create new final string variable to be modified
create for loop 
make first word lower case
make second word upper case 
create a space
print final string 
'''
string = "Hello World"
words = string.split()
final_string = ""

for i in range(len(words)):
    if i == 0:
        final_string += words[i].lower()
    else:
        final_string += words[i].upper()

    if i != len(words) - 1: # adds a space between words after first condition is met
        final_string += " "

print(final_string)


