from mycroft import MycroftSkill, intent_file_handler


class ILoveYou(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('you.love.i.intent')
    def handle_you_love_i(self, message):
        self.speak_dialog('you.love.i')


def create_skill():
    return ILoveYou()

