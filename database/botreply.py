#####SETUP YOOKA QUICK MENU
"""
quickman = QuickMenuManager(channel_access_token)
# Setup RichMenu to register
quickm = QuickMenu(name="Quick Menu", chat_bar_text="test")
quickm.add_area(0, 0, 1250, 843, "message", "テキストメッセージ")
quickm.add_area(1250, 0, 1250, 843, "uri", "http://imoutobot.com")
quickm.add_area(0, 843, 1250, 843, "postback", "data1=from_richmenu&data2=as_postback")
quickm.add_area(1250, 843, 1250, 843, "postback", ["data3=from_richmenu_with&data4=message_text", "ポストバックのメッセージ"])

# Register
res = quickman.register(quickm, "https://imgur.com/lTT9Axb") #imageline or image direct link?
richmenu_id = res["richMenuId"]
print("Registered as " + richmenu_id)

# Apply to user
user_id = "LINE_MID_TO_APPLY"
quickman.apply(user_id, richmenu_id)

# Check
res = quickman.get_applied_menu(user_id)
print(user_id  + ":" + res["richMenuId"])
"""