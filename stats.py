from collections import Counter

def get_word_count(text: str) -> int:
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def get_character_count(text: str) -> dict:
    lower_text = text.lower()
    character_counts = Counter(lower_text)
    return dict(character_counts)

def sort_on(items: dict):
    return items["num"]

def create_report(word_count: int, characters: dict, path: str):
    character_count_list = [{"name": key, "num": value} for key, value in characters.items()]
    sorted_character_count = sorted(character_count_list, key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character_count in sorted_character_count:
        if character_count["name"].isalpha():
            print(f"{character_count['name']}: {character_count['num']}")
    print("============= END ===============")