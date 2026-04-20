import sys
def count_all(s):
    vowels="aeiouAEIOU"
    v_c,c_c,d_c,s_c=0,0,0,0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_c+=1
            else:
                c_c+=1
        elif ch.isdigit():
            d_c+=1
        elif ch.isspace():
            s_c+=1
    return (v_c,c_c,d_c,s_c)

def main():
    s=sys.stdin.readline().strip()
    v,c,d,sp=count_all(s)
    print(v,c,d,sp)

if __name__=="__main__":
    main()
