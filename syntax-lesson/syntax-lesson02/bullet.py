import pygame
from pygame.sprite import Sprite

"""
子弹类
"""

# 定义了Bullet类，其括号里指定了父类为Sprite
class Bullet(Sprite):
    """一个对飞船发射的子弹进行管理的类"""

    def __init__(self, ai_settings, screen, ship):
        # 这里是python2.7子类继承父类的语法，也适用于python3，也可简写为supper().__init__()
        super(Bullet, self).__init__()

        self.screen = screen

        # 子弹属性
        # 子弹并非图像，所以使用pygame.Rect从空白处创建一个矩形，需要为其提供坐标x和y，还有宽度和高度
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 子弹位置在最下方，表示子弹从底部射出
        self.y = float(self.rect.y)

        # 子弹颜色
        self.color = ai_settings.bullet_color
        # 子弹速度
        self.speed_factor = ai_settings.bullet_speed_factor


    """向上移动子弹"""
    def update(self):
        # 更新表示子弹位置的最小值
        self.y -= self.speed_factor
        # 更新表示子弹的rect位置
        self.rect.y = self.y


    """在屏幕上绘制子弹"""
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
