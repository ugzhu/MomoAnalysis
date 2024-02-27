#!/usr/bin/python3

from load_text import *
from cut import * 
from sentiment import *
from word_cloud import *
from remove_stopwords import *
data = {
    'momo_note': {'text': get_momo_note_text(),},
    'all_note': {'text': get_all_note_text(),},
    'momo_comment': {'text': get_momo_comment_text(),},
    'all_comment': {'text': get_all_comment_text(),},
}

for item in data:
    data[item]['word_list'] = cut_text(data[item]['text'])
    data[item]['freq'] = find_word_frequency(data[item]['word_list'])
    remove_stopwords(data[item]['freq'])
    score = 0
    for word in data[item]['word_list']:
        score += get_senti_score(word)
    data[item]['avg_score'] = score / len(data[item]['word_list'])
    print(f"{item}: {data[item]['avg_score']}")
    # print(data[item]['freq'])
    generate_word_cloud(data[item]['freq'], item)









