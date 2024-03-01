def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    output = report(text)
    print(output)

def get_num_words(text):
    words = text.split()
    return len(words)

def find_char_amount(text):
    char_dict = {}
    for i in text:
        lowered = i.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def report(text):
    num_words = get_num_words(text)
    output = f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n"
    char_list = convert_to_alpha_list(find_char_amount(text))
    char_list.sort(reverse=True, key=sort_on)
    for i in char_list:
        output += f"\nThe '{i["char"]}' character was found {i["num"]} times"
    output += "\n--- End report ---"
    return output

def convert_to_alpha_list(dict):
    alpha_list = []
    for i in dict:
        if i.isalpha():
            alpha_list.append({"char": i, "num": dict[i]})
    return alpha_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()