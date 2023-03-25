########################### FIRST APPROACH #############################
def FindIndexOfString(alist,String):
    try:
       ans=alist.index(String)
       return ans
    except:
       return None
    
n=int(input())
alist=[]
for i in range(n):
    alist.append(input())   
string=input()
ans=FindIndexOfString(alist,string)
if ans:
    print("Position of the searched string is: ",ans)
else:
    print("String not found") 


###################### SECOND APPROACH ###############################
def FindIndexOfString(alist,String):
    n=len(alist)
    for i in range(n):
        if alist[i]==String:
            return i
    
n=int(input())
alist=[]
for i in range(n):
    alist.append(input())   
string=input()
ans=FindIndexOfString(alist,string)
if ans:
    print("Position of the searched string is: ",ans)
else:
    print("String not found") 