import requests
import csv


# 1
# Написать функцию, которая принимает в виде параметра целое число -
# количество цитат, и возвращает список не повторяющихся цитат. Если автор
# не указан - цитату не брать.
#
# 2
# Написать функцию, которая принимает результат предыдущей функции и
# сохраняет в csv файл. Имя файла сделать параметром по умолчанию.
# Заголовки csv файла: Author, Quote, URL. Перед сохранением в csv,
# записи отсортировать по автору (в алфавитном порядке).
def get_quotes(count):
    quote_dict_list = []
    i = 0
    url = "http://api.forismatic.com/api/1.0/"

    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"}
    while i != count:
        params["key"] = i
        r = requests.get(url, params=params)
        quote = r.json()
        quote_dict = {"Author": "",
                      "Quote": "",
                      "URL": ""}
        if len(quote["quoteAuthor"]) > 0:
            quote_dict["Author"] = quote["quoteAuthor"]
            quote_dict["Quote"] = quote["quoteText"]
            quote_dict["URL"] = quote["quoteLink"]
            quote_dict_list.append(quote_dict)
            i += 1
    return quote_dict_list


quotes = get_quotes(10)


def key_sorted_by_name(quote):
    return quote["Author"]


quotes = sorted(quotes, key=key_sorted_by_name)


def write_quotes_csv(filename, quotes):
    with open(filename, "w", encoding="utf-8") as csv_file:
        fieldnames = {"Author": "",
                      "Quote": "",
                      "URL": ""}
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
        writer.writeheader()
        writer.writerows(quotes)


write_quotes_csv("quotes.csv", quotes)
