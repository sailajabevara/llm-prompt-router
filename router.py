
from prompts import SYSTEM_PROMPTS

def route_and_respond(message, intent_data):

    intent = intent_data["intent"]

    if intent == "unclear":
        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"

    elif intent == "code":
        return "You can sort a list in Python using sorted() or list.sort(). Example: my_list.sort()"

    elif intent == "data":
        numbers = [12, 45, 23, 67, 34]
        avg = sum(numbers) / len(numbers)
        return f"The average of the numbers is {avg}. A bar chart would help visualize this."

    elif intent == "writing":
        return "Your writing may contain unnecessary words. Try simplifying sentences and avoiding passive voice."

    elif intent == "career":
        return "Can you tell me your experience level and the job role you are targeting so I can give better advice?"

    else:
        return "I'm not sure what you need. Are you asking for help with coding, data analysis, writing, or career advice?"