import random

def getNumbers(num: int) -> list[int]:
    # num * -3.000 ~ 3.000 사이의 숫자 15개
    rand_percent = set([])
    rand_sum = list([])

    while True:
        rand_num = random.uniform(-3.000, 3.000)
        if not rand_percent.__contains__(rand_num):
            rand_percent.add(rand_num)
        if len(rand_percent) == 15:
            break

    for percentage in rand_percent:
        rand_sum.append(int((num * percentage * 0.01) + num))

    random.shuffle(rand_sum)
    return rand_sum[:4]



if __name__ == '__main__':
    # func([1,2,3,4])
    while True:
        key = int(input('1: 입력 시작, 2: 프로그램 종료\n번호를 입력하세요: '))

        if key == 1:
            print('\n++++프로그램을 시작합니다++++\n')
            number = int(input('숫자를 입력하세요: '))
            nums = getNumbers(number)
            print('\n생성된 숫자는 다음과 같습니다.')
            print(nums)
            print('\n+++++++++++++++++++++++\n\n')

        if key == 2:
            print('\n++++프로그램을 종료합니다++++')
            break
