#!/usr/bin/env python
from typing import List, Optional, Dict, Any
import collections


class Trie:
    def __init__(self) -> None:
        self.data: Dict[str, Any] = {}

    def insert(self, word: str) -> None:
        t = self.data
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t['-'] = True

    def search(self, word: str) -> bool:
        t = self.data
        for c in word:
            if c not in t: return False
            t = t[c]
        return '-' in t

    def startsWith(self, prefix: str) -> bool:
        t = self.data
        for c in prefix:
            if c not in t: return False
            t = t[c]
        return True


class TrieNode:
    # Initialize your data structure here.
    def __init__(self) -> None:
        self.children: Dict[str, 'TrieNode'] = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie3:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)  # type: ignore
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)  # type: ignore
            if current is None:
                return False
        return True


class Trie2:
    def __init__(self) -> None:
        self._children: List[Optional[Trie]] = [None] * 26
        self._a = ord('a')
        self._is_end = False

    def insert(self, word: str) -> None:
        if not word: return
        prev = self

        for char in word:
            idx = ord(char) - self._a
            if prev._children[idx] is None:
                prev._children[idx] = Trie()  # type: ignore
            prev = prev._children[idx]  # type: ignore

        prev._is_end = True

    def search(self, word: str) -> bool:
        if not word: return True  # ! correct?
        curr = self

        for char in word:
            idx = ord(char) - self._a
            curr = curr._children[idx]  # type: ignore
            if not curr: return False

        return curr._is_end

    def startsWith(self, prefix: str) -> bool:
        if not prefix: return True  # ! right ?
        curr = self

        for char in prefix:
            idx = ord(char) - self._a
            curr = curr._children[idx]  # type: ignore
            if not curr: return False

        return curr._is_end or any([not not x for x in curr._children])

    def __repr__(self) -> str:
        out = []
        for child in self._children:
            if child:
                out.append(str(child))
        return "|".join(out)


if __name__ == '__main__':
    # ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
    # [[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
    
    t = Trie()
    print(t)
    t.insert("app")
    t.insert("apple")
    t.insert("beer")
    t.insert("add")
    t.insert("jam")
    t.insert("rental")
    t.search("apps")
    t.search("app")

