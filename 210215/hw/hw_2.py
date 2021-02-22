def my_decorator(func):
    def wrapper(str_len):
        print(str_len)
        return f"Длинная стороки = {func(len(str_len))} символов"

    return wrapper


@my_decorator
def my_functian_text(text_str):
    return text_str


sample_1 = 'Три девицы под окном. Пряли поздно вечерком.'
sample_2 = my_functian_text(sample_1)
print(sample_2)

sample_3 = 'К морю князь - а лебедь там Уж гуляет по волнам.'
sample_4 = my_functian_text(sample_3)
print(sample_4)
