def main(): 
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    report(count_words(file_contents), count_characters(get_specific_characters(file_contents), file_contents))

def count_words(str):
    return len(str.split())

def get_specific_characters(str):
    char_set = set()
    char_dict = {}

    for c in str.lower():
        char_set.add(c)

    for char in char_set:
        char_dict[char] = 0

    return char_dict

def count_characters(char_dict, str):
    for key in char_dict:
        for char in str:
            if key == char:
                char_dict[key] += 1
    return char_dict

def report(word_count, char_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")

    for key in char_dict:
        print(f"The {key} was found {char_dict[key]} times")



main()



