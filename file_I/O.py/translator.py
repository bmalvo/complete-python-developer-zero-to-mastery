from translate import Translator

translator = Translator(to_lang='ja')

try:
    with open('C:/Users/boydm/dev/complete-python-developer-zero-to-mastery/file_I/O.py/test.txt', mode='r', encoding='utf8') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('test-ja.txt', mode='w', encoding='utf8') as my_file2:
            my_file2.write(translation)
        print(translation)
except FileNotFoundError as err:
    print('check your file path silly')
