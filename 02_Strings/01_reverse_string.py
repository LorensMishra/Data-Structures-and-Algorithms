import sys

def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

def main():
    s = sys.stdin.readline().strip()
    print(reverse_string(s))

if __name__ == "__main__":
    main()