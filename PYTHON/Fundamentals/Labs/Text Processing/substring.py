key_string = input()
text = input()
new_text = ""

while key_string in text:
    text = text.replace(key_string, '')

print(text)
