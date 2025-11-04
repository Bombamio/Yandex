from pyrogram.client import Client


api_id = 23544899
api_hash = 'bf227cb86a49fe6aa2ff5e6135e18208'

app = Client('my_account', api_id, api_hash)

app.start()
app.send_message(5888318806, 'Ха, работает!')
app.stop()
https://api.telegram.org/bot8364619889:AAGCw6gZ24M6EIBySwfUDPpJ91EUxndTu7g/sendMessage?chat_id=1811456266&text=Hello!