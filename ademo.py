import asyncio

DELAY = 0.5

async def pre_processing():
    await asyncio.sleep(DELAY)


async def foo():
    await asyncio.sleep(DELAY)


async def bar():
    await asyncio.sleep(DELAY)


async def baz():
    await asyncio.sleep(DELAY)


async def sub_processing():
    await foo()
    await bar()
    await baz()


async def processing():
    await asyncio.gather(
        asyncio.create_task(sub_processing()),
        asyncio.create_task(sub_processing()),
        asyncio.create_task(sub_processing()),
    )


async def post_processing():
    await asyncio.sleep(DELAY)


async def request():
    await pre_processing()
    await processing()
    await post_processing()


asyncio.run(request())
