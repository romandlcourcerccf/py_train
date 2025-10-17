import time

from collections import defaultdict

freqs = defaultdict(int)

start = time.time()
with open("/Users/roman/Downloads/googlebooks-eng-all-1gram-20120701-a", "r") as reader:
    lines = reader.readlines()

    for line in lines:
        data = line.split()
        word = data[0]
        count = int(data[2])
        freqs[word] += 1

print(f"{time.time() - start: .4f}")
