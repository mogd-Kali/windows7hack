# 28.10.2024, 15:00 (MCK)
# Creator - Godilksq

import os
import time
import random

def gradient_text(text):
    result = ""
    colors = [(0, 0, 255), (50, 50, 255), (100, 100, 255), (150, 150, 255), (200, 200, 255), (255, 255, 255)]
    for i, char in enumerate(text):
        color_index = int((i / len(text)) * len(colors))
        r, g, b = colors[color_index]
        result += f'\033[38;2;{r};{g};{b}m{char}'
    return result + '\033[0m'

print(gradient_text(' '))
os.system("clear")

time.sleep(1)
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print(gradient_text('                                             ') + gradient_text('╭───────────────────────╮'))
print(gradient_text('                                             ') + gradient_text('│Инициализация программы│'))
print(gradient_text('                                             ') + gradient_text('╰───────────────────────╯'))
time.sleep(0.5)
import requests
import sys
import json
import csv
import hashlib
import keyboard
from fake_useragent import UserAgent
import smtplib
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_phone_number():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email


def generate_phone_number1():
    country_codes = ['+7', '+380', '+375']

    country_code = random.choice(country_codes)

    phone_number = ''.join(random.choices('0123456789', k=10))

    formatted_phone_number = f'{country_code}{phone_number}'

    return formatted_phone_number

def generate_random_email1():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]

    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(domains)

    email = f"{username}@{domain}"

    return email

def send_email(receiver, sender_email, sender_password, subject, body):
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.mail.ru', 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver, msg.as_string())
            time.sleep(3)
            server.quit()
            return True
        except Exception as e:
            return False

