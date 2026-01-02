n = int(input())
arr = list(map(int, input().split()))
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key in freq:
    print(key, ":", freq[key])        
