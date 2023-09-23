'''
원의 정의
원: 한 점에서 거리가 같은 점들의 집합
상대편 마린(류재명)이 있을 수 있는 위치의 수를 구한다
== 각 터렛의 좌표와 반지름이 주어지고, 이에 대한 원의 접점을 구하라
'''
######################################################
'''
두 원의 반지름 r1,r2
두 원의 중심 사이의 거리 d
두 원의 접점이 생길 수 있는 경우의 수 총 4가지

1.두 원의 접점이 0개인 경우
-(r1,r2,d중 가장 큰 수가 나머지 두 수의 합보다 큰 경우)
-(두 원의 중심은 같으나 반지름의 길이가 다른 경우)
-두 원이 서로 멀리 떨어져 있는 경우:접점 0개
-작은 원이 큰 원안에서 접하는 부분이 없을 경우 접점 0개

2.두 원의 접점이 무수희 많은 경우
-(r1,r2,d가 모두 같은 경우)
-두 원의 중심이 같고 반지름도 같다면 접점은 무수히 많음

3. 두 원의 접점이 1개인 경우
-(r1,r2의 합이 d와 같은 경우:외접)
-(r1,r2의 차가 d와 같은 경우:내접)
-두 원이 외접, 내접 하는 경우 접점이 하나

4. 두 원의 접점이 2개인 경우
-위 3가지를 제외한 나머지(else처리?)
'''
##################################################
import math #절댓값 함수를 사용하기 위해 수입

T = int(input()) #테스트 케이스의 개수 t 입력받기

for _ in range(T): #반복문
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) #각 좌표의 위치 한번에 입력받기
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) #두 원의 중심 사이의 거리

    if x1 == x2 and y1 == y2: #원의 중심이 같을 때
        if r1 == r2: #두 원의 반지름이 같을 때
            print(-1) #접점이 무수히 많음, -1출력
        else:#두 원의 반지름이 같지 않을 때
            print(0) #접점이 없음
    
    else: #두 원의 중심이 같지 않을 때
        if r1 > distance + r2 or r2 > distance + r1 or distance > r1 + r2: #가장 큰 수가 나머지 두 수의 합보다 큰 경우
            print(0) #접점이 없음
        elif abs(r1 - r2) == distance or r1 + r2 == distance: #두 원이 외접(반지름의 합이 d와 같을 때)하거나 내접(반지름의 차가 d와 같을 때)할 때
            print(1) #접점이 하나
        else: #그렇지 않을 경우(위 3가지 케이스를 제외한 나머지)
            print(2) #접점이 2개