def send_complaint(username, telegram_id, number, email, repeats, complaint_choice, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    complaints_sent = 0

    if complaint_choice == "1":
        text = f"Здраствуйте, сидя на просторах сети телеграмм, я заметил пользователя который совершает спам-рассылки, мне и другим пользователям это очень не нравится.Его аккаунт: {username}, ID {telegram_id}.Огромная просьба разобраться с этим и заблокировать данного пользователя. Заранее спасибо."
    elif complaint_choice == "3":
        text = f"Здраствуйте. Аккаунт {username}, id {telegram_id}. Очень много и частно нарушает политику сервиса Телеграмм. А именно, оскорбляет, сливает личные данные юзеров. Продает различные услуги. Просьба разобраться и наказать данный аккаунт."
    elif complaint_choice == "4":
        text = f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {username}, а мой айди, если злоумышленник поменял юзернейм —  {telegram_id} . Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
    elif complaint_choice == "5":
        text = f'Аккаунт {username}, {telegram_id} приобрёл премиум в вашем сервисе чтобы обходить наказания за спам и совершает спам-рассылки в личные сообщения пользователям и в чаты. Прошу проверить информацию!'
    elif complaint_choice == "6":
        text = f'Добрый день поддержка Telegram! Аккаунт {username}, {telegram_id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!'


    payload = {'text': text, 'number': number, 'email': email}

    try:
        for _ in range(int(repeats)):
            response = requests.post(url, headers=headers, data=payload, proxies=proxies)
            if response.status_code == 200:
                complaints_sent += 1
                print(gradient_text(f" │ Жалоба отправлена От: {email} {number}"))
            else:
                print(" │ Не удалось отправить. code:", response.status_code)
    except Exception as e:
        print(" │ An error occurred:", str(e))

def find_person_by_fio(full_name, file_path):
            with open(file_path, 'r', 
           encoding='utf-8') as file:
                for line in file:
                    json_line = line.strip()
                    if json_line:
                        person = json.loads(json_line)
                        fio = f"{person['_source'].get('firstName', '')} {person['_source'].get('lastName', '')} {person['_source'].get('middleName', '')}".strip()
                        if fio == full_name:
                            return person['_source']

            return None
        
def find_person_by_fio1(full_name, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if len(parts) < 2:
                            continue
                        row_full_name = parts[1]
                        if row_full_name == full_name:
                            return  {
                                 "Номер телефона": parts[0],
                                 "ФИО": parts[1],
                                 "Дата рождения": parts[2],
                                 "Email": parts[3],
                                 "Город": parts[4],
                                 "Адрес": parts[5] if len(parts) > 5 else "Не указано"
                             }
            return None
            
def find_person_by_fio2(full_name, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if len(parts) > 2 and parts[2] == full_name:
                            return {
                                "Номер телефона": parts[0],
                                "Имя": parts[1],
                                "ФИО": parts[2],
                                "Email": parts[3] if len(parts) > 3 else "Не указано",
                                "Город": parts[4] if len(parts) > 4 else "Не указано",
                                "Улица": parts[5] if len(parts) > 5 else "Не указано",
                                "Дом": parts[6] if len(parts) > 6 else "Не указано",
                                "Подъезд": parts[7] if len(parts) > 7 else "Не указано"
                            }
            return None
def find_person_by_phone(phone_number, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    json_line = line.strip()
                    if json_line:
                        person = json.loads(json_line)
                        if person['_source'].get('parentPhone') == phone_number:
                            return {
                            "Имя": person.get("firstName"),
                            "Фамилия": person.get("lastName"),
                            "Отчество": person.get("middleName"),
                            "ФИО родителя": person.get("parentFIO"),
                            "Номер Родителя": person.get('parentPhone'),
                            "Регион": person.get("region"),
                            "Почта": person.get("email"),
                            "Страна": person.get("citizenship", {}).get("title", "null"),
                            "Хобби": person.get("hobby")
                            }

            return None

def find_person_by_phone1(phone_number, file_path):
            phone_number = phone_number.replace('+', '')

            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row_phone_number = row['phone'].replace('+', '')
                    if row['id'] == phone_number or row_phone_number == phone_number:
                        return row
                    
def find_person_by_phone2(phone_number, file_path):
            phone_number = phone_number.replace('+', '')

            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        row_phone_number = parts[0].replace('+', '')

                        if row_phone_number == phone_number:
                            return  {
                                 "Номер телефона": parts[0],
                                 "ФИО": parts[1],
                                 "Дата рождения": parts[2],
                                 "Email": parts[3],
                                 "Город": parts[4],
                                 "Адрес": parts[5] if len(parts) > 5 else "Не указано"
                             }
            return None
def find_person_by_phone3(phone_number, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if parts[0] == phone_number:
                            return {
                                "Номер телефона": parts[0],
                                "Имя": parts[1],
                                "ФИО": parts[2] if len(parts) > 2 else "Не указано",
                                "Email": parts[3] if len(parts) > 3 else "Не указано",
                                "Город": parts[4] if len(parts) > 4 else "Не указано",
                                "Улица": parts[5] if len(parts) > 5 else "Не указано",
                                "Дом": parts[6] if len(parts) > 6 else "Не указано",
                                "Подъезд": parts[7] if len(parts) > 7 else "Не указано"
                            }
            return None
def find_person_by_phone4(phone_number, file_path):
    phone_number = phone_number.replace('+', '')

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(';')
                row_phone_number = parts[0].replace('+', '')

                if row_phone_number == phone_number:
                    names = parts[1] if len(parts) > 1 else "Не указано"
                    if names != "NULL":
                        names = json.loads(names.replace("'", "\"")) 
                        names = names[0] if isinstance(names, list) and names else "Не указано"
                    else:
                        names = "Не указано"

                    additional_info = parts[2] if len(parts) > 2 else "Не указано"
                    if additional_info == "NULL":
                        additional_info = "Не указано"

                    return {
                        "Номер телефона": parts[0],
                        "Имя": names,
                        "Дополнительная информация": additional_info
                    }
    return None
def find_person_by_phone5(phone_number, database_file):
    phone_number = phone_number.replace('+', '').strip()  
    try:
        with open(database_file, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            next(reader)  
            for row in reader:
                if len(row) > 1 and row[0].strip() == phone_number:
                    return row[1] 
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return None  

def find_person_by_email(email, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    json_line = line.strip()
                    if json_line:
                        person = json.loads(json_line)
                        if person['_source'].get('email') == email:
                            return person['_source']

            return None
def find_person_by_email1(email, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if len(parts) < 4:
                            continue 
                        row_email = parts[3]
                        if row_email == email:
                            return  {
                                 "Номер телефона": parts[0],
                                 "ФИО": parts[1],
                                 "Дата рождения": parts[2],
                                 "Email": parts[3],
                                 "Город": parts[4],
                                 "Адрес": parts[5] if len(parts) > 5 else "Не указано"
                             }
            return None
def find_person_by_email2(email, file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        parts = line.split(';')
                        if len(parts) > 3 and parts[3] == email:
                            return {
                                "Номер телефона": parts[0],
                                "Имя": parts[1],
                                "ФИО": parts[2] if len(parts) > 2 else "Не указано",
                                "Email": parts[3] if len(parts) > 3 else "Не указано",
                                "Город": parts[4] if len(parts) > 4 else "Не указано",
                                "Улица": parts[5] if len(parts) > 5 else "Не указано",
                                "Дом": parts[6] if len(parts) > 6 else "Не указано",
                                "Подъезд": parts[7] if len(parts) > 7 else "Не указано"
                            }
            return None

def LoadFileEmail(file_path):
    senders = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    email, password = line.split(': ', 1)
                    senders[email] = password
                except ValueError:
                    print(f"Ошибка в строке: {line}. Пропускаем.")
    
    return senders

def LoadFileProxies(file_path):
    proxies = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
    
    return proxies

def compute_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_hashes(directory, output_file):
    with open(output_file, 'r') as in_file:
        stored_hashes = {line.split(": ")[0]: line.split(": ")[1].strip() for line in in_file.readlines()}

    all_files_intact = True
    for file_path in stored_hashes.keys():
        if os.path.exists(file_path):
            current_hash = compute_file_hash(file_path)
            if current_hash != stored_hashes[file_path]:
                print(gradient_text(f"Файл изменен: {file_path}"))
                all_files_intact = False
                time.sleep(1)
                os.system('cls')
                time.sleep(0.5)
                print('')
                print(gradient_text( '▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
                print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
                print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
                print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
                print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
                print('')
                print(gradient_text(' │ Закрываю...'))
                time.sleep(1)
                sys.exit(5)
        else:
            print(gradient_text(f"Файл отсутствует: {file_path}"))
            all_files_intact = False
            time.sleep(1)
            os.system('cls')
            time.sleep(0.5)
            print('')
            print(gradient_text( '▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
            print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
            print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
            print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
            print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
            print('')
            print(gradient_text(' │ Закрываю...'))
            time.sleep(1)
            sys.exit(5)
    if all_files_intact:
        print(gradient_text(" │ Все файлы целы."))

directory_to_scan = 'system'
output_file_name = 'hashes/hashes.txt'

verify_hashes(directory_to_scan, output_file_name)

time.sleep(1)

file1 = 'system/senders.txt'
file2 = 'system/proxies.txt'
senders = LoadFileEmail(file1)
proxies = LoadFileProxies(file2)

datebase1 = "system/datebase/База Артек.json"
datebase2 = "system/datebase/База EYEOFGOD.csv"
datebase3 = "system/datebase/База СпортМастер.txt"
datebase4 = "system/datebase/База Яндекс Еда.csv"
datebase5 = "system/datebase/База GetContact.csv"
datebase6 = "system/datebase/База Тегов.csv"

os.system('title BLOAD - Version 3.11.8 / Premuim')
static = True
snosst = True

time.sleep(1)
os.system("cls")

while static == True:
    print('')
    print(gradient_text('                             ') + gradient_text('▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
    print(gradient_text('                             ') + gradient_text('▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
    print(gradient_text('                             ') + gradient_text('▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
    print(gradient_text('                             ') + gradient_text('██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
    print(gradient_text('                             ') + gradient_text('·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
    print('')
    print(gradient_text("            Поиск                         Снос                      Другое"))
    print(gradient_text(" ╭─────────────────────────╮    ╭──────────────────────╮    ╭────────────────────╮"))
    print(gradient_text(" │ [1] - Поиск по ФИО      │    │ [11] - Снос Аккаунта │    │ [21] - О Программе │"))
    print(gradient_text(" │ [2] - Поиск по Телефону │    │ [12] - Снос Канала   │    │ [22] - Выйти       │"))
    print(gradient_text(" │ [3] - Поиск по Почте    │    │ [13] - Снос Бота     │    │                    │"))
    print(gradient_text(" ╰─────────────────────────╯    ╰──────────────────────╯    ╰────────────────────╯ " + " Version 3.11.8"))

    print('')

    inputs = int(input(gradient_text(' │ Пункт: ')))

    if inputs == 1:
        time.sleep(0.5)
        def main():
            full_name = input(gradient_text(' │ Введите ФИО: '))
            if not full_name:
                print(gradient_text(' │ В строке не достаточно данных'))
                return
            else:
                person_info = find_person_by_fio(full_name, datebase1)
                person_info_sportmaster = find_person_by_fio1(full_name, datebase3)
                person_info_YandenEda = find_person_by_fio2(full_name, datebase4)
                if person_info:
                    filtered_info = {
                        "Имя": person_info.get("firstName"),
                        "Фамилия": person_info.get("lastName"),
                        "Отчество": person_info.get("middleName"),
                        "ФИО родителя": person_info.get("parentFIO"),
                        "Номер Родителя": person_info.get('parentPhone'),
                        "Регион": person_info.get("region"),
                        "Почта": person_info.get("email"),
                        "Страна": person_info.get("citizenship", {}).get("title", "Не указана"),
                        "Хобби": person_info.get("hobby")
                    }
                    
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(json.dumps(filtered_info, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(" │ Человек с таким ФИО не найден."))
                if person_info_sportmaster:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(json.dumps(person_info_sportmaster, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(" │ Человек с таким ФИО не найден."))
                if person_info_YandenEda:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(json.dumps(person_info_YandenEda, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(" │ Человек с таким ФИО не найден."))

        if __name__ == "__main__":
            main()

        print('')
        print(gradient_text(' │ Что бы продолжить нажмите esc'))
        keyboard.wait('esc')
        os.system('cls')
        continue
    if inputs == 2:
        time.sleep(0.5)

        phone_number = input(gradient_text(" │ Введите номер телефона (+79999999999): "))

        def main():
            if not phone_number:
                print(gradient_text(' │ В строке не достаточно данных'))
                return
            else:
                person_info_artek = find_person_by_phone(phone_number, datebase1)
                person_info_eyeofgod = find_person_by_phone1(phone_number, datebase2)
                person_info_sportmaster = find_person_by_phone2(phone_number, datebase3)
                person_info_YandenEda = find_person_by_phone3(phone_number, datebase4)
                person_info_GetContact = find_person_by_phone4(phone_number, datebase5)
                person_info_Tager = find_person_by_phone5(phone_number, datebase6)
                if person_info_artek:
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(json.dumps(person_info_artek, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))

                if person_info_eyeofgod:
                    print(gradient_text(" │ Глаз бога:"))
                    print(gradient_text(f" │ ID: {person_info_eyeofgod['id']}"))
                    print(gradient_text(f" │ Телефон: {person_info_eyeofgod['phone']}"))
                    print(gradient_text(f" │ Имя пользователя: {person_info_eyeofgod['username']}"))
                    print(gradient_text(f" │ Имя: {person_info_eyeofgod['first_name']}"))
                    print(gradient_text(f" │ Фамилия: {person_info_eyeofgod['last_name']}"))
                else:
                    print(gradient_text(" │ Глаз бога:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))
                if person_info_sportmaster:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(json.dumps(person_info_sportmaster, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))
                if person_info_YandenEda:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(json.dumps(person_info_YandenEda, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))
                if person_info_GetContact:
                    print(gradient_text(" │ GetContact:"))
                    print(gradient_text(json.dumps(person_info_GetContact, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ GetContact:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))
                if person_info_Tager:
                    print(gradient_text(" │ Теги:"))
                    print(gradient_text(json.dumps(person_info_Tager, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Теги:"))
                    print(gradient_text(" │ Человек с таким номером не найден."))

        if __name__ == "__main__":
            main()

        print('')
        print(gradient_text(' │ Что бы продолжить нажмите esc'))
        keyboard.wait('esc')
        os.system('cls')
        continue
    if inputs == 3:
        time.sleep(0.5)
        def main():
            email = input(gradient_text(' │ Введите почту (godls@mail.ru, или другую почтовую систему): '))

            if not email:
                print(gradient_text(' │ В строке не достаточно данных'))
                return
            else:
                person_info_artec = find_person_by_email(email, datebase1)
                person_info_sportmaster = find_person_by_email1(email, datebase3)
                person_info_YandenEda = find_person_by_email2(email, datebase4)
                if person_info_artec:
                    filtered_info = {
                        "Имя": person_info_artec.get("firstName"),
                        "Фамилия": person_info_artec.get("lastName"),
                        "Отчество": person_info_artec.get("middleName"),
                        "ФИО родителя": person_info_artec.get("parentFIO"),
                        "Номер Родителя": person_info_artec.get('parentPhone'),
                        "Регион": person_info_artec.get("region"),
                        "Почта": person_info_artec.get("email"),
                        "Страна": person_info_artec.get("citizenship", {}).get("title", "Не указана"),
                        "Хобби": person_info_artec.get("hobby")
                    }
                    
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(json.dumps(filtered_info, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Артек:"))
                    print(gradient_text(" │ Человек с такое почтой не найден."))
                if person_info_sportmaster:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(json.dumps(person_info_sportmaster, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ СпортМастер:"))
                    print(gradient_text(" │ Человек с такое почтой не найден."))
                if person_info_YandenEda:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(json.dumps(person_info_YandenEda, ensure_ascii=False, indent=4)))
                else:
                    print(gradient_text(" │ Яндекс Еда:"))
                    print(gradient_text(" │ Человек с такое почтой не найден."))

        if __name__ == "__main__":
            main()
        print('')
        print(gradient_text(' │ Что бы продолжить нажмите esc'))
        keyboard.wait('esc')
        os.system('cls')
        continue
    receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
                 'stopca@telegram.org', 'security@telegram.org', 'recover@telegram.org',
                'sticker@telegram.org', 'support@telegram.org']
    sent_emails = 0
    if inputs == 11:
            os.system('cls')
            print('')
            print(gradient_text(' ▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
            print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
            print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
            print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
            print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
            print('')
            print(gradient_text(' ╭─────────────────────╮'))
            print(gradient_text(' │ [1] - Cпам          │'))
            print(gradient_text(' │ [2] - Личный Данные │'))
            print(gradient_text(' │ [3] - Троллинг      │'))
            print(gradient_text(' │ [4] - Снос Сессий   │'))
            print(gradient_text(' │ [5] - Премиум       │'))
            print(gradient_text(' │ [6] - Вирт          │'))
            print(gradient_text(' ╰─────────────────────╯'))
            print('')
            comp_choice = input(gradient_text(' │ Пункт: '))
            if comp_choice in ["1", "2", "3"]:
                username = input(gradient_text(" │ @Username: "))
                id = input(gradient_text(" │ Telegram ID: "))
                chat_link = input(gradient_text(" │ Ссылка на чат: "))
                violation_link = input(gradient_text(" │ Ссылка на нарушение: "))
                email = generate_random_email()
                number = generate_phone_number()
                comp_texts = {
                    "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                    "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                    "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
                }
                for sender_email, sender_password in senders.items():
                    for receiver in receivers:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                    violation_link=violation_link.strip())
                        send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграмм', comp_body)
                        send_complaint(username, id, number, email, 1, comp_choice, proxies)
                        print(gradient_text(f" │ Отправлено на {receiver} от {sender_email}"))
                        sent_emails += 99999
                        time.sleep(0.2)

            elif comp_choice == "4":
                username = input(gradient_text(" │ @Username: "))
                id = input(gradient_text(" │ Telegram id: "))
                comp_texts = {
                    "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
                }

                for sender_email, sender_password in senders.items():
                    for receiver in receivers:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip())
                        send_email(receiver, sender_email, sender_password, 'Я потерял свой аккаунт в телеграмм', comp_body)
                        send_complaint(username, id, number, email, 1, comp_choice, proxies)
                        print(gradient_text(f" │ Отправлено на {receiver} от {sender_email}"))
                        sent_emails += 99999
                        time.sleep(0.2)

            elif comp_choice in ["5", "6"]:
                username = input(gradient_text(" @Username: "))
                id = input(gradient_text(" Telegram Id: "))
                comp_texts = {
                    "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                    "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
                }

                for sender_email, sender_password in senders.items():
                    for receiver in receivers:
                        comp_text = comp_texts[comp_choice]
                        comp_body = comp_text.format(username=username.strip(), id=id.strip())
                        send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграмма', comp_body)
                        send_complaint(username, id, number, email, 1, comp_choice, proxies)
                        print(gradient_text(f" │ Отправлено на {receiver} от {sender_email}"))
                        sent_emails += 99999
                        time.sleep(0.2)


    if inputs == 12:
            os.system('cls')
            print(gradient_text(' ▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
            print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
            print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
            print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
            print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
            print('')
            print(gradient_text(' ╭────────────────────────╮'))
            print(gradient_text(' │ [1] - Живодерство      │'))
            print(gradient_text(' │ [2] - Личный Данные    │'))
            print(gradient_text(' │ [3] - Десткое          │'))
            print(gradient_text(' │ [4] - Прайс с услугами │'))
            print(gradient_text(' │ [5] - Терроризм        │'))
            print(gradient_text(' │ [6] - Взломан          │'))
            print(gradient_text(' ╰────────────────────────╯'))
            print('')
            ch_choice =input(gradient_text(" │ Пункт: "))

            if ch_choice in ["1", "2", "3", "4", "5", "6"]:
                channel_link = input(gradient_text(" │ Ссылка на канал: "))
                channel_violation = input(gradient_text(" │ Ссылка на нарушение: "))
                comp_texts = {
                    "1": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, ссылка на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                    "2": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, ссылка на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                    "3": f"Здравствуйте, уважаемая поддержка телеграмма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, ссылка на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                    "4": f"Здравствуйте, уважаемый модератор телеграмма, хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                    "5": f"Здрайствуйте, уважаемый модератор телеграмма. На нашей платформе я нашел канал, который распространяет террорестические угрозы и устраивает терракты. Ссылка на канал - {channel_link}, ссылка на нарушение - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                    "6": f"Здрайствуйте, уважаемый модератор телеграмма. На нашей платформе я нашел канал, который был взломан. Я это понял так как резко сменились интересы канала и он начал противоречить самому себе. Ссылка на канал - {channel_link}, ссылка на нарушение - {channel_violation}. Пожалуйста заблокируйте данный канал."
                }

                for sender_email, sender_password in senders.items():
                    for receiver in receivers:
                        comp_text = comp_texts[ch_choice]
                        comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                        send_email(receiver, sender_email, sender_password, 'Жалоба на телеграмм канал', comp_body)
                        print(gradient_text(f" │ Отправлено на {receiver} от {sender_email}"))
                        sent_emails += 99999
                        time.sleep(0.2)
    if inputs == 13:
        print(gradient_text(' ▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
        print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
        print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
        print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
        print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
        print('')
        print(gradient_text(' ╭────────────────────────╮'))
        print(gradient_text(' │ [1] - Глаз бога        │'))
        print(gradient_text(' ╰────────────────────────╯'))
        print('')
        bot_ch =input(gradient_text(" │ Пункт: "))

        if bot_ch == "1":
            bot_user = input(" │ @username: ")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(gradient_text(f"\nОтправлено на {receiver} от {sender_email}"))
                    sent_emails += 1
                    time.sleep(5)
    if inputs == 21:
        print('')
        time.sleep(0.5)
        print(gradient_text(' │ Эта программа разрабатывалась под заказ для телеграмм канала "Русский Консерватор" - https://t.me/konservatorruss . '))
        print(gradient_text(' │ Создатель - Godilksq(Чаёк) один из администраторов канала.'))
        print(gradient_text(' │ Тут есть базы таких как: Артек, Глаз Бога, СпортМастер, Яндекс Еда'))
        print('')
        print(gradient_text(' │ Что бы продолжить нажмите esc'))
        keyboard.wait('esc')
        os.system('cls')
        continue
    if inputs == 22:
        time.sleep(1)
        os.system('cls')
        time.sleep(0.5)
        print('')
        print(gradient_text( '▄▄▄▄· ▄▄▌         ▄▄▄· ·▄▄▄▄  '))
        print(gradient_text(' ▐█ ▀█▪██•  ▪     ▐█ ▀█ ██▪ ██ '))
        print(gradient_text(' ▐█▀▀█▄██▪   ▄█▀▄ ▄█▀▀█ ▐█· ▐█▌'))
        print(gradient_text(' ██▄▪▐█▐█▌▐▌▐█▌.▐▌▐█ ▪▐▌██. ██ '))
        print(gradient_text(' ·▀▀▀▀ .▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•'))
        print('')
        print(gradient_text(' │ Закрываю...'))
        time.sleep(1)
        static = False
    else:
        print('')
        time.sleep(0.5)
        print(gradient_text(' │ Неизвестный Пункт!'))
        print('')
        print(gradient_text(' │ Что бы продолжить нажмите esc'))
        keyboard.wait('esc')
        os.system('cls')
        continue

# 28.10.2024, 15:00 (MCK)
# Creator - Godilksq