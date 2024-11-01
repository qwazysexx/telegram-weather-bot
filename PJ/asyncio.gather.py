import asyncio

async def download_file(file):
    print(f"Downloading {file}...")
    await asyncio.sleep(2) 
    print(f"{file} downloaded.")

async def main():
    await asyncio.gather(
        download_file("file1.txt"),
        download_file("file2.txt"),
        download_file("file3.txt")
    )

asyncio.run(main())
