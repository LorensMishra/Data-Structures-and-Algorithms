import sys
def remove_duplicates(s):
    seen = set()
    result = ""

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch

    return result

def main():
    s = sys.stdin.readline().strip()
    print(remove_duplicates(s))


if __name__ == "__main__":
    main()