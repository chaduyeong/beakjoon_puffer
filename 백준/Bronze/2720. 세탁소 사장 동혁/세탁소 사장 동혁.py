T = int(input())
for _ in range(T):
    C = int(input())

    quarter_num = C // 25
    C %= 25

    dime_num = C // 10
    C %= 10

    nickel_num = C // 5
    C %= 5

    penny_num = C
    print(quarter_num,dime_num,nickel_num,penny_num)