lines = int(input())
word = input()
new_words_list = []
filtered_list =[]

for i in range(lines):
    new_word = input()
    new_words_list.append(new_word)
    filtered_list = new_words_list

print(f"{new_words_list}")

for i in range(len(new_words_list) - 1, -1, -1):

    if word not in filtered_list[i]:
        filtered_list.remove(filtered_list[i])

print(f"{filtered_list}")
