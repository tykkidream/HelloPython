import pygame
import game_functions as gf

from settings import Settings
from ship import Ship
from pygame.sprite import Group

"""
游戏程序入口
"""

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen.fill(ai_settings.bg_color)

    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, ai_settings)

    # 创建一个用于存储子弹的编组
    bullets = Group();

    # 开始游戏的主循环
    while True:
        # 检查用户输入
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新飞船位置
        ship.update()
        # 更新子弹位置
        gf.update_bullets(bullets)
        # 绘制新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets)



run_game()
