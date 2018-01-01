class Lexicon(object):

    def __init__(self):
        self.tags = [('direction', 'north'),
                     ('direction', 'south'),
                     ('direction', 'east'),
                     ('direction', 'west'),
                     ('verb', 'go'),
                     ('verb', 'stop'),
                     ('verb', 'kill'),
                     ('verb', 'eat'),
                     ('stop', 'the'),
                     ('stop', 'in'),
                     ('stop', 'of'),
                     ('noun', 'bear'),
                     ('noun', 'princess')]

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None

    def scan(self, command):
        words = command.split(' ')

        tag_list = []

        for word in words:
            found = False
            for tag in self.tags:
                if word.lower() == tag[1]:
                    tag_list.append(tag)
                    found = True

            if not found:
                number = self.convert_number(word)
                if number is not None:
                    tag_list.append(('number', number))
                else:
                    tag_list.append(('error', word))

        return tag_list

if __name__ == '__main__':
    lexicon = Lexicon()
    result = lexicon.scan('north')
    print result
