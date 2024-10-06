from crewai import Agent
from tools import youtube_search_tool, serper_tool

from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

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
    tools=[youtube_search_tool],
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
    tools=[youtube_search_tool],
    allow_delegation=False
)


news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[serper_tool],
    allow_delegation=True
)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[serper_tool],
  allow_delegation=False
)