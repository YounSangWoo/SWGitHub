# 왜 나는 이런 생각을 못했을까 ... from : https://cotak.tistory.com/38


def append_star(n):
    if n ==1:
        return ['*']
    
    stars = append_star(n//3)
    L = []

    for s in stars:
        L.append(s*3)
    for s in stars:
        L.append(s+' '*(n//3)+s)
    for s in stars:
        L.append(s*3)
    return L

n = int(input())
print('\n'.join(append_star(n)))
        

        



  


    

