import xml.etree.ElementTree as ET

tree = ET.parse('newsafr.xml')
root = tree.getroot()

def xml_news():
    news_text_list = []
    xml_items = root.findall('channel/item')
    for item in xml_items:
        item = item.find('description').text.lower()
        news_text_list += item.split()

    len_words = []
    for word in news_text_list:
        if len(word) > 6:
            len_words.append(word)

    word_dict = {}
    for i in len_words:
        word_dict_new = {i: len_words.count(i)}
        word_dict.update(word_dict_new)

    list_word_dict = list(word_dict.items())
    list_word_dict.sort(key=lambda i: i[1])
    list_word_dict.reverse()

    print('Топ 10 самых часто встречающихся в новостях слов и количество повторений:')

    for i in range(10):
        print(f'{list_word_dict[i][0].capitalize()} - {list_word_dict[i][1]}')
xml_news()