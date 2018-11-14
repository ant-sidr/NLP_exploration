class Sentence:
    """Содержит исходное предложение на естественном языке и
    позиции определённых частей речи для приведения в начальную форму"""

    def __init__(self, text):
        self.text = text
        self.nouns_pos = None
        self.verb_pos = None
        self.adj_pos = None
        self.pronoun_pos = None
        self.trash_pos = None
        self.find_speech_parts()

    def find_nouns(self):
        pass

    def find_verbs(self):
        pass

    def find_adjectives(self):
        pass

    def find_pronouns(self):
        pass

    def find_trash(self):
        pass

    def find_speech_parts(self):
        self.find_nouns()
        self.find_verbs()
        self.find_adjectives()
        self.find_pronouns()
        self.find_trash()


class ProcessedSentence(Sentence):
    """Содержит исходное предложение на естественном языке,
    позиции определённых частей речи и приводит их в начальную форму"""

    def __init__(self, text, settings):
        super().__init__(text)
        self.processed = self.text
        self.settings = settings
        self.to_initial()

    def nouns_to_initial(self):
        pass

    def verbs_to_initial(self):
        pass

    def adjectives_to_initial(self):
        pass

    def pronouns_to_initial(self):
        pass

    def trash_to_initial(self):
        pass

    def to_initial(self):
        self.nouns_to_initial()
        self.verbs_to_initial()
        self.adjectives_to_initial()
        self.pronouns_to_initial()
        self.trash_to_initial()
