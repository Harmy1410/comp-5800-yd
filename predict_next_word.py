import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# may have to add
# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download('omw-1.4')

if __name__ == "__main__":
    text_file = open("./aladdin.txt", "r")

    # getting lines and removing whitespaces, newline and punctuations and converting to lower case
    lines = [
        " ".join([line.strip().lower()]).translate(
            str.maketrans("", "", string.punctuation)
        )
        for line in text_file.readlines()
    ]

    # tokenizing each line in lines
    token_lines = [word_tokenize(line) for line in lines if word_tokenize(line) != []]

    # removing stop words (a, and, the, etc...)
    stop_words = list(set(stopwords.words("english")))
    tokens = [word for token in token_lines for word in token if not word in stop_words]

    # stemming (eating -> eat)
    porter = PorterStemmer()
    tokens = [porter.stem(token) for token in tokens]

    print(tokens)

    text_file.close()
