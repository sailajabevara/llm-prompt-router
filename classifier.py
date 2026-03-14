
import re

def classify_intent(message: str):

    msg = message.lower()

    # Code related keywords
    code_keywords = [
        "python","code","bug","function","program","loop",
        "sql","query","sort","list","array"
    ]

    # Data related keywords
    data_keywords = [
        "average","mean","median","data","dataset",
        "statistics","pivot","numbers","chart"
    ]

    # Writing related keywords
    writing_keywords = [
        "rewrite",
        "sentence",
        "grammar",
        "paragraph",
        "writing",
        "professional",
        "verbose",
        "improve",
        "awkward"
    ]

    # Career related keywords
    career_keywords = [
        "career","job","interview","resume",
        "cover letter","promotion"
    ]

    # Check categories
    if any(word in msg for word in code_keywords):
        return {"intent": "code", "confidence": 0.9}

    elif any(word in msg for word in data_keywords):
        return {"intent": "data", "confidence": 0.9}

    elif any(word in msg for word in writing_keywords):
        return {"intent": "writing", "confidence": 0.9}

    elif any(word in msg for word in career_keywords):
        return {"intent": "career", "confidence": 0.9}

    else:
        return {"intent": "unclear", "confidence": 0.5}