import asyncio


async def cook(food, t):
    print(f'Microwave ({food}): Cooking {t} seconds...')
    await asyncio.sleep(t)
    print(f'Microwave ({food}): Finished cooking')
    return f'{food} is completed'


async def main():
    coros = [cook('Rice', 3), cook('Noodle', 3), cook('Curry', 3)]
    for coro in asyncio.as_completed(coros):
        result = await coro
        print(result)

if __name__ == '__main__':
    asyncio.run(main())
