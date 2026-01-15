from dataclasses import dataclass
from typing import Optional

STATES = ("INTAKE", "GOAL", "WORK", "WRAP")

@dataclass
class SessionState:
    state: str = "INTAKE"
    turns: int = 0
    goal: Optional[str] = None
    vignette_id: Optional[str] = None

def next_state(session: SessionState) -> None:
    # Intake a statement to intialize a goal
    if session.state == "INTAKE" and session.turns >= 1: 
        session.state = "GOAL"

    # Once goal receives confirmation, shift to work
    elif session.state == "GOAL" and session.turns >= 2:
        session.state = "WORK"
    
    # After 6 turns (will change later), finish session
    elif session.state == "WORK" and session.turns >= 6:
        session.state = "WRAP"