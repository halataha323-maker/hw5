import os
from crewai import Agent, Task, Crew, Process

# הגדרת מפתח הגישה (יש להחליף במפתח אמיתי בזמן ההרצה בענן)
os.environ["OPENAI_API_KEY"] = "sk-YOUR-API-KEY-HERE"

# ==========================================
# 1. הגדרת הסוכנים (Agents)
# ==========================================
researcher = Agent(
    role="Market Researcher",
    goal="Find accurate technical specs for the home equipment product.",
    backstory="You are a meticulous research analyst for an e-commerce store.",
    verbose=True
)

writer = Agent(
    role="Content Writer",
    goal="Write a 300-word engaging product description.",
    backstory="You are a technical writer who turns facts into engaging articles.",
    verbose=True
)

seo_specialist = Agent(
    role="SEO Specialist",
    goal="Create Title Tags and Meta Descriptions.",
    backstory="You are an SEO expert crafting perfect metadata.",
    verbose=True
)

reviewer = Agent(
    role="Quality Reviewer",
    goal="Review the article and SEO metadata.",
    backstory="You are a senior editor ensuring high quality.",
    verbose=True
)

# ==========================================
# 2. הגדרת המשימות (Tasks)
# ==========================================
research_task = Task(description="Find specs for: {product_name}. Produce a summary.", expected_output="Structured research summary.", agent=researcher)
writing_task = Task(description="Write a short product article based on the research.", expected_output="Article in Markdown.", agent=writer)
seo_task = Task(description="Generate 1 Title Tag and 1 Meta Description.", expected_output="SEO Metadata.", agent=seo_specialist)
review_task = Task(description="Review all outputs for quality.", expected_output="Final polished article and metadata.", agent=reviewer)

# ==========================================
# 3. הרכבת הצוות והפעלה
# ==========================================
crew = Crew(
    agents=[researcher, writer, seo_specialist, reviewer],
    tasks=[research_task, writing_task, seo_task, review_task],
    process=Process.sequential, 
    verbose=True
)

result = crew.kickoff(inputs={"product_name": "Smart Home Robot Vacuum Cleaner"})

print("\n######################\nFINAL RESULT:\n######################\n")
print(result)
