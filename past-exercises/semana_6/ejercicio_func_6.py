def sort_alphabetically(string_with_hyphen): 

    new_list = string_with_hyphen.split('-')
    new_list.sort()
    separator = "-"
    new_string = separator.join(new_list)
    return new_string


sorted_words = sort_alphabetically("python-variable-funcion-computadora-monitor")
print(sorted_words)