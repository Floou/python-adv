def my_decorator(func):
    def wrapper(str_len):
        print(f"Длина строки = {func(len(str_len))} символов")
        return func(str_len)

    return wrapper


@my_decorator
def my_function_text(text_str):
    return text_str


sample_1 = 'Три девицы под окном. Пряли поздно вечерком.'
sample_1 = my_function_text(sample_1)
print(sample_1)

sample_2 = 'К морю князь - а лебедь там Уж гуляет по волнам.'
sample_2 = my_function_text(sample_2)
print(sample_2)
