
import random

from game.casting.actor import Actor
from game.casting.stone import Stones
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


FRAME_RATE = 5
MAX_X = 900
MAX_Y = 600
MIN_Y = 0
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "GREED"
WHITE = Color(255, 255, 255)
DEFAULT_STONES = 40


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y - CELL_SIZE)
    position = Point(x, y)

    player = Actor()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    cast.add_actor("players", player)
    
    # create stones
    
    for n in range(DEFAULT_STONES):
        stones_characters = ["*", "o"]
        text = random.choice(stones_characters)

        # text messages for gems and stones
        if text == "*":
            message = "You got a gem!"
        else:
            message = "Oh no thats a rock!"

        # position 
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # color 
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # setting the stones and messages
        stone = Stones()
        stone.set_text(text)
        stone.set_font_size(FONT_SIZE)
        stone.set_color(color)
        stone.set_position(position)
        stone.set_velocity(Point(0, 1).scale(CELL_SIZE))
        stone.set_message(message)
        cast.add_actor("stones", stone)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()