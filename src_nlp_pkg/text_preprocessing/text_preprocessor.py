from src_nlp_pkg.structures.sentence import ProcessedSentence
from utilities_nlp_pkg.word2vec_preprocessor import Word2VecPreprocessor


class TextPreprocessor:
    """Переводит текст в нижний регистр, приводит слова к начальной форме
     и обрабатывает мусор (TO BE IMPLEMENTED), удаляет стоп-слова
     """
    def __init__(self):
        raise NotImplementedError('Under construction')

    @staticmethod
    def to_lower(text, use_dict=False):
        """Переводит входной текст в нижний регистр. Поддерживает работу со спец.словами

        :param text: исходный текст
        :param use_dict: флаг, использовать словарь спец.слов
        :return: текст в нижнем регистре
        :rtype: [str]
        """
        if use_dict:
            raise NotImplementedError('Under construction')  # TODO: implement
        else:
            res = [x.lower() for x in text]
        return res

    @staticmethod
    def to_initial(text, settings=None):
        """Переводит слова в тексте в их начальную форму

        :param text: исходный текст (в нижнем регистре)
        :param settings: настройки приведения слов в начальную форму
        :return: текст со словами в начальной форме
        :rtype: [str]
        """
        sentences = [ProcessedSentence(x, settings).processed for x in text]
        return sentences

    @staticmethod
    def remove_stop_words(text, lang='RUS'):
        """Удаляет из предложений неинформативные слова (в отдельных настройках)

        :param text: исходный текст (в начальной форме)
        :param lang: язык, на котором написан текст
        :return: текст, готовый к дальнейшей обработке
        :rtype: [str]
        """
        return Word2VecPreprocessor.remove_stop_words(text, lang)
