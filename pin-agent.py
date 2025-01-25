from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
import asyncio
from browser_use import Browser

browser = Browser()

load_dotenv()


async def main():
    agent = Agent(
        task="Go to Reddit, search for 'saas ideas' and click on the first post and return the top 3 comments.",
        llm=ChatOpenAI(
            model="gpt-4o",
        ),
        browser=browser,
    )
    result = await agent.run()
    print(result)
    await browser.close()


asyncio.run(main())
