import os
import time
import base64
import curses

from pyfiglet import Figlet

# you can change this verible !
FROM: int = 1
TO: int = 5
TITLE: str = "Name-Tool"


class Logo:
    def __init__(self, round: str, numbers: list, title: str=TITLE, time: float=1.0):
        self.round = base64.b64decode(
            b'ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtICAgICAgICAgICAgLQogICAgICAgICAgICAgICAgICAgICAgICAgLS0tLSAgICAgICAgICAgICAgICAgICAgIC0tLS0KICAgICAgICAgICAgICAgICAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLQogICAgICAgICAgICAgICAgIC0tLSAgICAgICAgICAgICAgICAgIC0tLSAgICAgICAgICAgICAgICAgIC0tCiAgICAgICAgICAgICAgIC0tICAgICAgICAgIC0tLS0tXy0tLS0tLS0tLS0tLS1fLS0tLS0gICAgICAgICAgLS0KICAgICAgICAgICAgLS0gICAgICAgICAtLS0tLS0tLSAgICAgICAgICAgICAgICAgLS0tLV8tLS0gICAgICAgICAtCiAgICAgICAgICAtLSAgICAgICAgLS0tLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLS0tICAgICAgICAtCiAgICAgICAgIC0gICAgICAgLS0tLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLS0gICAgICAgIC0KICAgICAgIC0gICAgICAgLS0tLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtLS0tICAgICAgIC0tCiAgICAgIC0gICAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tICAgICAgIC0KICAgIC0tICAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLSAgICAgIC0KICAgLS0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtLS0gICAgICAtCiAgIC0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLSAgICAgIC0KICAtICAgICAgXy0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLSAgICAgIC0KIC0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtLS0gICAgIC0KIC0gICAgIC1fLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLV8gICAgICAtCi0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLSAgICAgLQotICAgICAgXy0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtLS0gICAgICAtCi0gICAgIC1fLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtXyAgICAgIC0KLSAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC1fICAgICAgLQotICAgICAtXy0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLV8gICAgICAtCi0gICAgICBfLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLSAgICAgIC0KLSAgICAgIC0tLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tICAgICAtCiAtICAgICAgXy0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC1fICAgICAgLQogLSAgICAgIC0tLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC1fLSAgICAgLQogIC0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tICAgICAgLQogICAtICAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtXy0gICAgICAtCiAgICAtICAgICAgLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tICAgICAgLQogICAgIC0gICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAtLS0gICAgICAgLQogICAgICAtICAgICAgIC0tLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLSAgICAgICAtCiAgICAgICAtLSAgICAgICAtLS0gICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLSAgICAgICAtLQogICAgICAgICAtICAgICAgICAtLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIC0tLS0tICAgICAgIC0tCiAgICAgICAgICAgLSAgICAgICAgLS0tLS0tICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLS0gICAgICAgICAtCiAgICAgICAgICAgICAtICAgICAgICAgLS0tLS0tLS0gICAgICAgICAgICAgICAgLS0tLS0tLS0gICAgICAgICAtLQogICAgICAgICAgICAgICAtLSAgICAgICAgICAgLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0gICAgICAgICAgIC0tCiAgICAgICAgICAgICAgICAgIC0tICAgICAgICAgICAgICAgICAtLSAtLSAgICAgICAgICAgICAgICAtLS0KICAgICAgICAgICAgICAgICAgICAgLS0tLSAgICAgICAgICAgICAgICAgICAgICAgICAgICAgLS0tLQogICAgICAgICAgICAgICAgICAgICAgICAgIC0tLS0tLSAgICAgICAgICAgICAgIC0tLS0tLQ=='
        ).decode().split("\n")
        self.max = max(len(_) for _ in self.round)
        self.round = [_ + ' '*(self.max - len(_)) for _ in self.round]
        self.numbers = numbers
        self.time = time
        self.title = title.split('\n')[0]

    def parts_round_with_number(self):
        for num in self.numbers:
            length = max(len(_) for _ in num)
            temp = 0
            out = ''
            for index in range(len(self.round)):
                if index > len(self.round) // 2 - len(num) // 2 and temp < len(num):
                    out += self.round[index][:self.max//2-length//2] + num[temp]
                    out += self.round[index][self.max//2-length//2+len(num[temp]):]
                    temp += 1
                else:
                    out += self.round[index]
                out += "\n"
            yield out.split('\n')

    def __start_with_curses(self, stdscr):
        curses.curs_set(0)
        
        for logo in self.parts_round_with_number():
            width, height = os.get_terminal_size()
            stdscr.addstr(1, width // 2 - len(self.title) // 2, self.title)
            for line in range(len(logo)):
                if len(logo[line]) > width:
                    logo[line] = logo[line][:width]
                stdscr.addstr(line + 5, width // 2 - len(logo[line]) // 2, logo[line])
            stdscr.refresh()
            time.sleep(self.time)
            stdscr.clear()
        curses.curs_set(1)

    @staticmethod
    def del_padding(text: str) -> str:
        text = text.split('\n')
        ID = str(id('del'))
        for i in range(len(text)):
            if not text[i].strip():
                text[i] = ID
            if not text[-i].strip():
                text[-i] = ID
        while True:
            try:
                text.remove(ID)
            except:
                 return text
           
    def start(self):
        try:
            curses.wrapper(
                self.__start_with_curses
            )
        except curses.error:
            print("please, make the small screen !")
        

if __name__ == '__main__':
    view = Logo(round, [Logo.del_padding(Figlet('doh').renderText(str(_)))for _ in range(FROM, TO + 1)])
    view.start()
