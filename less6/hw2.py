from datetime import time

def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=21)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную


    if dark_theme_enabled_by_user:
        print('Вы включили темную тему!')
        is_dark_theme = True
    elif dark_theme_enabled_by_user == False:
        print('Вы выключили темную тему')
    else:
        print('Вы ввели неподдерживаемое значение или не сделали выбор, темная тема работает по времени системы')
        if current_time >= time(hour=22) or current_time < time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True