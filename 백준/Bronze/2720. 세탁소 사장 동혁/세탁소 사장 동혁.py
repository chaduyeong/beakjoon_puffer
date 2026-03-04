T = int(input())

quarter = 25
dime = 10
nickel = 5
penny = 1
for _ in range(T):
    C = int(input())
    quarter_num = 0
    dime_num = 0
    nickel_num = 0
    penny_num = 0
    while C > 0 :
        if C >= 25 :
            C -= quarter
            quarter_num += 1
        elif C >= 10 :
            C -= dime
            dime_num += 1
        elif C >= 5 :
            C -= nickel
            nickel_num += 1
        else:
            C -= penny
            penny_num += 1
    print(quarter_num,dime_num,nickel_num,penny_num)