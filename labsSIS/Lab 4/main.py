from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def read_file(path):
    with open(path, 'r') as file:
        return file.read()
    
def write_file(path, data):
    with open(path, 'w') as file:
        file.write(data)

def encrypt(key, path_in, path_out):
    with open(path_in, 'r') as file_input:
        with open(path_out, 'w') as file_output:
            des = DES.new(key, DES.MODE_ECB)
            data = file_input.read()
            data = bytes(data, encoding='utf-8')
            data = pad(data, len(key))
            data = des.encrypt(data)
            data = base64.b64encode(data).decode('utf-8')
            file_output.write(data)

def decrypt(key, path_in, path_out):
    with open(path_in, 'r') as file_input:
        with open(path_out, 'w') as file_output:
            cipher = DES.new(key, DES.MODE_ECB)
            data = file_input.read()
            data = bytes(data, encoding='utf-8')
            data = base64.b64decode(data)
            data = cipher.decrypt(data)
            try:
                data = unpad(data, len(key))
            except:
                print("Помилка при декодуванні файлу.")
                return
            data = str(data, encoding='utf-8')
            file_output.write(data)

def signature(key, text):
    des = DES.new(key, DES.MODE_CBC)
    text = bytes(text, encoding='utf-8')
    text = pad(text, len(key))
    data = des.encrypt(text)
    data = base64.b64encode(data).decode('utf-8')
    print(f'Signature: {data}')


if __name__ == '__main__':
    runing = True
    while runing:
        print('1. Сігнатура')
        print('2. Кодування файлу')
        print('3. Декодування файлу')
        print('4. Вихід')
        menu_choice = input('Вибір: ')
        
        if menu_choice == '1':
            key = bytes(input('Ключ: '), encoding='utf-8')
            text = input('Текст: ')
            signature(key, text)
        elif menu_choice == '2':
            input_path = input('Вхідний файл: ')
            output_path = input('Вихідний файл: ')
            key = bytes(input('Ключ: '), encoding='utf-8')
            if len(key) != 8:
                print('Довжина ключа повинна бути 8.')
                continue
            encrypt(key, input_path, output_path)
        elif menu_choice == '3':
            input_path = input('Вхідний файл: ')
            output_path = input('Вихідний файл: ')
            key = bytes(input('Ключ: '), encoding='utf-8')
            if len(key) != 8:
                print('Довжина ключа повинна бути 8.')
                continue
            decrypt(key, input_path, output_path)
        elif (menu_choice == '4'):
            break
        else:
            print('Wrong input. Try again.')