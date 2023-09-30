# fee
# 기본시간 / 기본요금 / 단위시간 / 단위요금
# record
# 시각 차량번호 내역

# output
# 차량번호자 작은 자동차부터 청구 한다.
from collections import defaultdict


def cal_fee(time_lst, fees):
    basic_time, basic_fee, unit_time, unit_fee = fees

    l = len(time_lst)
    # if time_lst의 길이가 홀수라면 마지막 out이 없는 것이니:
    if l % 2 == 1:
        time_lst.append(24 * 60 - 1)
    total_time = 0
    for idx in range(0, l, 2):
        in_time, out_time = time_lst[idx], time_lst[idx+1]
        total_time = total_time + out_time - in_time

    # total_time 이 기본 시간보다 작으면 기본요금
    # 크면 기본요금 + @
    if total_time <= basic_time:
        fee = basic_fee
    else:
        over_time = total_time - basic_time
        # 올림
        # from math import ceil
        # unit = ceil(over_time / unit_time)
        if over_time % unit_time == 0:
            unit = over_time // unit_time
        else:
            unit = over_time // unit_time + 1
        fee = basic_fee + unit * unit_fee
    return fee




def solution(fees, records):
    # 차량 번호를 key값으로 가지는 녀석
    # value
    car_dic = defaultdict(list)

    for record in records:
        time, car_num, status = record.split()
        time = int(time[:2]) * 60 + int(time[-2:])
        car_dic[car_num].append(time)
    answer = []

    # car_dic에 있는 car_num 을 돌면서 위의 시간을 계산해 줄 것입니다.
    for car in sorted(car_dic.keys()):
        answer.append(cal_fee(car_dic[car], fees))

    return answer



s = solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])
print(s)




