import sys
def compress_string(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result
def main():
    s = sys.stdin.read().strip()    
    if s:
        print(compress_string(s))
    else:
        print("")
if __name__ == "__main__":
    main()