from crewai import Agent
from tools import yt_tool

from dotenv import load_dotenv
import os


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"

blog_researcher=Agent(
    role="Blog researcher from youtube videos",
    goal="Get the relevant video transcription for the topic {topic} from the provide youtube channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in the understanding podcast videos and providing suggestion"
    ),
    tools=[yt_tool],
    allow_delegation=True
)

blog_writer = Agent(
    role="Blog writer",
    goal="Narrate compelling tech stories about the video {topic} from Youtube video",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    allow_delegation=False
)
