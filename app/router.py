from dataclasses import dataclass
from typing import Optional

STATES = ("INTAKE", "GOAL", "WORK", "WRAP")

@dataclass
class SessionState:
    state: str = "INTAKE" #start with INTAKE as base state
    turns: int = 0
    state_turns: int = 0
    goal: Optional[str] = None
    vignette_id: Optional[str] = None
    pending_intro: bool = False
    awaiting_goal: bool = False
    trigger: Optional[str] = None
    erp_done: bool = False

def next_state(session: SessionState) -> None:
    # Intake a statement to intialize a goal
    if session.state == "INTAKE" and session.state_turns >= 2: 
        session.state = "GOAL"
        session.awaiting_goal = True
        session.state_turns = 0
        return

    # Once goal receives confirmation, shift to work
    elif session.state == "GOAL" and session.awaiting_goal is not None: 
        session.state = "WORK"
        session.state_turns = 0
        return
    
    # After 6 turns (will change later), finish session
    elif session.state == "WORK" and session.state_turns >= 6:
        session.state = "WRAP"
        session.state_turns = 0
        return