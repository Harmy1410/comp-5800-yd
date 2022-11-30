import string
import math
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


# may have to add
# nltk.download("punkt")
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download('omw-1.4')


def term_frequency(document: list[str]) -> dict[str, int]:
    x = {}

    for word in document:
        if word in x:
            x[word] += 1
            continue
        x[word] = 1

    return x


def inverse_doc_frequency(tf: dict[str, int]) -> dict[str, float]:
    x = {}

    for key, val in tf.items():
        x[key] = math.log(val)

    return x


def tf_idf(tf: dict[str, int], idf: dict[str, float]) -> dict[str, float]:
    x = {}

    for key in tf.keys():
        x[key] = tf[key] * idf[key]

    return x


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

    tf = term_frequency(tokens)
    idf = inverse_doc_frequency(tf)
    tfidf = tf_idf(tf, idf)
    print(tfidf)

    text_file.close()
