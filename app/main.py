from app.config import USE_MOCK_MODEL
from app.llm import mock_response

def main():
    print("Krishnamurti (CLI) — OCD-informed CBT/ERP support (not diagnosis).")
    print("Type /quit to exit.\n")

    while True:
        user = input("You: ").strip()
        if not user:
            continue
        if user.lower() == "/quit":
            print("Krishnamurti: Take care.")
            break

        if USE_MOCK_MODEL:
            assistant_text = mock_response(user)
        else:
            raise RuntimeError("Real LLM mode not enabled yet")

        print(f"\nKrishnamurti: {assistant_text}\n")

if __name__ == "__main__":
    main()