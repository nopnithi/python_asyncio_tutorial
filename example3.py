import time


def wash(basket):
    print(f'Washing Machine ({basket}): Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    time.sleep(5)
    print(f'Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'


def main():
    for basket in ['Basket A', 'Basket B']:
        wash(basket)


if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')

