from translate import Translator

try:
    with open('F:/Python/Practice/TestFolder/Name.txt', mode='r') as my_file:
        file_text = my_file.read()
        print(file_text)
        translator = Translator(to_lang='ja')
        translate_string = translator.translate(file_text)

        with open('F:/Python/Practice/TestFolder/Name-ja.txt', mode='') as my_file_translated:
            print(translate_string)
            my_file_translated.write(translate_string)


except FileNotFoundError as err:
    print('File Not Found')
    raise err
except IOError as err:
    print('Input/Output Error')
    raise err
