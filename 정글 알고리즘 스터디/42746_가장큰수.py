def solution(numbers):
     
    numberse = list(map(str,numbers))
    numberse.sort(key = lambda x : x*3, reverse = True)
    ## 3행에서 문자열로 바꾸었기 아스키코드순으로 정렬되며 조건이 1000이하이므로 3자리 를 맞추기 위해 각 문자를 3번 곱해준다.
    ## 666 101010 222 에서 아스키 문자열이 큰 순으로는 6 2 1순으로 [6,2,10]이 된다.
    ## answer = ''.join(numberse) 이건 왜 안될까?  아래 해답
    ## 모든 값이 0일 때(즉, '000'을 처리하기 위해) int로 변환한 뒤, 다시 str로 변환한다
    answer = str(int(''.join(numberse)))
    
    return answer
