import asyncio


async def wash(basket):
    print(f'Washing Machine ({basket}): Put the coin')
    print(f'Washing Machine ({basket}): Start washing...')
    await asyncio.sleep(5)
    print(f'Washing Machine ({basket}): Finished washing')
    return f'{basket} is completed'
