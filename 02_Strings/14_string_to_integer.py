import sys

def string_to_int(s):
    sign = 1
    i = 0
    result = 0

    # handle sign
    if s[0] == '-':
        sign = -1
        i += 1
    elif s[0] == '+':
        i += 1

    # convert characters to integer
    while i < len(s):
        if not s[i].isdigit():
            break
        result = result * 10 + (ord(s[i]) - ord('0'))
        i += 1

    return sign * result


def main():
    s = sys.stdin.read().strip()
    
    if s:
        print(string_to_int(s))
    else:
        print(0)


if __name__ == "__main__":
    main()