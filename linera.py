
pos = -1

def search(list,n):
    i=0
    while i<len(list):
        if list[i] == n:

            globals()['pos']=i
            return True
        i = i + 1

    return False        

list=[1,4,2,7,8,23,59]
n=23


if search(list,n):
    print(f"Found at : {pos}")  

else:
    print("Not Found") 