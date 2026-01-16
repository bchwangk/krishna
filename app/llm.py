from typing import Optional, Dict
from app.erp import erp_plan

def mock_response(user_text: str, state: str, vignette: Optional[Dict], goal: Optional[str], trigger: Optional[str]) -> str:
    base = "Thanks for sharing that. "

    if state == "INTAKE":
        return base + "Understood"

    if state == "GOAL":
        return base + "Got it"

    if state == "WORK":
        return (
        "What part of this feels hardest to try, and what do you predict will happen if you delay the compulsion for 30 seconds?"
    )
    
    if state == "WRAP":
        g = f" Your goal was: {goal}." if goal else ""
        return (
            "Here’s what I’m taking away: you’re dealing with a recurring OCD-style loop where anxiety spikes and relief behaviors feel necessary."
            + g
            + "\nOne next step: try the ERP micro-experiment once, then reflect on what you noticed.\n"
            + "Would you like to check in after you try it?"
        )
    
    # Fall back - can work on this later down the road
    return base + "What’s the main pattern you’re noticing right now?"
