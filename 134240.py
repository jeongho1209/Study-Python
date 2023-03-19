def solution(food):
    answer = ''
    lst = []

    for index, element in enumerate(food[1:]):
        onePersonFoodCount = int(element / 2)
        for _ in range(onePersonFoodCount):
            lst += str(index + 1)
    for n in lst:
        answer += n
    answer += '0'
    for n in reversed(lst):
        answer += n

    return answer