from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from book import file_links


def download_files_with_selenium(file_links, download_dir):
    # Настройка опций для Chrome, чтобы файлы скачивались автоматически в указанную папку
    chrome_options = Options()

    prefs = {"download.default_directory": download_dir}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    # Инициализация драйвера
    driver = webdriver.Chrome(options=chrome_options)

    for file_name, file_url in file_links.items():
        try:
            # Переходим по ссылке
            driver.get(file_url)

            # Ждем некоторое время для загрузки страницы
            time.sleep(5)

            print(f"Файл {file_name} начал скачиваться.")
        except Exception as e:
            print(f"Произошла ошибка при скачивании файла {file_name}: {e}")
    print('Скачивание завершенно')
    driver.quit()


download_dir = 'C:\\Users\\orion\\PycharmProjects\\parser\\file'
dir_file = file_links
download_files_with_selenium(dir_file, download_dir)
