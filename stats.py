def count_words(text):
    print(f"Found {len(text.split())} total words")

def count_letters(text):
    letters_dict = {}
    text = text.lower()
    for letter in text:
        if letter.isalpha() and letter not in letters_dict:
            letters_dict[letter] = text.count(letter)
    return letters_dict

def sorted_letters(letters_dict):
    sorted_letters_dict = sorted(letters_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_letters_dict