import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1,6):
        print(f"Силач {name} поднял {i} шар")
        await asyncio.sleep(10/power)
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    task_Pasha = asyncio.create_task(start_strongman('Pasha', 3))
    task_Denis = asyncio.create_task(start_strongman('Denis', 4))
    task_Apollon = asyncio.create_task(start_strongman('Apollon', 5))

    await task_Pasha
    await task_Denis
    await task_Apollon

asyncio.run(start_tournament())