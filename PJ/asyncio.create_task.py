import asyncio

async def say_hello():
    print("Hello!")
    await asyncio.sleep(1)
    print("Finished Hello!")

async def say_goodbye():
    print("Goodbye!")
    await asyncio.sleep(1)
    print("Finished Goodbye!")

async def main():
    task1 = asyncio.create_task(say_hello())
    task2 = asyncio.create_task(say_goodbye())

    await task1
    await task2

asyncio.run(main())
