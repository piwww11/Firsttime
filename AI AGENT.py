# Simple AI Agent - Fixed Version

from xai_sdk import Client
from langchain_xai import ChatXAI
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import MessagesPlaceholder
from langchain.agents import AgentState
from langchain.agents.middleware.types import AgentState
from langchain_core.tools.structured import StructuredTool
from langchain_core.tools import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_core.prompts import ChatPromptTemplate

import os

os.environ["XAI_API_KEY"] = "PASTE_YOUR_API_KEY_HERE"
from langchain_xai import ChatXAI
# Initialize LLM
llm = ChatXAI(model="grok-beta")

# 1. Buat prompt template
prompt_template = ChatPromptTemplate.from_messages([
     ("system", "You are an AI assistant that helps users finds answers to their questions using the tools provided."),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
])


# Initialize search tool
search = SerpAPIWrapper(
    serpapi_api_key="PASTE_YOUR_API_KEY_HERE"
)


def web_search(query: str) -> str:
        """Berguna kalo butuh cari info terkini dari Google/web"""
        return search.invoke(query)

tools = [
        StructuredTool.from_function(
            func=web_search,
            name="web_search",
            description="Berguna kalo butuh cari info terkini dari Google/web"
        )
]

# Create agent using initialize_agent (sudah ada import-nya)
agent = create_tool_calling_agent(llm, tools, prompt_template)
agent_executor = AgentExecutor(agent=agent, tools=tools)
# Interactive agent test
print("===================================")
print("   AI AGENT LU SUDAH HIDUP BRO 🔥")
print("===================================")
print("Tanya apa aja, agent bakal mikir & cari info kalo perlu.")
print("Ketik 'keluar' buat stop.\n")

while True:
    tanya = input("\nTanya ke agent: ")
    if tanya.lower() == "keluar":
        print("Agent mati dulu ya bro, good job hari ini! 🚀")
        break
    
    try:
        result = agent_executor.invoke({"input":tanya})
        print(f"\nJawaban: {result['output']}\n")
    except Exception as e:
        print(f"Agent error: {e}")
