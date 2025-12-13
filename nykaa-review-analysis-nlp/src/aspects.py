ASPECTS = {
    "quality": ["quality", "smooth", "texture"],
    "price": ["price", "expensive", "cheap"],
    "packaging": ["packaging", "bottle"],
    "fragrance": ["fragrance", "smell"]
}

def extract_aspects(text):
    return [a for a, kws in ASPECTS.items() if any(k in text for k in kws)]
