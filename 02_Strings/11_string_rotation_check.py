import sys

def is_rotation(s1,s2):
    if len(s1)!=len(s2):
        return False
    temp = s1+s2
    return s2 in temp

def main():
    data = sys.stdin.readline().split()
    s1 = data[0]
    s2 = data[1]
    if is_rotation(s1,s2):
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
    
    