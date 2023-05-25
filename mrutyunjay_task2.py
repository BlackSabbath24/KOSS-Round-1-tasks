import asyncio
import aiohttp
import time

async def download_comic_json(comic_id):
    url = f"https://xkcd.com/{comic_id}/info.0.json"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()
                filename = f"comic_{comic_id}.json"
                async with aiofiles.open(filename, "w") as file:
                    await file.write(await response.text())
                print(f"Downloaded comic {comic_id}")

async def main():
    tasks = [download_comic_json(i) for i in range(1, 201)]
    start_time_async = time.time()
    await asyncio.gather(*tasks)
    time_taken_async = time.time() - start_time_async
    print(f"Time Taken: {time_taken_async} seconds")
    print("Your file is downloaded")

asyncio.run(main())

