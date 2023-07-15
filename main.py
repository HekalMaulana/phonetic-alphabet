import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(data)

phonetic_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    word = input("Enter a word : ").upper()
    try:
        output = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
