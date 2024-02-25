import aiohttp
import asyncio

async def fetch_users(session):
    url = 'https://jsonplaceholder.typicode.com/users'
    async with session.get(url) as response:
        return await response.json()

async def fetch_posts(session):
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with session.get(url) as response:
        return await response.json()

async def main():
    async with aiohttp.ClientSession() as session:
        users = await fetch_users(session)
        posts = await fetch_posts(session)

        print(f'Users: {users[:1]}\n')  
        print(f'Posts: {posts[:1]}')  

asyncio.run(main())
