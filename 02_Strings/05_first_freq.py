def first_non_repeating(s):
    freq = {}

    # Step 1: Count frequency
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Step 2: Find first with freq = 1
    for ch in s:
        if freq[ch] == 1:
            return ch

    return -1


def main():
    s = input().strip()
    print(first_non_repeating(s))


if __name__ == "__main__":
    main()