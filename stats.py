def count_words(text: str):
    return len(text.split())

def count_symbols(text: str):
    char_map = {}
    for char in text:
        char = char.lower()
        if char not in char_map:
            char_map[char] = 0
        char_map[char] += 1
    return char_map

def sorted_count_symbols(symbol_dict: dict[str, int]):
    dicts: list[dict[str, str|int]] = []
    for char in symbol_dict:
        count = symbol_dict[char]
        dicts.append({
            "char": char,
            "num": count
        })
    dicts.sort(reverse=True, key=lambda x: x["num"])
    return dicts