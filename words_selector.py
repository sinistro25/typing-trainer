word_file = open("corpi/top10000.txt","r")
words = word_file.read().split("\n")

def words_by_letter(letter):
    filtered = []
    for word in words:
        if letter in word:
            filtered.append(word)
    return filtered


