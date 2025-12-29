from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str


def greeting(state: AgentState) -> AgentState:
    print(f"{state["name"]}, you're doing an amazing job")

graph = StateGraph(AgentState)

graph.add_node("Greeting",greeting)
graph.set_entry_point("Greeting")
graph.set_finish_point("Greeting")

app=graph.compile()

app.invoke({"name":"Adwan"})