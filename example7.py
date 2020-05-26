import asyncio


async def cook(food, t):
    print(f'Microwave ({food}): Cooking {t} seconds...')
    await asyncio.sleep(t)
    print(f'Microwave ({food}): Finished cooking')
    return f'{food} is completed'


async def main():
    coros = [cook('Rice', 5), cook('Noodle', 3), cook('Curry', 1)]
    results = await asyncio.wait(coros, return_when='FIRST_COMPLETED')
    print(f'Completed task: {len(results[0])}')
    for completed_task in results[0]:
        print(f' - {completed_task.result()}')
    print(f'Uncompleted task: {len(results[1])}')


if __name__ == '__main__':
    asyncio.run(main())
