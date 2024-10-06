from crewai_tools import YoutubeChannelSearchTool
from crewai_tools import SerperDevTool
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

# Initialize the tool with a specific Youtube channel handle to target your search
youtube_search_tool = YoutubeChannelSearchTool(youtube_channel_handle='@sibaramsahu2463')

# Initialize the tool for internet searching capabilities
serper_tool = SerperDevTool()