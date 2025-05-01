# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = ''
    intermediate_result = open_browser.__name__ + ' ['+browser_name+']'
    for i in intermediate_result.title():
        if i == '_':
            actual_result += ' '
        else:
            actual_result += i

    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = ''
    intermediate_result = go_to_companyname_homepage.__name__
    for i in intermediate_result.title():
        if i == '_':
            actual_result += ' '
        else:
            actual_result += i
    actual_result += ' [' + page_url + ']'
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = ''
    intermediate_result = find_registration_button_on_login_page.__name__
    for i in intermediate_result.title():
        if i == '_':
            actual_result += ' '
        else:
            actual_result += i
    actual_result += ' [' + page_url + ', ' + button_text.title() + ']'
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"