ban_list = input().split(", ")
text = input()

for i in range(len(ban_list)):
    current_ban_word = ban_list[i]
    if current_ban_word in text:
        stars = "*" * len(current_ban_word)
        text = text.replace(current_ban_word, stars)

print(text)