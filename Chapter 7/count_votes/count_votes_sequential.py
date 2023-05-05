#!/usr/bin/env python3

"""Counting votes sequentially"""

import typing as T
import random

Summary = T.Mapping[int, int]


def process_votes(votes: T.List[int]) -> Summary:
    total_summary = {}
    for candidate in votes:
        if total_summary.get(candidate):
            total_summary[candidate] += 1
        else:
            total_summary[candidate] = 1
    return total_summary


if __name__ == "__main__":
    num_candidates = 3
    num_voters = 100000
    # generating a huge list of votes
    # each vote is an integer represents the selected candidate
    votes = [random.randint(1, num_candidates) for _ in range(num_voters)]
    counts = process_votes(votes)
    print(f"Total number of votes: {counts}")
