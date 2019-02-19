import sys


class Redact:

    _file_to_redact = None
    _list_to_redact = []
    _replacement_char = '_'
    _replacement_length = 5
    _redacted_file_name = None
    _replacement_word = ""

    def __init__(self, file_name, redactions):
        self._file_to_redact = file_name
        self._list_to_redact = redactions
        self.create_replacement_word()
        self.create_replacement_file_name()

    def create_replacement_file_name(self):
        self._redacted_file_name = "redacted_" + str(self._file_to_redact)

    def create_replacement_word(self):
        replacement = ""
        for i in range(0, self._replacement_length):
            replacement += self._replacement_char
        self._replacement_word = replacement

    def replace_words(self):
        with open(self._file_to_redact, 'r') as read_file:
            with open(self._redacted_file_name, 'w') as write_file:
                contents = read_file.read()
                for word in self._list_to_redact:
                    contents = contents.replace(word, self._replacement_word)
                write_file.write(contents)


def main(argv):
    num_args = len(argv)
    if num_args < 1:
        print("File name must be provided")
        sys.exit(0)
    if num_args < 2:
        print("No words to be redacted")
        sys.exit(0)
    redactions = []
    for words in range(2, num_args):
        redactions.append(argv[words])
    redact_words = Redact(argv[1], redactions)
    redact_words.replace_words()


if __name__ == "__main__":
    main(sys.argv)
