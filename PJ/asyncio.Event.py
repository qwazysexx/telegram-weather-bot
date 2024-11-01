import asyncio

event = asyncio.Event()

async def waiter():
    print("Waiting for the event to be set...")
    await event.wait()  
    print("Event is set! Continuing execution...")

async def trigger():
    await asyncio.sleep(3) 
    print("Setting the event.")
    event.set()

async def main():
    await asyncio.gather(waiter(), trigger())

asyncio.run(main())
