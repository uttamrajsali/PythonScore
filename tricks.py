##########

a = []
for i in range(0,9):
  a.append(i)

print(len(a))

stri=""

a=stri.split()
print(a)

if len(a) > 0:
  print("bigger strng")
else:
  print("single world")

#test multi line string
my_string = "test \
mutli line \
string"

print(my_string)



############## Print a Key if value is 112

my_dict = {"Java": 100, "Python": 112, "C": 11}
value = 112
 
key_list = [key for key, val in my_dict.items() if val == value]
 
if len(key_list) > 0:
    print("The key for the value", value, "is", key_list[0])
else:
    print("Value not found in dictionary")
