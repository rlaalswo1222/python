##김민재 2021041070
import random

 

d1,d2,d3,d4,d5,d6 = [0] * 6

throwCount, serialCount = 0,0

 

if __name__ == "__main__":

    while True:

        throwCount += 1

 

        d1 = random.randrange(1,7)

        d2 = random.randrange(1,7)

        d3 = random.randrange(1,7)

        d4 = random.randrange(1,7)

        d5 = random.randrange(1,7)

        d6 = random.randrange(1,7)

 

        if d1 == d2 == d3 == d4 == d5 == d6 :

            print('6개의 주사위가 모두 동일한 숫자가 나옴 -->',d1,d2,d3,d4,d5,d6)

            break

        elif(d1==1 or d2==1 or d3==1 or d4==1 or d5==1 or d6==1) and \
            (d1==2 or d2==2 or d3==2 or d4==2 or d5==2 or d6==2) and \
            (d1==3 or d2==3 or d3==3 or d4==3 or d5==3 or d6==3) and \
            (d1==4 or d2==4 or d3==4 or d4==4 or d5==4 or d6==4) and \
            (d1==5 or d2==5 or d3==5 or d4==5 or d5==5 or d6==5) and \
            (d1==6 or d2==6 or d3==6 or d4==6 or d5==6 or d6==6) :
            serialCount += 1

 

        print('6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수 -->',throwCount)
        print('6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수 -->',serialCount)
