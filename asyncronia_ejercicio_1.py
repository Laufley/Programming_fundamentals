import asyncio

async def heat_water() :
    print("heating water")
    await asyncio.sleep(3)
    print("water heated!")

async def add_leaves():
    print("adding the leaves")
    await asyncio.sleep(2)
    print("leaves added!")

async def pour_tea():
    print("pouring....")
    await asyncio.sleep(1)
    print("tea poured!")

async def make_tea() :
    await asyncio.gather(
        heat_water(),
        add_leaves(),
        pour_tea()
    )
    print("tea brewed, enjoy!")

asyncio.run(make_tea())