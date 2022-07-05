name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

#The proper way to “mutate” a string is to use slicing and concatenation to build a new string by copying from parts of the old string.
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
name #'Zophie a cat'
newName #'Zophie the cat'