from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo   #enables an Agent to serach the web for information
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
PHIDATA_API_KEY = os.getenv("PHIDATA_API_KEY")

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role = "Serach the wen for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [DuckDuckGo()],
    instructions=["Always include the sources"],
    show_tool_calls= True,
    markdown=True,

)

# Financial Agnet
finanace_agent = Agent(
    name="Fianacial Search Agent",
    role = "Serach the wen for the information",
    model = Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                        company_news=True)],
    show_tool_calls=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True,

)

muti_ai_agent = Agent(
    team = [web_search_agent, finanace_agent],
    model = Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include the sources","Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown= True
)

muti_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream= True)


