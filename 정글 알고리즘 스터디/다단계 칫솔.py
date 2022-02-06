from collections import defaultdict
def solution(enroll, referral, seller, amount):
    dadangae_list = defaultdict(list)
    answer = []
    for i in range(len(enroll)):
        if referral[i] !='-':
            dadangae_list[enroll[i]] = [referral[i],0]
        else :
            dadangae_list[enroll[i]] = ['center',0]
    
    referral_stack = []
    for i in range(len(seller)):
        tmp_money = amount[i]*10 #상납할 금액 
        dadangae_list[seller[i]][1] += (amount[i]*100-tmp_money)
        referral_stack.append(seller[i])
        while referral_stack:
            child = referral_stack.pop()
            parent = dadangae_list[child][0]
            if parent == 'center':
                break
            elif tmp_money < 10  :
                dadangae_list[parent][1]+= tmp_money
                break 
            else :
                referral_stack.append(parent)  
                dadangae_list[parent][1]+=(tmp_money - tmp_money//10)
                tmp_money = tmp_money//10
    
    for i in enroll:
        answer.append(dadangae_list[i][1])
    
          
    return answer