from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    age: int
    skills: list
    finalResult: str

def printGreeting(state: AgentState) -> AgentState:
    state["finalResult"] = f"Hello {state["name"]}, Welcome! "
    return state
def printAge(state: AgentState) -> AgentState:
    state["finalResult"] =state["finalResult"] +  f"Your age is {state["age"]}."
    return state
def printSkills(state: AgentState) -> AgentState:
    state["finalResult"] =state["finalResult"] +  f'You have skills in: {", ".join(state["skills"])}.'
    return state
graph = StateGraph(AgentState)
graph.add_node("printGreeting",printGreeting)
graph.add_node("printAge",printAge)
graph.add_node("printSkills",printSkills)
graph.set_entry_point("printGreeting")
graph.set_finish_point("printSkills")
graph.add_edge("printGreeting","printAge")
graph.add_edge("printAge","printSkills")
app=graph.compile()



result = app.invoke({"name":"Adwan","age":"24","skills":["AI","Pentesting","Python","LangGraph"]})
print(result["finalResult"])