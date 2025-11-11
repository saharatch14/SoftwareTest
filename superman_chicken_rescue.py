def max_chickens_protected(n, k, positions):
    start = 0
    max_chickens = 0
    for end in range(n):
        # Expand the window [start, end]
        while positions[end] - positions[start] >= k:
            # shrink the window from the start
            start += 1
        
        # update max number of chickens protected
        max_chickens = max(max_chickens, end - start + 1)
    return max_chickens

# Parsing input
n, k = map(int, input().split())
positions = list(map(int, input().split()))
# Getting the result
result = max_chickens_protected(n, k, positions)
print(result)