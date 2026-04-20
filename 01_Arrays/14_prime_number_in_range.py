import sys

def solve():
    n = int(sys.stdin.readline().strip())
    
    for num in range(2, n + 1):
        is_prime = True
        
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")

if __name__ == "__main__":
    solve()