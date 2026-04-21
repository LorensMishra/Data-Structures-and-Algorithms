import sys
def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False 
    
    freq = {}
    for ch in s1:
        freq[ch]=freq.get(ch,0)+1
    for ch in s2:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True
def main():
    data = sys.stdin.readline().split()
    s1=data[0]
    s2=data[1]
    if is_anagram(s1,s2):
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
