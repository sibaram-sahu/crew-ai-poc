from crewai import Crew,Process
from agents import blog_researcher,blog_writer, news_researcher, news_writer
from tasks import yt_research_task,yt_write_task, sp_research_task, sp_write_task


# Forming the tech-focused crew with some enhanced configurations
def youtube_search():
    # yt_crew = Crew(
    #     agents=[blog_researcher, blog_writer],
    #     tasks=[yt_research_task, yt_write_task],
    #     process=Process.sequential,  # Optional: Sequential task execution is default
    #     memory=True,
    #     cache=True,
    #     max_rpm=100,
    #     share_crew=True
    # )
    # result=yt_crew.kickoff(inputs={'topic':'The Naval Podcast - Naval Ravikant with BeerBiceps'})    
    # print(result)
    pass


def news_search():
    sp_crew=Crew(
        agents=[news_researcher,news_writer],
        tasks=[sp_research_task, sp_write_task],
        process=Process.sequential,
    )
    result=sp_crew.kickoff(inputs={'topic':'AI in healthcare'})
    print(result)

def main(search_type = "search"):
    print(">>>", search_type)
    news_search()
    # if search_type == "search":
    #     youtube_search()    
    # else:
    #     news_search()


if __name__ == "__main__":
    main("search")