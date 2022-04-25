import random

# 각 10%, 20%, 30%, 40% 확률인 경우

products = {'꽝': 69.89,
            '2000원': 20,
            '3000원': 10,
            '20000원': 1,
            '200000원': 0.1,
            '1000000원': 0.01
            }


def MainLot():
    # 총 추첨 수
    count = 1

    productrange = []
    productresult = []

    for product in products:

        if not productrange:
            productresult.append(product)
            productrange.append(products[product])
        else:
            productresult.append(product)
            productrange.append(productrange[-1] + products[product])

    for j in range(0, count):
        tempresult = random.randrange(1, productrange[-1]+1)
        tempcnt = 0
        for i in productrange:
            # print('i',i)
            if tempresult <= i:
                return productresult[tempcnt]
            else:
                tempcnt = tempcnt+1


MainLot()
