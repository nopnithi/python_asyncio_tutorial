import asyncio
import time


async def wash(basket):
    print(f'Washing Machine ({basket}): Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(wash('Basket A'))
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')
