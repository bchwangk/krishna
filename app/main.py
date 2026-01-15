from app.config import USE_MOCK_MODEL
from app.router import SessionState, next_state
from app.prompt import state_intro
from app.vignettes import load_vignettes, pick_vignette
from app.llm import mock_response

def main():
    print("Krishnamurti (CLI) — OCD-informed CBT/ERP support (not diagnosis).")
    print("Type /quit to exit.\n")

    session = SessionState()
    vignettes = load_vignettes()

    pending_intro_text = state_intro(session.state)
    print(f"Krishnamurti ({session.state}): {pending_intro_text}\n")
    pending_intro_text = None

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() == "/quit":
            print("Krishnamurti: Take care.")
            break

        if session.state == "GOAL" and session.goal is None:
            session.goal = user

        if session.vignette_id is None:
            v = pick_vignette(user, vignettes)
            if v:
                session.vignette_id = v["id"]

        vignette = None
        if session.vignette_id:
            vignette = next((x for x in vignettes if x["id"] == session.vignette_id), None)

        if pending_intro_text:
            print(f"\nKrishnamurti ({session.state}): {pending_intro_text}\n")
            pending_intro_text = None
            continue  # wait for next user input

        if USE_MOCK_MODEL:
            assistant_text = mock_response(user, session.state, vignette, session.goal)
        else:
            raise RuntimeError("Real LLM mode not enabled yet")

        print(f"\nKrishnamurti ({session.state}): {assistant_text}\n")

        session.turns += 1
        prev_state = session.state
        next_state(session)

        if session.state != prev_state:
            pending_intro_text = state_intro(session.state)

if __name__ == "__main__":
    main()
