from num2words import num2words

def number_to_indian_mix(num):
    words = num2words(num, lang='en_IN')
    # Capitalize important Indian units
    words = (words.replace("crore", "Crore")
                   .replace("lakh", "Lakh")
                   .replace("thousand", "Thousand"))
    # Replace number words with digits where needed
    # e.g., "two crore" -> "2 Crore"
    mapping = {
        "one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
        "six": "6", "seven": "7", "eight": "8", "nine": "9",
        "ten": "10", "twenty": "20", "thirty": "30", "forty": "40",
        "fifty": "50", "sixty": "60", "seventy": "70", "eighty": "80", "ninety": "90"
    }
    for word, digit in mapping.items():
        words = words.replace(word, digit)
    return words
