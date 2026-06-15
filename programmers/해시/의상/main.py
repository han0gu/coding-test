"""
카테고리별 1개까지 가능
아무거나 1개 이상 입으면 됨
입는 순서는 의미가 없음

같은 이름의 의상 없음
전체 의상 1~30개
"""
from collections import Counter

def solution(clothes):
    answer = 1
    
    # 카테고리별로 dict 생성
    category_dict = Counter(cate for _, cate in clothes)
    # print('category_dict', category_dict)
    
    # (각 카테고리의 개수 + 안 입는 경우)의 곱셈
    for v in category_dict.values():
        answer *= v + 1
    
    # 아무것도 안 입는 경우 제외
    return answer - 1