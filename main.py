def main():
    read_file()
    print_contents(read_file())
    count_words(read_file())
    count_chars(read_file())
    print_report(path, count_words(read_file()), count_chars(read_file()))

path = 'books/frankenstein.txt'

def read_file():
    with open(path) as f:
        file_contents = f.read()
        return file_contents 

def print_contents(file):
    print(file)

def count_words(file):
    words = file.split()
    count = len(words)
    return count

def count_chars(file):
    char_count = {}
    for char in file:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def print_report(file_path, word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)

    for char_count in char_list:
        letter = char_count["char"]
        num = char_count["num"]
        print(f"The '{letter}' character was found {num} times")
    print("\n--- End Report ---")

main()




        
