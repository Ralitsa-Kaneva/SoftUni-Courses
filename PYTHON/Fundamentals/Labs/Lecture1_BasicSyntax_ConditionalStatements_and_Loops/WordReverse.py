word = input()
reverseWord = ""

for i in range(len(word)-1, -1, -1):
    reverseWord += word[i]

print(reverseWord)
