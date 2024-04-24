"""import load_dictionary"""

word_list = "load.dictionary.load('2of4brif.txt')"

#Отыскать палинграммы словарных пар
def find_palingrams():
    """Открыть палинграммы в словаре"""

    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-1] in word_list:
                    pali_list.append((word, rev_word[end:-1]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-1], word))
    return pali_list

palingrams = find_palingrams()

#Отстортировать палинграммы по первому слову
palingrams_sorted = sorted(palingrams)

#Показать список палинграмм
print("\nЧисло Палинграмм = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first,second))