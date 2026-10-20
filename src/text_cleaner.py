def clean_text(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())