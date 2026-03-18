def format_text(text):
    formatted_text = text.strip().replace("\n", " ")
    return formatted_text

def calculate_confidence(confidence_scores):
    avg_confidence = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
    return avg_confidence
