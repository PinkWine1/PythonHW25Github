def api_util_foo(param: str):
    print("Функция утилита api_util_foo")

print(__name__)
if __name__ == "__main__":
    print("Проверка работы api_util_foo")
    api_util_foo("привет")