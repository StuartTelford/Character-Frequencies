# Set elements in list to 0. Method 1
# alpha = []
# alpha = [0 for i in range(97, 122)]
# print(alpha)

# Set elements in list to 0
alpha = []
for i in range(0, 126):  # Printable characters 32-126
    alpha.append(0)
# print(alpha)

source_txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet elit gravida, tempor tortor eget, tincidunt mauris. Nunc aliquet quam nec metus cursus lacinia. Cras tempus eget nibh et dictum. Donec at volutpat tortor, sit amet gravida risus. Pellentesque facilisis in quam at faucibus. In hac habitasse platea dictumst. Ut varius dapibus pretium. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur volutpat mi maximus, gravida purus at, maximus libero. Aenean a pharetra orci. Donec dignissim ante quis elit dapibus, eu elementum augue ullamcorper. Proin tempor enim eget nunc ultricies, eu sagittis quam iaculis. Nam commodo porta mi, non lobortis leo tincidunt sed. Nunc sit amet placerat justo, non porta justo. Maecenas ultrices, justo sed vulputate lacinia, lorem tellus lobortis felis, ut lobortis arcu nulla condimentum dolor. Proin cursus justo at ullamcorper ultrices.'
# source_txt = source_txt_original.lower()

# Loop through text checking each character is printable and keeping count.
for tst_char in range(len(source_txt)):
    alpha[ord(source_txt[tst_char])] += 1

# Print character counts
for i in range(32, 126):  # Printable characters
    print(chr(i) + " =", alpha[i])

print(sum(alpha), 'Characters in text')