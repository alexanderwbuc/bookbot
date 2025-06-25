def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char_dict):
    sorted_items = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)

    # Convert each pair into a single-entry dictionary
    sorted_list = [{char: count} for char, count in sorted_items]

    return sorted_list