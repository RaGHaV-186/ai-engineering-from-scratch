import tracemalloc

tracemalloc.start()

# allocate some stuff
small = [1, 2, 3]
big = [i for i in range(100000)]
matrix = [[0] * 1000 for _ in range(100)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics("lineno")

print("Top 5 memory allocations:")
for stat in top_stats[:5]:
    print(stat)