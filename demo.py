import asyncio


async def pre_processing():
    await asyncio.sleep(0.5)


async def foo():
    await asyncio.sleep(0.1)


async def bar():
    await asyncio.sleep(0.2)


async def baz():
    await asyncio.sleep(0.3)


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
    await asyncio.sleep(0.5)


async def request():
    await sub_processing()
    await processing()
    await post_processing()


asyncio.run(request())
