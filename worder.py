#coding:utf-8
import re
import codecs
import string
import importlib


def get_occurences(alphabet):
    uniques = set(alphabet)
    occurences = {}
    for unique in uniques:
        occurences[unique] = len(re.findall(unique, alphabet))
    return occurences


def get_limited(alphabet, words):
    occurences = get_occurences(alphabet)
    banned = []
    for word in words:
        for char, occurence in occurences.items():
            if len(re.findall(char, word)) > occurence:
                banned.append(word)
    return words - set(banned)


if __name__ == '__main__':
    alphabet = raw_input('Enter letters: ').decode('utf-8')
    language = raw_input('Enter language:') or 'en'
    regex = raw_input('Enter regex (optional):')
    settings = importlib.import_module('settings.settings_%s' % language)
    regex_set = ''.join(filter(lambda x: x in string.lowercase, regex))
    alphabet += regex_set
    matcher = re.compile('[' + alphabet + ']{2,}$', re.I).match
    words = set(word.replace('\n', '')
                for word in codecs.open('data/%s.txt' % language, 'r', 'utf-8')
                if matcher(word))
    calculated = []
    for word in get_limited(alphabet, words):
        if re.match(r'%s' % regex, word):
            calculated.append(
                (word, sum([settings.CHAR_POINTS[char] for char in word])))

    for word in sorted(calculated, key=lambda x: x[1], reverse=True):
        print word[0], ' - ', word[1]
