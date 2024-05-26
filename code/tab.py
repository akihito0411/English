import functools
import json

# 各関数呼び出しのオプションを保存する辞書
options_log = {}
call_count = {}

def log_options(func):
    @functools.wraps(func)  # functoolsモジュールのwrapsを使用、関数の引継ぎ（内容すべて）
    def wrapper_log_options(*args, **kwargs):
        # 関数に渡されたオプションをログに記録する
        if func.__name__ not in call_count:
            call_count[func.__name__] = 0
        call_count[func.__name__] += 1
        
        options_log[func.__name__] = {
            'args': args,                           #ここで使われるのはデータベースよって宣言はa = {}でする
            'kwargs': kwargs,
            'call_count': call_count[func.__name__]
        }
        return func(*args, **kwargs)
    return wrapper_log_options

# デコレータの使用例を示す関数
@log_options
def example_function_1(option1, option2):
    # 何らかの計算
    return option1 + option2

@log_options
def example_function_2(option3, option4):
    # 何らかの計算
    return option3 * option4

def save_output(output, filename='output.json'):
    # 出力を保存する
    with open(filename, 'w') as f:
        json.dump({'output': output, 'options_log': options_log}, f, indent=4)

# 関数の使用例
result1 = example_function_1(1, 2)
result2 = example_function_2(3, 4)
example_function_1(1, 3)

# 結果とオプションログを保存する
save_output({'result1': result1, 'result2': result2})

# 結果の表示
#print(result1)
#print(result2)
