botname = "Yooka"
botact = "ngoding"

################### RICH MENU

"""
def richmenu(button):
{
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": true,
  "name": "Yooka Quick Menu",
  "chatBarText": "Quick Menu",
  "areas": [
    {
      "bounds": {
        "x": 11,
        "y": 14,
        "width": 1232,
        "height": 1656
      },
      "action": {
        "type": "message",
        "text": "Info PMB"
      }
    },
    {
      "bounds": {
        "x": 1243,
        "y": 21,
        "width": 1243,
        "height": 1646
      },
      "action": {
        "type": "message",
        "text": "Info Mahasiswa Aktif"
      }
    }
            ]
}
"""

################### USER RESPONSES vs BOT RESPONSES

user_responses = {
  "siapa kamu?": [
      "perkenalkan, namaku {0}".format(botname),
      "kawan di kampus sih manggil aku {0}".format(botname),
      "panggil aja {0}".format(botname)
   ],
  "kamu lagi apa?": [
      "biasa, lagi sibuk {0}".format(botact),
      "ini nih lagi {0}, deadline sudah semakin dekat".format(botact),
      "lagi ngoding {0}, ngga selesai - selesai nih".format(botact)
    ],
  "default": ["Sorry, aku belum ngerti apa yang kamu maksud. Kalau mau tanya soal UNSADA, coba pilih bantuan menu dibawah ya"]
}

def bot_responses(message):
    # Check if the message is in the responses
    if message in user_responses:
        # Return a random matching response
        bot_responses = random.choice(user_responses[message])
    else:
        # Return a random "default" response
        bot_responses = random.choice(user_responses["default"])
    return bot_responses
