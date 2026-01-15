def state_intro(state: str) -> str:
    if state == "INTAKE":
        return (
            "Let’s start with what’s been happening. "
            "Share a recent situation where anxiety or intrusive thoughts showed up."
        )

    if state == "GOAL":
        return (
            "Let’s define a small, realistic goal for the next 1–2 weeks. "
            "For example: reduce checking by one step, delay a compulsion, or tolerate uncertainty for 30 seconds."
        )
    
    if state == "WORK":
        return (
            "Let’s work with a specific example. "
            "We’ll name the OCD cycle and pick one small experiment."
        )
    
    if state == "WRAP":
        return (
            "Let’s wrap up: I’ll summarize what I heard and suggest one next step you can try."
        )
    return ""