import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


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
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()

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


def update_screen(ai_settings, screen, ship, bullets, aliens):
    screen.fill(ai_settings.bg_color)

    for bullet in bullets:
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, bullets, aliens):
    # 更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    # 不能直接从bullets中删除，需要从bullets的副本遍历
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
            # print(len(bullets))

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


"""计算外星人在 x 轴的位置"""
def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

"""计算可以创建多少行外星人"""
def get_number_rows(ai_settings, alien_height, ship_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_rows = int(available_space_y / ( 2 * alien_height))
    return number_rows

"""创建一个外星人"""
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    # 设置外星人 x 轴的位置
    alien_width = alien.rect.width
    alien.x = (alien_width + 2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = (alien.rect.height + 2 * alien.rect.height * row_number)
    aliens.add(alien)


"""创建多个外星人"""
def create_fleet(ai_settings, screen, aliens, ship):
    alien = Alien(ai_settings, screen);
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    row_numbers = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(row_numbers):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)



""" 第1版
def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen);

    alien_width = alien.rect.width
    availablle_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(availablle_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        # 设置外星人 x 轴的位置
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)
"""



"""修改外星人在 y 轴上的位置，并修改方向"""
def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1



"""检查外星人的位置是否到达了屏幕的边缘,如果是则改变其方向"""
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break



"""更新外星人位置"""
def update_aliens(ai_settings, ship, aliens, stats, screen, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)



def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()

        create_fleet(ai_settings, screen, aliens, ship)
        ship.center_ship()

        sleep(0.5)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break