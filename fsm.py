from transitions.extensions import GraphMachine

from utils import send_text_message, send_image_url, handle_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_help(self, event):
        text = event.message.text
        return text.lower() == "help"

    def is_going_to_picture(self, event):
        text = event.message.text
        return text.lower() == "c8763"

    def is_going_to_info(self, event):
        text = event.message.text
        return text.lower() == "info"

    def is_going_to_weather(self, event):
        #text = event.message.text
        cmd = event.message.text.split(" ")
        text = cmd[0]
        return text == "天氣"

    def on_enter_help(self, event):
        print("I'm entering help")

        reply_token = event.reply_token
        text = "功能:\n圖片:\t輸入 c8763\n天氣:\t輸入 \"天氣 地區\"\n幫助:\t輸入 help\n資訊:\t輸入 info"
        send_text_message(reply_token, text)

        self.go_back()

    def on_exit_help(self):
        print("Leaving help")

    def on_enter_picture(self, event):
        print("I'm entering picture")

        image_url='https://i.imgur.com/6azVaI0.jpg'
        reply_token = event.reply_token
        send_image_url(reply_token, image_url)

        self.go_back()

    def on_exit_picture(self):
        print("Leaving picture")

    def on_enter_info(self, event):
        print("I'm entering picture")
        
        reply_token = event.reply_token
        send_image_url(reply_token, https://imgur.com/a/u8KuxUb)

        self.go_back()

    def on_exit_info(self):
        print("Leaving info")

    def on_enter_weather(self, event):
        print("I'm entering weather")

        reply_token = event.reply_token
        cmd = event.message.text.split(" ")
        handle_message(reply_token, cmd)
        #send_text_message(reply_token, "Trigger weather")
        self.go_back()

    def on_exit_weather(self):
        print("Leaving weather")
