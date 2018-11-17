import zipfile
from xml.etree.cElementTree import XML

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
    def __load_txt(path):
        """Загружает текстовые строки из файла txt"""
        file = open(path, 'r', encoding='utf-8').read()  # todo: auto-check encoding
        lines = [TextLoader.remove_trash_symbols(l.strip()) for l in file.split('.')]
        lines = [l for l in lines if len(l) > 0]
        return lines

    @staticmethod
    def __load_doc(path):
        """Документы в формате .doc и .docx разбираются как zip-архив, из него достаётся .xml файл с текстом
        Подробное описание метода:
        https://github.com/nmolivo/tesu_scraper/blob/master/Python_Blogs/01_extract_from_MSWord.ipynb
        """
        document = zipfile.ZipFile(path)
        source_filename = 'word/document.xml'
        if source_filename in document.namelist():
            xml_content = document.read(source_filename)
        else:
            raise FileNotFoundError('Cannot find {} inside selected file'.format(source_filename))
        document.close()

        # Warning The xml.etree.ElementTree module is not secure against maliciously constructed data.
        tree = XML(xml_content)

        word_namespace = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        para = word_namespace + 'p'
        text = word_namespace + 't'

        paragraphs = []
        for paragraph in tree.iter(para):
            texts = [node.text
                     for node in paragraph.getiterator(text)
                     if node.text]
            if texts:
                paragraphs.append(''.join(texts))

        lines = [TextLoader.remove_trash_symbols(l.strip()) for parag in paragraphs for l in parag.split('.')]
        lines = [l for l in lines if len(l) > 0]
        return lines

    @staticmethod
    def __load_pdf(path):
        raise NotImplementedError('Under construction')

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
            return TextLoader.__load_txt(path)
        elif extension == 'pdf':
            return TextLoader.__load_pdf(path)
        elif extension in ['doc', 'docx']:
            return TextLoader.__load_doc(path)
        else:
            raise ValueError("Can't handle non pdf, txt, doc or docx file")
