def pig_latin(word: str) -> str:
    vowels = 'aeiuoAEIOU'
    is_capitalized = word[0].isupper()
    word_lower = word.lower()
    if word_lower[0] in vowels:
        result = word_lower + 'way'
    else:
        result = word_lower[1:] + word_lower[0] + 'ay'
    
    if is_capitalized:
        result = result.capitalize()

    return result
       

print(pig_latin("Pnime"))
