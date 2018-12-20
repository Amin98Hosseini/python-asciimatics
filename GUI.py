from asciimatics.effects import Cycle,Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects=[
        Cycle(
            screen,
            FigletText("Hello",font='big'),
            int(screen.height/2-8)),
        Cycle(
            screen,
            FigletText("Happy Yalda",font='big'),
            int(screen.height/2)),
        Stars(screen,400)
        ]
    screen.play([Scene(effects,500)])

Screen.wrapper(demo)
