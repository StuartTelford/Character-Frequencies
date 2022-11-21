# ASCII Characters
# Populate list with values 32 to 127 for printable characters
lst = [i for i in range(32, 128)]
print(lst)

for i in lst:
    print(i, chr(i))

print('---')
# Print Number and Character
for i in range(32, 128):
	print(str(i) + ' ' + chr(i) + ' ,', end = '')


#print(chr(31))
#print('The ord: ', ord(a))