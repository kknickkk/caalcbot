import telegram
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep

bot = telegram.Bot('TOKEN')
    
def main():
   
    update_id = 0
    
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None 

    while True :
            try:
                    update_id = binary(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    # The user has removed or blocked the bot.
                    print("Error: user unauthorized")
                    update_id += 1
    file_.close()

        
def binary(bot, update_id):
    message = 0
    
    file_ = open('log.txt', 'a')
    with open('log.txt', 'r') as f:
        log_out = f.read()
     
    # Request updates after the last update_id
    for update in bot.getUpdates(offset=update_id, timeout=10):
        # chat_id is required to reply to any message
        chat_id = update.message.chat_id
        update_id = update.update_id + 1
        message = update.message.text
        firstname = update.message.from_user.first_name
        lastname = update.message.from_user.last_name
        iduser = str(update.message.from_user.id)
        date = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        
        if message == '/start':
            welcome = "Welcome " + firstname + "!\nEnter a decimal number"
            bot.sendMessage(chat_id=chat_id, text = welcome )
            return update_id
        if message == '/sendlog' and iduser == 'AdminId': #to be changed to admin's chat id
            try:
                bot.sendMessage(chat_id=chat_id, text = log_out )
            except:
                bot.sendMessage(chat_id=chat_id, text = "log is empty" )

            return update_id
            
        file_.write(date +"\t" + iduser +"\t" + firstname + "\t" + lastname + "\t" + message + "\n")
        file_.close()
        
        if not message.isnumeric():
            bot.sendMessage(chat_id=chat_id, text = "Your entry is not a number!\n" + telegram.Emoji.PILE_OF_POO + "\n" + telegram.Emoji.MAN)
            return update_id
       
        num = int(message)        
        binary = "{0:b}".format(num)     
        out =  "Bin ==> " + binary + "\nHex ==> " + hex(num)      

        if num == 42 :
            bot.sendMessage(chat_id=chat_id,text = "MAAAAAGIICCC NUUUUMBEEERRRRR\n")

        if num > 300 :
            bot.sendMessage(chat_id=chat_id,text = "number too large for pile of poo")                        

        else:
            out = num*telegram.Emoji.PILE_OF_POO + "\n\n"+ out

        # Reply to the message
        bot.sendMessage(chat_id=chat_id,text = out)                        

        return update_id

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
