from typing import Dict, Optional

def erp_plan(vignette: Dict, goal: Optional[str], trigger: Optional[str]) -> str:
    theme = vignette.get("theme", "ocd")

    if theme == "contamination":
        experiment = (
            "Delay hand washing by 30 seconds one time today, "
            "and allow the anxiety to rise and fall without neutralizing."
        )
    elif theme == "checking":
        experiment = (
            "Check once (instead of multiple times), then leave the situation "
            "without going back, and practice tolerating uncertainty."
        )
    elif theme == "intrusive_thoughts":
        experiment = (
            "Label the thought as 'I’m having the thought that…' "
            "and let it pass without analyzing or neutralizing it."
        )
    else:
        experiment = "Delay or reduce the compulsion slightly and observe the urge curve."

    goal_text = f"\nGoal you mentioned: {goal}" if goal else ""
    trigger_text = trigger or vignette.get("scenario") or "N/A"

    return (
        "ERP Micro-Experiment\n"
        "-------------------\n"
        f"Trigger: {trigger_text}\n\n"
        "Obsession: What thought or image shows up?\n"
        "Compulsion: What action or mental behavior reduces anxiety short-term?\n\n"
        f"ERP Experiment: {experiment}\n\n"
        "What to notice:\n"
        "- How strong the anxiety feels at first\n"
        "- Whether it rises, plateaus, or falls\n"
        "- What happens if you don’t complete the compulsion\n"
        f"{goal_text}\n\n"
        "Question: What part of this feels hardest to try?"
    )
