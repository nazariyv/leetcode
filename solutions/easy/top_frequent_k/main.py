#!/usr/bin/env python
from typing import Iterable, NamedTuple
from sortedcontainers import SortedDict

class WordFrequency(NamedTuple):
    word: str
    frequency: int

def smallest_word(word_a: str, word_b: str) -> int: return 0 if word_a < word_b else 1
def _sort_alphabetically(l: Iterable[WordFrequency]) -> Iterable[WordFrequency]:
    return sorted(l, key=lambda x: x[0])
def order_alphabetically(l: Iterable[WordFrequency]):
    wordFreq = WordFrequency(word="Vikysia", frequency="69")
    wordFreq.word
    wordFreq.frequency

    n = len(l)
    if n < 2: return l
    r = []
    curr_freq = l[0].frequency
    prev_ix = 0
    # each group that has the same count send to sort alphabetically
    for i in range(1, n):
        if l[i].frequency < curr_freq:
            r.extend(_sort_alphabetically(l[prev_ix:i]))
            curr_freq = l[i].frequency
            prev_ix = i
    r.extend(_sort_alphabetically(l[prev_ix:]))
    return r

def top_k_frequent(words: Iterable[str], k: int) -> Iterable[str]:
    frequency_list = []
    frequency_map = SortedDict()

    for word in words:
        frequency_map[word] = frequency_map.setdefault(word, 0) + 1
    for word, count in frequency_map.items():
        print(f"word:{word},count:{count}")
        frequency_list.append(WordFrequency(word=word, frequency=count))

    frequency_list = sorted(frequency_list, key=lambda x: x[1], reverse=True)
    frequency_list = order_alphabetically(frequency_list)
    return [x.word for x in frequency_list][:k]


if __name__ == '__main__':
    l = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    r = top_k_frequent(l, 4)
    print(r)
