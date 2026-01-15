from app.config import USE_MOCK_MODEL
from app.llm import mock_response
from app.router import SessionState, next_state
from app.prompt import state_intro

def main():
    print("Krishnamurti (CLI) — OCD-informed CBT/ERP support (not diagnosis).")
    print("Type /quit to exit.\n")

    session = SessionState()

    # initial prompt for intake
    print(f"Krishnamurti: {state_intro(session.state)}\n")

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() == "/quit":
            print("Krishnamurti: Take care.")
            break

        if session.state == "GOAL" and session.goal is None:
            session.goal = user

        if USE_MOCK_MODEL:
            assistant_text = mock_response(user)
        else:
            raise RuntimeError("Real LLM mode not enabled yet")

        print(f"\nKrishnamurti ({session.state}): {assistant_text}\n")

        # Update turn count and advance state if needed
        session.turns += 1
        next_state(session)

        # After state transitions, print a guiding prompt once
        if session.turns in (1, 2, 6):  
            print(f"Krishnamurti: {state_intro(session.state)}\n")

if __name__ == "__main__":
    main()