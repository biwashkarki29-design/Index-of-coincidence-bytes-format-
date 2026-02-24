#!/usr/bin/env python3
import sys
def index_of_coincidence(data: bytes) -> float:
    N = len(data)
    if N<2:
        return 0.0
    
    freq = [0] *256
    for b in data:
        freq[b] += 1

    ic = sum(f*(f - 1) for f in freq) / (N *(N - 1))
    return ic

def find_key_length(mysterytext: bytes, max_k = 60):
    results = []

    for k in range (1, max_k):
        columns = [mysterytext[i::k] for i in range(k)]
        ic_values = [index_of_coincidence(col) for col in columns]
        avg_ic = sum(ic_values) / k
        results.append((k, avg_ic))

    return results

with open(sys.argv[1], "rb") as f:
    mysterytext = f.read()

results = find_key_length(mysterytext)

for k, ic in results:
    print(f"Key Length {k:2d} -> IC = {ic:.6f}")






