import asyncio

lock = asyncio.Lock()

async def access_shared_resource(name):
    print(f"{name} is waiting to access the resource...")
    async with lock:
        print(f"{name} has access to the resource!")
        await asyncio.sleep(1)
        print(f"{name} released the resource")

async def main():
    await asyncio.gather(
        access_shared_resource("Task 1"),
        access_shared_resource("Task 2"),
        access_shared_resource("Task 3")
    )

asyncio.run(main())
