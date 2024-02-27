import os
from pathlib import Path

def load_stopwords():
    stopwords = set()
    stpwd_docs = [
        'baidu_stopwords.txt', # 中文停用词表
        'cn_stopwords.txt', # 哈工大停用词表
        'hit_stopwords.txt', # 百度停用词表
        'scu_stopwords.txt' # 四川大学机器智能实验室停用词库
        ]

    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for doc in stpwd_docs:
        # Join the script directory with the specified path
        doc_path = os.path.join(script_dir,  f"asset/stopwords/{doc}")
        with open(doc_path, 'r') as file:
            for line in file:
                # Strip newline and whitespace from the line before adding to the set
                stopwords.add(line.strip())

    return stopwords

    
def remove_stopwords(freq):
    stopwords = load_stopwords()
    for word in list(freq.keys()):
        if word in stopwords:
            pop = freq.pop(word)