import json

class MusicLibrary:
    """Класс для управления музыкальной библиотекой."""

    def __init__(self, filename="music_data.json"):
        self.filename = filename
        self.music_data = self.load_data()

    def add_album(self):
        """Добавляет альбом в словарь."""
        artist = input("Введите имя исполнителя: ")
        album = input("Введите название альбома: ")
        if artist in self.music_data:
            self.music_data[artist].append(album)
        else:
            self.music_data[artist] = [album]
        print(f"Альбом '{album}' добавлен для исполнителя '{artist}'.")

    def remove_data(self):
        """Удаляет данные из словаря."""
        artist = input("Введите имя исполнителя для удаления данных: ")
        if artist in self.music_data:
            del self.music_data[artist]
            print(f"Данные об исполнителе '{artist}' удалены.")
        else:
            print(f"Исполнитель '{artist}' не найден.")

    def search_data(self):
        """Ищет данные в словаре."""
        artist = input("Введите имя исполнителя для поиска: ")
        if artist in self.music_data:
            print(f"Альбомы исполнителя '{artist}': {self.music_data[artist]}")
        else:
            print(f"Исполнитель '{artist}' не найден.")

    def edit_data(self):
        """Редактирует данные в словаре."""
        artist = input("Введите имя исполнителя для редактирования: ")
        if artist in self.music_data:
            print(f"Текущие альбомы: {self.music_data[artist]}")
            new_albums = input("Введите новые названия альбомов через запятую: ").split(",")
            self.music_data[artist] = [album.strip() for album in new_albums]
            print(f"Данные об исполнителе '{artist}' обновлены.")
        else:
            print(f"Исполнитель '{artist}' не найден.")

    def save_data(self):
        """Сохраняет данные в JSON файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.music_data, f, indent=4)
        print(f"Данные сохранены в файл '{self.filename}'.")

    def load_data(self):
        """Загружает данные из JSON файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"Данные загружены из файла '{self.filename}'.")
            return data
        except FileNotFoundError:
            print(f"Файл '{self.filename}' не найден.")
            return {}


if __name__ == "__main__":
    library = MusicLibrary()

    while True:
        print("\nВыберите действие:")
        print("1. Добавить альбом")
        print("2. Удалить данные об исполнителе")
        print("3. Найти альбомы исполнителя")
        print("4. Редактировать данные об исполнителе")
        print("5. Сохранить данные")
        print("6. Загрузить данные")
        print("7. Выйти")

        choice = input("Ваш выбор: ")

        if choice == '1':
            library.add_album()
        elif choice == '2':
            library.remove_data()
        elif choice == '3':
            library.search_data()
        elif choice == '4':
            library.edit_data()
        elif choice == '5':
            library.save_data()
        elif choice == '6':
            library.load_data()
        elif choice == '7':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

