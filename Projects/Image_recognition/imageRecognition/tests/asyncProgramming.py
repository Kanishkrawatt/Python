import asyncio

async def Hello():
    task = asyncio.create_task(Hello2())
    print("Hello")
    await asyncio.sleep(1)
    print("World")


async def Hello2():
    print("Hello2")

asyncio.run(Hello())