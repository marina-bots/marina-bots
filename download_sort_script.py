import os
import requests
from urllib.parse import urlparse

# Папка для скачанных файлов
DOWNLOAD_FOLDER = "downloads"

# Правила сортировки: расширение -> папка
SORT_RULES = {
    ".jpg": "images",
    ".jpeg": "images",
    ".png": "images",
    ".pdf": "pdfs",
    ".txt": "texts",
    ".csv": "csv_files",
    ".xlsx": "excel_files",
}

def download_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Получаем имя файла из URL
        path = urlparse(url).path
        filename = os.path.basename(path)
        if not filename:
            filename = "downloaded_file"
        
        # Создаём папку downloads, если нет
        os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
        
        # Полный путь сохранения
        filepath = os.path.join(DOWNLOAD_FOLDER, filename)
        
        with open(filepath, "wb") as f:
            f.write(response.content)
        
        print(f"Файл {filename} скачан")
        return filepath
    except Exception as e:
        print(f"Ошибка при скачивании {url}: {e}")
        return None

def sort_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    folder = SORT_RULES.get(ext)
    if folder:
        target_folder = os.path.join(DOWNLOAD_FOLDER, folder)
        os.makedirs(target_folder, exist_ok=True)
        
        new_path = os.path.join(target_folder, os.path.basename(filepath))
        os.rename(filepath, new_path)
        print(f"Файл {os.path.basename(filepath)} перемещён в {folder}")

def main():
    # Читаем ссылки из файла links.txt
    with open("links.txt", "r") as file:
        urls = [line.strip() for line in file if line.strip()]
    
    for url in urls:
        downloaded_path = download_file(url)
        if downloaded_path:
            sort_file(downloaded_path)

if __name__ == "__main__":
    main()
