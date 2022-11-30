import nltk
from nltk.tokenize import word_tokenize
import string

# may have to add
# nltk.download("punkt")

if __name__ == "__main__":
    text_file = open("./aladdin.txt", "r")

    lines = [
        " ".join([line.strip().lower()]).translate(
            str.maketrans("", "", string.punctuation)
        )
        for line in text_file.readlines()
    ]

    tokens = [word_tokenize(token) for token in lines]
    print(tokens)

    text_file.close()
