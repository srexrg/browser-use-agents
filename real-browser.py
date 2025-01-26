import asyncio
import os
import dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, SecretStr
from browser_use.agent.service import Agent
from browser_use.controller.service import Controller
from browser_use import Browser, BrowserConfig

dotenv.load_dotenv()

browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    )
)

controller = Controller()


class WebpageInfo(BaseModel):
    link: str = "https://calendar.google.com/"


@controller.action("Go to the webpage", param_model=WebpageInfo)
async def go_to_webpage(webpage_info: WebpageInfo):
    return webpage_info.link


async def main():
    task = (
        "Go to the Google Calendar webpage via the link I provided you. "
        "Check if there is an event scheduled for this month. "
        "If there is any, return the event title and the time, if not create one for 27th jan at 10:00 am to 11:00 am named 'meeting with michael'"
    )

    model = ChatOpenAI(
        model="gpt-4o", api_key=SecretStr(os.getenv("OPENAI_API_KEY", ""))
    )
    agent = Agent(task, model, controller=controller, use_vision=False, browser=browser)

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
