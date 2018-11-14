from settings_nlp_pkg.common_nlp_settings import TRASH_SYMBOLS


class TextLoader:
    @staticmethod
    def remove_trash_symbols(line):
        """Удаляет из строки "мусор" - специальные и ненужные символы

        :param line: исходный текст
        :type line: str
        :return: текст без мусорных символов
        :rtype: [str]
        """
        for symbol in TRASH_SYMBOLS:
            line = line.replace(symbol, '')
        return line

    @staticmethod
    def load(path):
        """Загружает файл по указанному адресу, разбивает на предложения и возвращает список предложений

        :param path: путь к загружаемому файлу
        :type path: str
        :return: список, содержащий предложения, загруженные из указанного файла
        :rtype: [list]
        """
        if not isinstance(path, str):
            raise ValueError('Path must be a string with path to file')
        extension = path.split('.')[-1]
        if extension == 'txt':
            file = open(path, 'r', encoding='utf-8').read()  # todo: auto-check encoding
            lines = [TextLoader.remove_trash_symbols(l.strip()) for l in file.split('.')]
            lines = [l for l in lines if len(l) > 0]
            return lines
        elif extension == 'pdf':
            raise NotImplementedError('Under construction')
        elif extension in ['doc', 'docx']:
            raise NotImplementedError('Under construction')
        else:
            raise ValueError("Can't handle non pdf, txt, doc or docx file")
