
class Light_board_text():
    def __init__(self, text, location):
        self.__text = text
        self.__location = location

    def getlocation(self):
        return self.__location

    def adjustlocation(self, location):
        self.__location = location


class Light_board():
    def __init__(self, serial, dimnsions, texts):
        self.__serial = serial
        self.__dimensions = dimnsions
        self.__lightboard_texts = []
        for i in texts:
            self.__lightboard_texts.append(Light_board_text(i,(0, 0)))

board1 = Light_board_text('dududdupachuuuiichui', (0, 0))

#print(board1.text)