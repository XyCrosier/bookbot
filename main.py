def main():
    doc_path = choose_doc()
    report(doc_path)

def choose_doc():
    #hardcoded for now for testing.
    return "books/frankenstein.txt"

#returns the contents of a document
def read(doc_path):
    with open(doc_path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    l_text = text.lower()
    c_counts = {}
    for char in l_text:
        if char in c_counts:
            c_counts[char] += 1
        else:
            c_counts[char] = 1
    return c_counts

# Converts a dictionary into a list of dictionaries
def dict_to_list(dictionary, k_name, v_name):
    list = []
    for k in dictionary:
        list.append({ k_name : k, v_name : dictionary[k] })
    return list

# Converts a char/count dictionary into a sorted list of char/count dictionaries. If letters_only = true, discards non-alphabet characters.
def sort_count_alphabetically(c_counts, letters_only):
    c_count_list = dict_to_list(c_counts, "char", "count")

    if letters_only:
        purged_list = []
        for dict in c_count_list:
            if dict["char"].isalpha():
                purged_list.append(dict)
        c_count_list = purged_list

    # A function that takes a dictionary and returns the value of the "count" key
    # This is how the `.sort()` method knows how to sort the list of dictionaries
    def sort_on(dict):
        return dict["count"]   

    c_count_list.sort(reverse=True, key=sort_on)

    return c_count_list

def print_char_counts(text, letters_only):
    c_counts = sort_count_alphabetically(count_characters(text), letters_only)
    for dict in c_counts:
        char = dict["char"]
        count = dict["count"]
        print(f"The '{char}' character was found {count} times.")


def report(doc_path):
    text = read(doc_path)
    word_count = count_words(text)

    print(f"--- Begin report of {doc_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    print_char_counts(text, True)
    print("--- End report ---")

main()