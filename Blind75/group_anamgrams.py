lst_words = ["listen", "silent", "hello", "world", "python", "typhon"]


# group anagrams together
dict_wrds = {}
for word in lst_words:
    word1 = ''.join(sorted(word))
    print(word1)

    if word1 in dict_wrds:
        dict_wrds[word1].append(word)
    
    else:
         dict_wrds[word1] = [word]
    
print(dict_wrds.values())