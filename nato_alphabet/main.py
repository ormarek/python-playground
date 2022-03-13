import pandas as pd

data = pd.read_csv("./nato_alphabet/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}
input = input("Word: ").upper()
nato_encoded = [phonetic_dict[letter] for letter in input]
print(nato_encoded)
