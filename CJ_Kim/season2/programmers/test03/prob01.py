# 100점
'''
🥤
일반화된 콜라 문제
빈 병 a 개를 가져다주면 콜라 b 병을 주는 마트가 있을 때,
빈 병 n 개를 가져다주면 몇 병을 받을 수 있는지 계산
'''

def solution(a, b, n):
    answer = 0
    # 바꿔주는 단위 개수보다 많이 있을 때,
    # 단위 개수보다 작아질 때까지 계산
    while n >= a:
        # 단위 개수로 나눈 몫을 미리 대기
        getReady = n // a
        # 전체 병 수에서 바꿀 만큼 빼기
        n -= getReady * a
        # 새 콜라 병수 세기
        newBottle = getReady*b
        answer += newBottle
        n += newBottle
    return answer