import requests
from bs4 import BeautifulSoup
import warnings


# Установите заголовки, как указано в вашем запросе
headers = {
    "Accept": "*/*",
    "Accept-Language": "ru,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "has_js=1",
    "Origin": "https://www.atsenergo.ru",
    "Referer": "https://www.atsenergo.ru/results/market/fact_region",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
}

# Создаем словарь для хранения названий файлов и ссылок
file_links = {}
# Создаем список с разными значениями id (сочетание из месяца и года)
id_list = ["102021", "112021", "122021", "012022", "022022", "032022", "042022", "052022", "062022", "072022", "082022", "092022", "102022", "112022", "122022", "012023", "022023", "032023", "042023", "052023", "062023", "062023", "072023", "082023", "092023", "102023", "112023"]
# Установим URL и данные запроса
url = "https://www.atsenergo.ru/js-data"


# Игнорирование предупреждения о незащищенных HTTPS-запросах
# Игнорирование предупреждения о незащищенных HTTPS-запросах
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    for id in id_list:

        data = {
            "data": "results/market/fact_region",
            "id": id,
        }

        # Выполнение POST-запрос с использованием библиотеки requests
        response = requests.post(url, headers=headers, data=data, verify=False)

        # Использование BeautifulSoup для разбора HTML-кода ответа
        soup = BeautifulSoup(response.text, 'html.parser')

        # Поиск всех элементов <a> с атрибутом href, начинающимся с "https://www.atsenergo.ru/dload/fact_region/"
        for link in soup.find_all('a', href=True,
                                  attrs={'href': lambda x: x.startswith('https://www.atsenergo.ru/dload/fact_region/')}):
            # Получаем текст (название файла) и значение атрибута href (ссылку на файл) для каждой ссылки
            file_name = link.get_text()
            file_url = link['href']
            if file_name == 'Свердловская область':
                # Добавьте их в словарь с учетом переменной id
                file_links[f"{id}_{file_name}"] = file_url
