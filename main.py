import sys
from stats import get_word_count, get_character_count, create_report

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(file_path: str):
    text = get_book_text(f"./{file_path}")
    count = get_word_count(text)
    character_count = get_character_count(text)
    create_report(count, character_count, file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])