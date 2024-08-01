import asyncio
import aiohttp
import time

async def fetch(url, session):
    """
    Asynchronously send a GET request to the specified URL and print the response status.
    Handles exceptions by printing an error message.
    """
    try:
        async with session.get(url, timeout=60) as response:
            print(f"Response status: {response.status}")
    except Exception as e:
        print(f"Request failed: {e}")

async def main():
    """
    Main function to perform the stress test.
    - Configures the target URL, total number of requests, and number of concurrent requests.
    - Uses aiohttp to manage HTTP sessions and asyncio to manage concurrency.
    - Batches requests to avoid overwhelming the system.
    """
    url = 'http://exemple.com/'  # Replace with your website URL
    number_of_requests = 100000  # Total number of requests
    concurrent_requests = 100  # Number of concurrent requests

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(number_of_requests):
            if i % concurrent_requests == 0 and i > 0:
                await asyncio.gather(*tasks)
                tasks = []
                print(f"Completed {i} requests")
                time.sleep(1)  # Adding a delay between batches

            tasks.append(fetch(url, session))

        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
