def count_words(text):
    
    return len(text.split())

def count_characters(text):
    text = text.lower()

    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char,0) + 1
    
    return char_count

def sort_on(item):

    return item["num"]

def generate_report(file_path, word_count, char_count):
    print(f" --- Begin report of {file_path} --- ")
    print(f"{word_count} words fount in the document\n")

    alphabetic_counts = [
        {"char": char, "num": count} for char, count in char_count.items() if char.isalpha()
    ]

    alphabetic_counts.sort(reverse=True, key=sort_on)

    for item in alphabetic_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")

def main():
    path_to_file = "books/frankenstein.txt"
    
    with open(path_to_file) as f:
        content = f.read()

    word_count = count_words(content)
    char_count = count_characters(content)

    generate_report(path_to_file, word_count, char_count)
    

if __name__ == "__main__":
    main()
