from prime_generator import PrimeGenerator, random
import os

class RSA:
    def generate_keys(key_length):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def compute_lcm(a, b):
            if a == 0 or b == 0:
                return 0
            else:
                return abs(a * b) // gcd(a, b)

        def extended_gcd(a, b):
            if a == 0:
                return b, 0, 1
            else:
                g, x, y = extended_gcd(b % a, a)
                return g, y - (b // a) * x, x

        def mod_inverse(a, m):
            g, x, y = extended_gcd(a, m)
            if g != 1:
                raise ValueError(f"The modular inverse does not exist for {a} modulo {m}")
            else:
                return x % m
    
        generator = PrimeGenerator()
        p = generator(key_length)
        q = generator(key_length)
        n = p * q
        l = compute_lcm(p-1, q-1)
        e = random.randrange(2, l - 1)
        searching = True
        while searching:
            try:
                d = mod_inverse(e, l)
                searching = False
            except:
                e = random.randrange(2, l - 1) 
        return (n, e),(n, d)
    
    def int_to_bytes(integer):
        return integer.to_bytes((integer.bit_length() + 7) // 8, 'big')
    
    def bytes_to_int(bytes_obj):
        return int.from_bytes(bytes_obj, byteorder = 'big')
    
    def base10_to_other_base(number, base):
        result = []        
        while number > 0:
            remainder = number % base
            result.append(remainder)
            number //= 256
        return result[::-1]
    
    def encrypt_file(input_path, output_path, public_key, block_size):
        n, e = public_key
        with open(input_path, "r") as input_file:
            with open(output_path, "bw") as output_file:
                output_file.write(block_size.to_bytes(2, 'big'))
                while True:
                    input_chunk = input_file.read(block_size)
                    if not input_chunk:
                        break
                    input_cypher = 0
                    power = 0
                    for symbol in input_chunk:
                        input_cypher += ord(symbol) * pow(256, power)
                        power += 1
                    byte_number = RSA.int_to_bytes(pow(input_cypher, e, n))
                    size = (len(byte_number)).to_bytes(2, 'big')
                    result = size + byte_number
                    output_file.write(result)

    def decrypt_file(input_path, output_path, private_key):
        n, d = private_key

        with open(input_path, "rb") as input_file:
            with open(output_path, "w") as output_file:
                block_size = RSA.bytes_to_int(input_file.read(2))
                while True:
                    size = input_file.read(2)
                    if not size:
                        break
                    size = RSA.bytes_to_int(size)
                    encrypted_symbol = RSA.bytes_to_int(input_file.read(size))
                    # Decrypt each byte in the chunk
                    decrypted_symbol = pow(encrypted_symbol, d, n)
                    symbols = RSA.base10_to_other_base(decrypted_symbol, 256)[::-1]
                    output_string = [chr(symbol) for symbol in symbols]
                    # Convert the list of integers to bytes and write to the output file
                    output_file.write("".join(output_string))
   


def main():
    state = 0
    runing = True
    public_key = None
    while runing:
        if (state == 0):
            print("1. Завантажити ключ\n2. Створити ключ\n3. Exit")
            general_input = input()
            if(general_input == '1'):
                state = 4
            elif (general_input == '2'):
                state = 1
            elif (general_input == '3'):
                runing = False
            else:
                print("Wrong input")
        elif (state == 1):
            try:
                length = int(input("Введіть довжину бази ключа шифрування : "))
                public_key, private_key = RSA.generate_keys(length)
                print(f"Публічний ключ : {public_key}")
                print(f"Приватний ключ : {private_key}")
                with open('public_key.key', 'w') as public_key_file:
                    e, n = public_key
                    public_key_file.write(f"{str(e)} {str(n)}")
                with open('private_key.key', 'w') as private_key_file:
                    d, n = private_key
                    private_key_file.write(f"{str(d)} {str(n)}")
                state = 5
            except:
                print("Wrong format, please write number")
        elif (state == 2):
            try:
                input_file_path = input("Введіть шлях до вхідного файлу: ")
                if (not os.path.isfile(input_file_path)):
                    print("File not exist")
                output_file_path = input("Введіть шлях до куди вставити закодований файл: ")
            except:
                print("Error happened try again")
            block_size = 5
            RSA.encrypt_file(input_file_path, output_file_path, public_key, block_size)
            state = 5
        elif (state == 3):
            try:
                input_file_path = input("Введіть шлях до закодованого файлу: ")
                if (not os.path.isfile(input_file_path)):
                    print("File not exist")
                output_file_path = input("Введіть шлях до куди вставити файл: ")
            except:
                print("Error happened try again")
            RSA.decrypt_file(input_file_path, output_file_path, private_key)
            state = 5
        elif (state == 4):
            with open('public_key.key', 'r') as key_file:
                key_string = key_file.read().split(' ')
                e = int(key_string[0])
                n = int(key_string[1])
                public_key = (e, n)
            with open('private_key.key', 'r') as key_file:
                key_string = key_file.read().split(' ')
                d = int(key_string[0])
                n = int(key_string[1])
                private_key = (d, n)
            state = 5
        elif (state == 5):
            print("1. Encode file\n2. Decode file\n3. Drop keys\n4. Exit")
            general_input = input()
            if (general_input == '1'):
                state = 2
            elif (general_input == '2'):
                state = 3
            elif (general_input == '3'):
                state = 0
            elif (general_input == '4'):
                runing = False
            else:
                print("Wrong input")
if (__name__ == "__main__"):
    main()