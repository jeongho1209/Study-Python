def solution(numbers):
    answer = []
    numbers.sort()

    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])

    newAnswer = set(answer)
    return sorted(list(newAnswer))
