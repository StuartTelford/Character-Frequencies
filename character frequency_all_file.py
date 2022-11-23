# Count character frequency in text from file

f = open('S:\Python\PyCharm Projects\Character-Frequencies\Declaration of Independence.txt', 'r')
# f = open('S:\Python\PyCharm Projects\Character-Frequencies\Ipsum.txt', 'r')
source_txt = (f.read())

# Set elements in list to 0
alpha = []
for i in range(0, 126):  # Printable characters 32-126
    alpha.append(0)

# Loop through text checking each character is printable and keeping count.
for tst_char in range(len(source_txt)):
    alpha[ord(source_txt[tst_char])] += 1
    # print(source_txt[tst_char], end = '')  # Print current character

# Print character counts
for i in range(32, 126):  # Printable characters
    print(chr(i) + " =", alpha[i])

print(sum(alpha), 'Characters in text')