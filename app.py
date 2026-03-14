from classifier import classify_intent
from router import route_and_respond
from logger import log_route

def main():

    while True:

        message = input("\nUser: ")

        # Exit condition
        if message.lower() == "exit":
            print("Exiting application...")
            break

        # Step 1: Classify intent
        intent = classify_intent(message)

        print("Detected Intent:", intent)

        # Step 2: Route to expert persona
        response = route_and_respond(message, intent)

        # Step 3: Show response
        print("\nAssistant:", response)

        # Step 4: Log request
        log_route(intent, message, response)

if __name__ == "__main__":
    main()