# Count character frequency in text from file
# 2022125

file_to_analyse = open('S:\Python\PyCharm Projects\Character-Frequencies\Text Files to Analyse\Declaration of Independence.txt', 'r')
# file_to_analyse = open('S:\Python\PyCharm Projects\Character-Frequencies\Text Files to Analyse\Lorum Ipsum.txt', 'r')
# file_to_analyse = open('S:\Python\PyCharm Projects\Character-Frequencies\Text Files to Analyse\Gettysburg Address.txt', 'r')
source_txt = (file_to_analyse.read())
file_to_analyse.close()

# Create list and set elements to 0
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