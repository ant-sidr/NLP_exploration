import numpy as np

from utilities_nlp_pkg.word2vec_preprocessor import Word2VecPreprocessor


class OneHotEncoder:
    """Contains words dictionary, their number representations, and different methods"""

    def __init__(self, words, max_len=4, silent=True):
        """Fullfill object with words dictionary

        :param words: words set
        :param max_len: maximum n-grams length (from 2 to max_len)
        :param silent: flag, show unique words number
        """
        self.words = words
        self.word2int = Word2VecPreprocessor.get_word2int(words)
        self.ng_max_len = max_len
        self.ngram2int = Word2VecPreprocessor.get_ngram2int(words, max_len)
        self.dim = len(words)
        self.ng_dim = len(self.ngram2int)
        if not silent:
            print('Current words dictionary contains {} words'.format(self.dim))
            print('Current n-grams dictionary contains {} n-grams'.format(self.ng_dim))

    def one_hot(self, word):
        """Converts word into vector representation ([0...1...0])

        :param word: word to convert to one-hot
        :return: numpy array of one-hot encoded word
        :rtype: numpy.array
        """
        vector = np.zeros(self.dim)
        if word not in self.words:
            raise ValueError('Current word ({:s}) is not in dictionary'.format(word))
        position = self.word2int[word]
        vector[position] = 1
        return vector

    def ngram_one_hot(self, word):
        """Converts word into its n-grams vector representation ([0...1...0...1...0])

        :param word: word to convert its n-grams to semi-one-hot
        :return: numpy array of one-hot encoded word
        :rtype: numpy.array
        """
        vector = np.zeros(self.ng_dim)
        ngrams = Word2VecPreprocessor.get_ngrams(word, self.ng_max_len)
        for ng in set(ngrams):
            position = self.ngram2int[ng]
            vector[position] = 1
        return vector

    def split_to_x_y(self, df, x_label='word', y_label='context_word'):
        """Splits data frame of words and context words into X and Y sets

        :param df: words data frame
        :param x_label: column of words
        :param y_label: column of context words
        :return: arrays of one-hot vectors as X and Y
        :rtype: (numpy.array, numpy.array)
        """
        x_array = []
        y_array = []
        for x, y in zip(df[x_label], df[y_label]):
            x_array.append(self.one_hot(x))
            y_array.append(self.one_hot(y))
        x_array = np.asarray(x_array)
        y_array = np.asarray(y_array)

        return x_array, y_array

    def split_to_ngrams_vectors(self, df, x_label='word'):
        """Splits data frame of words into n-grams' semi-one-hots

        :param df: words data frame
        :param x_label: column of words
        :return: array of semi-one-hot vectors as X
        :rtype: numpy.array
        """
        x_array = [self.ngram_one_hot(x) for x in df[x_label]]
        return np.asarray(x_array)
