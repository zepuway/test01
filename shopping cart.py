commodity_list = [
    ('Apple', 10),
    ('Banana', 15),
    ('Orange', 20),
    ('Peach', 30),
    ('Grape', 50),
    ('Pear', 25),
]

shopping_car = []
charge = input("welcome to our shop!请输入你的钱包金额：")
if charge.isdigit():
    charge = int(charge)

    while True:
        print('商品列表:')
        for k, v in enumerate(commodity_list, 1):
            print(k, '', v)
        choice = input('选择购买商品编号[确认结算：q]：')
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(commodity_list):
                c_numbers = commodity_list[choice - 1]
                if c_numbers[1] < charge:
                    charge -= c_numbers[1]
                    shopping_car.append(c_numbers)
                    print(c_numbers)
                else:
                    print('钱包余额不足，还剩%s元' % charge)

            else:
                print('抱歉，没有此商品，请重新输入以下商品编号！')
        elif choice == 'q':
            print('购物车：')
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱' % charge)

            number = input('是否清空购物车[y/n]：')
            if number == 'y':
                shopping_car = []
                print('亲，购物车已空，请重新购买商品！')

            elif number == 'n':
                print('亲，购物结束，欢迎下次光临本店！')

            else:
                print('runoob！请重新考虑是否清空购物车')
        else:
            print('invalid input!Please re-enter the following number!')
else:
    print('invalid input!')