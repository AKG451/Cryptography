import itertools
import random

text = input("Enter the text to permute:")
print(random.choice([''.join(p) for p in itertools.permutations(text)]))
