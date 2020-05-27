import asyncio
import time


async def wash(basket):
    print(f'Washing Machine ({basket}): Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'


async def main():
    coros = []
    for i in range(1, 100001):
        coros.append(wash(f'Basket {i}'))
    results = await asyncio.wait(coros)
    print(f'Completed task: {len(results[0])}')
    print(f'Uncompleted task: {len(results[1])}')


if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')
