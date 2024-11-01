import asyncio

semaphore = asyncio.Semaphore(2)  

async def download(name):
    async with semaphore:
        print(f"{name} is downloading...")
        await asyncio.sleep(2)  
        print(f"{name} has finished downloading")

async def main():
    await asyncio.gather(
        download("Download 1"),
        download("Download 2"),
        download("Download 3"),
        download("Download 4")
    )

asyncio.run(main())
