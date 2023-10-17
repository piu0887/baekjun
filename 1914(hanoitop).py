n= int(input())

def hanoi (n, start, destination, via):

    #하노이 탑 규칙에 따라 원반을 옮기고, 옮길때 마다 원반의 시작 위치와 이동한 위치를 출력합니다.
    #마지막으로 총 이동 횟수를 반환합니다.
    #params
    # n: 총 원반 개수    start: 시작기둥   destination : 도착기둥   via: 보조 기둥 : return count:

    # 원반이 1개 일 때 시작 기둥에서 도착 기둥까지 한번에 이동
    if n == 0:
        return
    hanoi (n-1, start, via, destination)
    print(start, destination)
    hanoi(n-1,via,destination,start)


print(2**n -1 )
if n <=20 :
    hanoi(n,1,3,2)