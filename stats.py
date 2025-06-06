def word_counter(text):
    return len(text.split())


def char_counter(text):
    stats_dict = {}
    clean_text = text.lower()
    for c in clean_text:
        if c not in stats_dict:
            stats_dict[c] = clean_text.count(c)
    return stats_dict

test = {'t': 29493, 'h': 19176, 'e': 44538, ' ': 70480, 'p': 5952, 'r': 20079, 'o': 24494, 'j': 497, 'c': 9011, 'g': 5795, 'u': 10111, 'n': 23643, 'b': 4868, 'k': 1661, 'f': 8451, 'a': 25894, 's': 20360, 'i': 23927, ';': 1350, ',': 5962, 'm': 10206, 'd': 16318, '\n': 7630, 'y': 7756, 'w': 7450, 'l': 12306, 'v': 3737, '.': 3121, '-': 173, ':': 211, '2': 19, '3': 15, '0': 18, '1': 91, '[': 2, '#': 1, '4': 12, '5': 12, ']': 2, '&': 5, '8': 24, '/': 8, '*': 97, '’': 144, 'x': 691, '_': 124, 'q': 325, '?': 208, '—': 123, '6': 9, 'z': 235, '(': 35, ')': 35, '7': 18, 'æ': 28, '!': 201, '“': 506, '”': 316, '9': 9, 'ë': 2, '‘': 43, 'â': 8, 'ê': 7, 'ô': 1, '™': 57, '•': 4, '%': 1, '$': 2}

def sort_dict(unsorted_dict):
    data = []
    for k in unsorted_dict:
        if k.isalpha():
            entry = {}
            entry["char"] = k
            entry["num"] = unsorted_dict[k]
            data.append(entry)
    
    # sorted_dict = dict(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))
    def sort_on(dict):
        return dict["num"]
    data.sort(reverse=True, key=sort_on)

    return data
                

# print(sort_dict(test))           

