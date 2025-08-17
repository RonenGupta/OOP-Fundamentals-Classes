words = ["hello", "world", "!"]
sentence = ""
for word in words:
    sentence += word + " "

print(sentence.strip())

# optimised

words = ["hello", "world", "!"]
sentence = " ".join(words)
print(sentence.strip())