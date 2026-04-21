import sys

def longest_common_prefix(arr):
    if not arr:
        return ""

    prefix = arr[0]

    for s in arr[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


def main():
    arr = sys.stdin.read().split()
    result = longest_common_prefix(arr)
    print(result)


if __name__ == "__main__":
    main()