import json

with open('newsafr.json', encoding ='utf-8') as top_news:
    json_top_news = json.load(top_news)

    def json_news():
        len_words = []
        for news in json_top_news['rss']['channel']['items']:
            news = news['description'].lower()
            for word in news.split():
                if len(word) > 6:
                    len_words.append(word)

        word_dict = {}
        for i in len_words:
            word_dict_1 = {i: len_words.count(i)}
            word_dict.update(word_dict_1)

        list_word_dict = list(word_dict.items())
        list_word_dict.sort(key=lambda i: i[1])
        list_word_dict.reverse()

        print('Топ 10 самых часто встречающихся в новостях слов и количество повторений:')

        for i in range(10):
            print(f'{list_word_dict[i][0].capitalize()} - {list_word_dict[i][1]}')
    json_news()