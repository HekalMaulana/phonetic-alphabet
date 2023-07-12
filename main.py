import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word : ").upper()
output = [phonetic_alphabet[letter] for letter in word]
print(output)
