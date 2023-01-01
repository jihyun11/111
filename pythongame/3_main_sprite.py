import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("죠죠의 기묘한 모험")

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\USER\\Desktop\\pygame\\background.png")

#스프라이트 불러오기
character = pygame.image.load("C:\\Users\\USER\\Desktop\\pygame\\character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_hight = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기, 즉 화면 중앙에 위치하게 설정함
character_y_pos = screen_height - character_hight #화면 세로의 가장 아래에 위치하게 설정함


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하는 상태인 건지 체크
        if event.type == pygame.QUIT: #x창을 눌러 게임을 껐을 때 발생하는 이벤트
            running = False #게임이 진행중이 아닐때
    
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update() #게임화면을 다시 그리기!


#pygame 종료
pygame.quit()