from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    name: str
    operation: str
    numbers: list

def mathFunction(state: AgentState) -> AgentState:
    if state["operation"] == "+":
        answer = 0
        for value in state["numbers"]:
            answer += value
    elif state["operation"] == "*":
        answer = 1
        for value in state["numbers"]:
            answer = answer * value
    print(f" Hi {state["name"]}, Your answer is: {answer}")


graph = StateGraph(AgentState)
graph.add_node("mathFunction",mathFunction)
graph.set_entry_point("mathFunction")
graph.set_finish_point("mathFunction")
app=graph.compile()

app.invoke({"name":"Adwan","operation":"*","numbers":[1,2,3,4]})