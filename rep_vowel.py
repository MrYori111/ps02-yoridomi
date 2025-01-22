sentence = "Python is fun and python is easy to learn!"
sentence = sentence.replace("a", "A").replace("e", "E").replace("i", "I").replace("o", "O").replace("u", "U")
for letter in sentence: 
    print(letter, end="")