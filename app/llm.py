from typing import Optional, Dict

def mock_response(user_text: str, state: str, vignette: Optional[Dict], goal: Optional[str]) -> str:
    base = "Thanks for sharing that. "

    if state == "INTAKE":
        return base + "What’s a recent moment where the anxiety or urge showed up most strongly?"

    if state == "GOAL":
        return base + "If we aimed for a small win in 1–2 weeks, what would you want to be different?"

    if vignette:
        theme = vignette.get("theme", "ocd")
        scenario = vignette.get("scenario", "")
        if theme == "contamination":
            tip = "A small ERP-style experiment could be delaying washing by 10–30 seconds once, and noticing what happens to the urge."
        elif theme == "checking":
            tip = "A small experiment could be reducing checking by one round (e.g., check once, then leave) and practicing uncertainty tolerance."
        elif theme == "intrusive_thoughts":
            tip = "A small practice could be labeling the thought: 'I’m having the thought that ___' and letting it pass without analyzing it."
        else:
            tip = "A small experiment could be delaying the compulsion slightly and observing the urge curve."

        if state == "WRAP":
            g = f" Your goal was: {goal}." if goal else ""
            return (
                "Here’s what I’m taking away: you’re dealing with a recurring OCD-style loop where anxiety spikes and relief behaviors feel necessary."
                + g
                + " One next step: "
                + tip
                + " Would you like to try that once before we end?"
            )

        return (
            f"{base}It sounds like a {theme}-pattern.\n\n"
            f"Example vignette: {scenario}\n\n"
            f"{tip}\n\n"
            "What part of that experiment feels hardest—starting it, staying with the anxiety, or resisting the 'one more time' urge?"
        )

    return (
        base
        + "I’m not fully sure which theme fits yet (checking, contamination, intrusive thoughts, etc.). "
        + "What do you notice yourself doing to reduce the anxiety in the moment?"
    )
