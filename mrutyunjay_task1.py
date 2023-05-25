import aiohttp
import asyncio
import time

async def get_page(el):
    url = f"https://reqres.in/api/users?page={el}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            page = await response.text()
            print(f"Downloaded page {el}")
            return page

async def main():
    arr = [1, 2, 3]
    coroutines = [get_page(el) for el in arr]

    start = time.time()

    await asyncio.gather(*coroutines)

    time_taken = time.time() - start
    print('Time Taken: {0}'.format(time_taken))
    print("Your file is downloaded!")

asyncio.run(main())
