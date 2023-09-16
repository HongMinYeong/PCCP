#fee
#기본시간/기본요금/단위시간/
#record
# 시각 
#output
#차량번호 작은 자동차부터 청구한다.
from collections import defaultdict

#요금을 계산하는 함수 
def cal_fee(time_lst,fees):
    basic_time, basic_fee, unit_time, unit_fee = fees


    l = len(time_lst)
    #if time_list의 길이가 홀수라면 마지막 out이 없는 것이니:
    if l % 2 == 1: #in out in 일때 -> out이 없을 때 
        time_lst.append(24 * 60 - 1) #23:59
    total_time = 0
    for idx in range(0,l,2): #전체리스트를 두개씩 묵기 
        in_time,out_time = time_lst[idx],time_lst[idx+1]
        total_time = total_time+out_time - in_time
    

    #total_time이 기본시간보다 작으면 기본요즘 
    if total_time <= basic_time:
        fee = basic_fee
    else:
        over_time = total_time - basic_time
        #올림 (4.5 -> 5 즉 나누어떨어지지않으면 올려 ) -> 또는 from math import ceil,round,floor 
        if over_time % unit_time == 0:
            unit = over_time//unit_time
        else:
            unit = over_time//unit_time + 1

        fee = basic_fee + unit * unit_fee
    return fee

    #total_time이 기본시간보다 크면 + a

    #idx,idx+1 번째를 가져올거얌 

    
    #out - in 이라는 숫자를 total_time에다가 더해줄거임 

def solution(fees,records):
    #차량 번호를 key값으로 가지는 녀석
    #value
    car_dic = defaultdict(list)
    
#car_dic를 채워나가겠다.
# car_dic[car_num] = 시간을 사용한 리스트를 가져야해
    for record in records:
        time,car_num,status = record.split()
        time = int(time[:2]) * 60 + int(time[-2:])
        car_dic[car_num].append(time)
    
    for car in sorted(car_dic.keys()):
        print(cal_fee(car_dic[car]))
    print(' ')
    print(car_dic)
    answer = []

    for car in 
    return answer
        

        


solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
#주차요금은 일괄로 정산 