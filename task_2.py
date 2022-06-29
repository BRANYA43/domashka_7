"""Написати калькулятор температури.

    Користувач вводить число та тип температури (C, F, K - Цельсій, Фарренгейт, Кельвін відповідно)

    Програма має вивести температуру у трьох шкалах температур – Цельсій, Фарренгейт, Кельвін."""


def is_int(value: str) -> bool:
    try:
        if int(value):
            return True
    except ValueError:
        return False


def is_float(value: str) -> bool:
    try:
        if float(value):
            return True
    except ValueError:
        return False


def get_input_number_element_list(message: str, some_list: list) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
        if is_int(ret):
            if int(ret) >= len(some_list):
                print(f'Не має елемента з номером {ret}')
                ret = ''
    return int(ret)


def get_input_number_int_or_float(message: str) -> int | float:
    ret = ''
    while not is_int(ret) or not is_float(ret):
        ret = input(message)
        if is_int(ret) or ret == '0':
            return int(ret)
        elif is_float(ret):
            return float(ret)


def get_round_off_number(number: float) -> float:
    return number * 100 // 1 / 100


def get_celsius(number: int, scale: str) -> float:
    formulas = {
        'K': number - 273.15,
        'C': number,
        'F': (number - 32) / 1.8
    }
    return get_round_off_number(formulas[scale])


def get_fahrenheit(number: int, scale: str) -> float:
    formulas = {
        'K': number * 1.8 - 459.67,
        'C': number * 1.8 + 32,
        'F': number
    }
    return get_round_off_number(formulas[scale])


def get_kelvin(number: int, scale: str) -> float:
    formulas = {
        'K': number,
        'C': number + 273.15,
        'F': (number + 459.67) / 1.8
    }
    return get_round_off_number(formulas[scale])


def print_temperatures(number: int, scale: str):
    print(f'{get_kelvin(number, scale)} K')
    print(f'{get_celsius(number, scale)} C')
    print(f'{get_fahrenheit(number, scale)} F')


def print_numbered_list(some_list: list):
    for i, elem in enumerate(some_list):
        print(f'{i}. {elem}')


def main():
    scales = ['K', 'C', 'F']
    temperature = get_input_number_int_or_float('Введіть температуру: ')
    print_numbered_list(scales)
    choose_scale = get_input_number_element_list('Оберіть шкалу: ', scales)
    print_temperatures(temperature, scales[choose_scale])


if __name__ == '__main__':
    main()

