def main():
    read_file()
    print_contents(read_file())
    count_words(read_file())
    count_chars(read_file())

def read_file():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        return file_contents 

def print_contents(file):
    print(file)

def count_words(file):
    words = file.split()
    count = len(words)
    print(f"Number of words: {count}")

def count_chars(file):
    char_count = {}
    count = 0
    for char in file:
        char = char.lower()
        if char not in char_count:
            count = 1
            char_count[char] = count
        else:
            count += 1
            char_count[char] = count
    print(f"Number of characters: {char_count}")


main()




        
