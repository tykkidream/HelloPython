import sys
import pygame
from bullet import Bullet

"""
根据键盘操作，执行飞船的动作，比如移动、射击
"""

def check_events(ai_settings, screen, ship, bullets):
    # 监视键盘和鼠标事件

    """ 初始代码，之后被重构
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
    """

    """ 第一次重构 简化代码 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets);
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship);




"""响应按键"""
def check_keydown_event(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True;
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

"""响应按键"""
def check_keyup_event(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False;
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False;


"""如果没有达到限制，就发射一颗子弹"""
def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一个子弹，并将其加入到编组bullets中
    # 屏幕上最多3个子弹
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(bullets):
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    # 不能直接从bullets中删除，需要从bullets的副本遍历
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            # print(len(bullets))