lst = ["jainab", "farzana", "amit", "ram", "shayam"]
output = []
# for i,word in enumerate(lst):
#     new_word =""
#     for index, char in enumerate(word):
#         if index == i:
#             new_word += char.upper()
#         else:
#             new_word+=char
#     output.append(new_word)
print(output )
for i in range(len(lst)):
    new_word = ""
    word = lst[i]
    for j in range(len(word)):
        if i==j:
            new_word +=word[j].upper()
        else:
            new_word+=word[j]
    output.append(new_word)
print(output)
    