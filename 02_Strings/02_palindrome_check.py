import sys
def palindrome(s):
    left , right = 0,len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True

def main():
    s= sys.stdin.readline().strip()
    print(palindrome(s))

if __name__=="__main__":
    main()