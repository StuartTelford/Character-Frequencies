# Count vowels in text
# 20221122

source_txt_original = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc sit amet elit gravida, tempor tortor eget, tincidunt mauris. Nunc aliquet quam nec metus cursus lacinia. Cras tempus eget nibh et dictum. Donec at volutpat tortor, sit amet gravida risus. Pellentesque facilisis in quam at faucibus. In hac habitasse platea dictumst. Ut varius dapibus pretium. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur volutpat mi maximus, gravida purus at, maximus libero. Aenean a pharetra orci. Donec dignissim ante quis elit dapibus, eu elementum augue ullamcorper. Proin tempor enim eget nunc ultricies, eu sagittis quam iaculis. Nam commodo porta mi, non lobortis leo tincidunt sed. Nunc sit amet placerat justo, non porta justo. Maecenas ultrices, justo sed vulputate lacinia, lorem tellus lobortis felis, ut lobortis arcu nulla condimentum dolor. Proin cursus justo at ullamcorper ultrices.'

source_txt = source_txt_original.lower()

# Set all variables = 0
a = e = i = o = u = 0
#a = b = c = d = e = f = g = h = i = j = k = l = m = n = o = p = q = r = s = t = u = v = w = x = y = z = 0

# Loop through text checking if each character is a vowel and keeping count.
for tst_char in range(len(source_txt)):
    if source_txt[tst_char] == 'a':
        a += 1
    elif source_txt[tst_char] == 'e':
        e += 1
    elif source_txt[tst_char] == 'i':
        i += 1
    elif source_txt[tst_char] == 'o':
        o += 1
    elif source_txt[tst_char] == 'u':
        u += 1

# Display Results
print('Source Text')
print(source_txt_original)
print('Length:',len(source_txt))
print('\nVowel Frequencies in Text')
print('a:',a,'e:', e, 'i:',i, 'o:',o, 'u:',u)