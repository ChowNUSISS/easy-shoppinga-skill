from mycroft import MycroftSkill, intent_file_handler


class EasyShoppinga(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shoppinga.easy.intent')
    def handle_shoppinga_easy(self, message):
        self.speak_dialog('shoppinga.easy')


def create_skill():
    return EasyShoppinga()

