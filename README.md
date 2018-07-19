# Yooka - Line Chatbot
***
API : [https://devdocs.line.me/en/](https://devdocs.line.me/en/)  
line-bot-sdk-python : [https://github.com/line/line-bot-sdk-python](https://github.com/line/line-bot-sdk-python)
***

1. Line Messaging API  
[https://business.line.me/zh-hant/services/bot](https://business.line.me/zh-hant/services/bot)  
 - 記下`Channel Access Token``Channel Secret`

2. Deploy to Heroku

3. App.py configuration
`line_bot_api = LineBotApi('') #Your Channel Access Token`  
`handler = WebhookHandler('') #Your Channel Secret` 

4. Line developers `Webhook URL`  
`https://{YOUR_HEROKU_SERVER_ID}.herokuapp.com/callback`