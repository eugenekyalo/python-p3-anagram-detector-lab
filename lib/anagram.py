class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        matches = []
        for possible_anagram in possible_anagrams:
            if self.is_anagram(possible_anagram):
                matches.append(possible_anagram)
        return matches

    def is_anagram(self, word):
        return sorted(word.lower()) == sorted(self.word)
