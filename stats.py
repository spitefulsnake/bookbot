#Count the number of words in a string
def count_words(string):
    count = 0
    for i in string.split():
        count += 1
    return count


# Count the number of characters in a string
def count_chars(string):
    dictionary = {}

    for i in string.lower():
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary [i] = 1
    
    return dictionary



def report(dictionary):
    sorted_list = []

    for char, count in dictionary.items():
        sorted_list.append({"char": char, "num": count})
    
    def sort_on(d):
        return d["num"]

    sorted_list.sort(reverse = True, key = sort_on)

    return sorted_list
    

    
