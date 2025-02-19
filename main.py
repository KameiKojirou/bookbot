def count_words(text):
    """Returns the number of words in the text."""
    return len(text.split())

def count_letters(text):
    """Returns a dictionary with letter frequency counts (only alphabetic characters)."""
    char_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()  # Normalize to lowercase
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def print_letter_count_report(filename):
    """Reads the file, processes letter frequencies, and prints a formatted report."""
    with open(filename, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    letter_count = count_letters(file_contents)

    # Convert dictionary to sorted list of tuples based on count (descending)
    sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)

    # Print report
    print(f"--- Begin report of {filename} ---")
    print(f"{word_count} words found in the document\n")

    for letter, count in sorted_letters:
        print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

# Run the function with the specified file
print_letter_count_report("books/frankenstein.txt")
