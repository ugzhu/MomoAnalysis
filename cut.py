import jieba
 
def cut_text(text):
    word_list = list(jieba.cut(text, cut_all=False))
    return word_list

def find_word_frequency(word_list) -> tuple:
    freq = {}

    for word in word_list:
        freq[word] = freq.get(word, 0) + 1
    
    return freq
