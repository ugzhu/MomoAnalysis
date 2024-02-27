from wordcloud import WordCloud
import matplotlib.pyplot as plt


def generate_word_cloud(words, name):
    wc = WordCloud(
        font_path='./asset/font/SourceHanSerifK-Light.otf',
        background_color="white",
        width=1000,
        height=860
        )

    wc.generate_from_frequencies(words)
    wc.to_file(f'./out/wc_{name}.jpg')
