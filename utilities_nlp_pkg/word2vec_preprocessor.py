import pandas as pd

from settings_nlp_pkg.common_nlp_settings import STOP_WORDS, SUPPORTED_LANGUAGES, LANGUAGES_STRING


class Word2VecPreprocessor:
    """Contains methods to pre-process texts for using in NLP tasks"""

    @staticmethod
    def remove_stop_words(corpus, lang='ENG'):
        """Removes uninformative words from input corpus of text

        :param corpus: sentences list
        :param lang: input text language to use correct stop-words
        :return: updated corpus without stop-words in it
        :rtype: list
        """
        if lang not in SUPPORTED_LANGUAGES:
            raise ValueError('Chosen language is not supported. Try one of: {:s}'.format(LANGUAGES_STRING))
        stop_words = STOP_WORDS[lang]
        results = []
        for text in corpus:
            tmp = text.split(' ')
            for stop_word in stop_words:
                while True:  # Used to remove several includes on one sentence
                    if stop_word in tmp:
                        tmp.remove(stop_word)
                    else:
                        break
            results.append(" ".join(tmp))
        return results

    @staticmethod
    def get_unique_words(corpus):
        """Splits all available text to words and returns unique set of them

        :param corpus: sentences list
        :return: set of unique words
        :rtype: set
        """
        text = ' '.join(corpus)
        words = [x for x in text.split(' ')]
        return set(words)

    @staticmethod
    def get_word2int(words):
        """Converts words set into dictionary with words index

        :param words: set of unique words
        :return: words index
        :rtype: dict
        """
        # Word index generation
        word2int = {word: i for i, word in enumerate(words)}
        return word2int

    @staticmethod
    def get_ngrams(word, max_len=4):
        """Splits input word into its character n-grams

        :param word: input word to split
        :param max_len: maximum length of n-grams
        :return: list of ngrams
        :rtype: list
        """
        _min = 0
        _max = min(len(word), max_len)
        ngrams = []

        for i in range(2, _max+1):
            for j in range(0, len(word) - i + 1):
                ngrams.append(word[j:(j+i)])
        return ngrams

    @staticmethod
    def get_ngram2int(words, max_len=4):
        """Converts words into set of n-grams

        :param words: words set
        :param max_len: maximum n-grams length (from 2 to max_len)
        :return: n-grams dictionary
        :rtype: dict
        """
        ngrams = []
        for word in words:
            ngrams += Word2VecPreprocessor.get_ngrams(word, max_len)
        ngrams = set(ngrams)
        ngram2int = {ngram: i for i, ngram in enumerate(ngrams)}
        return ngram2int

    @staticmethod
    def get_words_and_context(corpus, window=2):
        """Converts text corpus into data frame with words and context

        :param corpus: list of sentences
        :param window: window size to lookup context
        :return: words and context data frame
        :rtype: pandas.DataFrame
        """
        sentences_vectors = [sen.split() for sen in corpus]

        data = []
        for sentence in sentences_vectors:
            for idx, word in enumerate(sentence):
                left = max(idx - window, 0)
                right = min(idx + window, len(sentence)) + 1
                for neighbour in sentence[left:right]:
                    if neighbour != word:
                        data.append([word, neighbour])

        result = pd.DataFrame(data, columns=['word', 'context_word'])
        return result
