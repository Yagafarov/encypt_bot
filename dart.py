from telebot import *
import  logging 

logger  =  telebot . logger 
telebot . logger . setLevel ( logging . DEBUG ) 

bot = TeleBot("5231045993:AAEQjkLZsp00trHA-JIbxlyuatRY6i3vr2Y")
tugmalar=types.ReplyKeyboardMarkup(resize_keyboard=True)

def encrypt(message):
    key=2
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr((ord(message[i]) + key) % 256)
    return encrypted
def decrypt(message):
    key=2
    decrypted = ""
    for i in range(len(message)):
        decrypted += chr((ord(message[i]) - key) % 256)
    return decrypted

tugma1=types.KeyboardButton("Shifr")
tugma2=types.KeyboardButton("DeShifr")
tugmalar.add(tugma1,tugma2)

@bot.message_handler(commands=['start'])
def start(message):
    a=bot.send_message(message.chat.id,"Salom, " + message.from_user.first_name + "!\n"
                                      "Men bilan matnlarni 🔐 <b>Shifrlashingiz</b> va <b>🔓 Deshifrlashingiz</b> mumkin",parse_mode='HTML',reply_markup=tugmalar)

#create help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,"Bot yaratuvchisi: <i><a href='https://t.me/Yagafarov_d' >Computer Science</a> </i>\n"
                     'Bu botga matnni shifr yoki deshifr qilish uchun <b>shifr</b> yoki <b>deshifr</b> tugmasini bosing',parse_mode='HTML')
@bot.message_handler(content_types=['text'])
def text(msg):
    if msg.text=='Shifr':
        a=bot.send_message(msg.chat.id,"Matnni kiriting")
        bot.register_next_step_handler(a,shifr)
    elif msg.text=='DeShifr':
        a=bot.send_message(msg.chat.id,"Matnni kiriting")
        bot.register_next_step_handler(a,deshifr)
    else:
        bot.send_message(msg.chat.id,"Shifr yoki Deshifr tugmasini bosing")
def shifr(message):
    matn=encrypt(message.text)
    bot.send_message(message.chat.id,matn)
def deshifr(message):
    matn=decrypt(message.text)
    bot.send_message(message.chat.id,matn)

bot.polling(none_stop=True)
