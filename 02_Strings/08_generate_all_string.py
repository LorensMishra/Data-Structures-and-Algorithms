import sys

def get_substrings(s):
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])


def main():
    s = sys.stdin.readline().strip()
    get_substrings(s)


if __name__ == "__main__":
    main()