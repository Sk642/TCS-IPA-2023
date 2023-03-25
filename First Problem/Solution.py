######################## FIRST APPROACHE #########################
def ValidString(alist):
    res=[0,0]
    for item in alist:
        val=item.split()
        s=""
        for st in val:
            s+=st
        if st.isalpha():
           res[0]+=1
        else:
           res[1]+=1
    return res
            
n=int(input())
alist=[]
for i in range(n):
    alist.append(input().lower())

ans=ValidString(alist)
print(f"Count Of Valid Strings={ans[0]}")
print(f"Count Of Invalid Strings={ans[1]}")

######################### SECOND APPROACHE #########################
def ValidString(alist):
    Valid=0
    Invalid=0
    for item in alist:
        val=item.split()
        s=""
        for st in val:
            st=s.join(st)
        if st.isalpha():
           Valid+=1
        else:
           Invalid+=1
    return [Valid,Invalid]
            
n=int(input())
alist=[]
for i in range(n):
    alist.append(input().lower())

Valid,Invalid=ValidString(alist)
print("Count Of Valid Strings=",Valid)
print("Count Of Invalid Strings=",Invalid)