import os
import pandas as pd

# Создаем пустой DataFrame, который будет содержать объединенные данные
merged_data = pd.DataFrame()

# Укажите путь к папке, содержащей файлы XLS
folder_path = 'C:\\Users\\orion\\PycharmProjects\\parser\\file'

# Проходим по всем файлам в указанной папке
for filename in os.listdir(folder_path):
    if filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)

        # Читаем данные из текущего файла XLS
        data = pd.read_excel(file_path)

        # Объединяем данные с предыдущими
        merged_data = pd.concat([merged_data, data], ignore_index=True)

# Определяем путь для сохранения объединенных данных в той же папке
output_file_path = os.path.join(folder_path, 'concat_data.xlsx')

# Сохраняем объединенные данные в новом файле XLSX
merged_data.to_excel(output_file_path, index=False)

print(f'Объединенные данные сохранены в файл {output_file_path}')