import heapq
from collections import Counter

language = ['python', 'php', 'go', 'go', 'go', 'php', 'java']

def top_n(language, n):
    counter_launage = Counter(language)

    data = [(-counter_launage[lang], lang) for lang in counter_launage] 
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(n)]

print(top_n(language, 3))