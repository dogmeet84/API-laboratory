from telethon.sync import TelegramClient
import csv
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

api_id = 26685350
api_hash = '36e0b49f5de71b251277054b3fd535ca'
phone = '+88806073519'
client = TelegramClient(phone, api_id, api_hash)

client.start()

chats = []
last_date = None
size_chats = 200
groups = []

result = client(GetDialogsRequest(
    offset_date = last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit = size_chats,
    hash = 0
))

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Выберите номер группы из перечня:')
i = 0
for g in groups:
    print(str(i) + '_ ' + g.title)
    i+=1

g_index = input('Введите нужную цифоу: ')
target_group = groups[int(g_index)]

print('Узнаём пользователей...')
all_participants = []
all_participants = client.get_participants(target_group)

print('Сохраняем данные в файл...')
with open ("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter = ",", lineterminator = "\n")
    writer.writerow(['username', 'name', 'group'])
    for user in all_participants:
        if user.username:
            usermame = user.username
        else:
            username = ""
        if user.first_name:
            first_name = user.first_name
        else:
            first_name = ""
        if user.last_name:
            last_name = user.last_name
        else:
            last_name = ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([usermame, name, target_group.title])
print('Парсинг участников группы успешно выполнен.')
