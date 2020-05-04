import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})


token = "15d6b148cd74b4165ed62c8c6a39dd61b4483534e15c3842d7783257e01b3d9cf4fb9d06e9af773ef6ac1"

vk = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk)
f = open('cts.txt')
s = f.readlines()
f.close()
gamestart = 0
bot_letter = 0
user_letter = 0
bot_city = str()
user_city = str()
already_named = []

print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            if event.text.split()[0] == 'Начать': 
                already_named = []
                bot_city = s[random.randrange(0, len(s) - 1)].split()[0]
                write_msg(event.user_id, bot_city)
                already_named.append(bot_city)
                gamestart = 1
                bot_letter = bot_city[len(bot_city) - 1].capitalize()
                if bot_letter == 'Ь':
                    bot_letter = bot_city[len(bot_city) - 2].capitalize()
            if gamestart == 1 and event.text.split()[0] + '\n' in s and event.text.split()[0] not in already_named and event.text.split()[0][0] == bot_letter:
                user_city = event.text.split()[0]
                already_named.append(user_city)
                user_letter = user_city[len(user_city) - 1].capitalize()
                if user_letter == 'Ь':
                    user_letter = user_city[len(user_city) - 2].capitalize()
                for i in s:
                    if i.split()[0][0] == user_letter and i.split()[0] not in already_named:
                        bot_city = i
                        write_msg(event.user_id, bot_city)
                        already_named.append(bot_city.split()[0])
                        bot_letter = bot_city[-2].capitalize()
                        if bot_letter == 'Ь':
                            bot_letter = bot_city[-3].capitalize()
                        break       
