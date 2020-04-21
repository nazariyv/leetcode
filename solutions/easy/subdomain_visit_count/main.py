#!/usr/bin/env python
from solutions.minions import TestCase as T, TestRunner as TR, iterable_comparator as comparator
from collections import defaultdict
from typing import List


def main_faster(cpdomains: List[str]) -> List[str]:
    domain_visits = defaultdict(int)

    for domain in cpdomains:
        n = len(domain)
        whitespace_ix = 0
        subdomains = []
        for i in range(n - 1, -1, -1):
            char = domain[i]
            if char == " ":
                subdomains.append(domain[i + 1:n])
                whitespace_ix = i
            elif char == ".":
                subdomains.append(domain[i + 1:n])

        count = int(domain[0:whitespace_ix])

        for subdomain in subdomains:
            domain_visits[subdomain] += count

    result = []
    for domain, visits in domain_visits.items():
        result.append(f"{visits} {domain}")

    return result


# Example 2:
# Input: 
# ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output: 
# ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
# Explanation: 
# We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5 times.
# For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times, and
# "org" 5 times.
def main(cpdomains: List[str]) -> List[str]:
    domain_visits = defaultdict(int)

    # T=O(n), n domains
    for domain in cpdomains:
        n = len(domain)
        whitespace_ix = 0
        subdomains = []
        # T=O(k), k characters in each domain on average
        for i in range(n - 1, -1, -1):
            char = domain[i]
            if char == " ":
                # S=O(s), where s is the number of subdomains
                subdomains.append(domain[i + 1:n])
                whitespace_ix = i
            elif char == ".":
                subdomains.append(domain[i + 1:n])

        count = int(domain[0:whitespace_ix])

        # T=O(s)
        for subdomain in subdomains:
            domain_visits[subdomain] += count

    # O(s)
    result = []
    for domain, visits in domain_visits.items():
        result.append(f"{visits} {domain}")

    # total time complexity = O(n(k + s) + s) = O(nk + ns + s) = O(nk + ns) = O(n * (k + s))
    # space complexity      = O(s)

    return result


if __name__ == '__main__':
    TR(
        (
            T(
                case=["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"],
                expected=["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]),
            T(
                case=["9001 discuss.leetcode.com"],
                expected=["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"],
            ),
        ),
        main,
        comparator,
    )()
