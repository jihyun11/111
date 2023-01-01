import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로크기
screen_height = 640 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("죠죠의 기묘한 모험")

#FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\USER\\Desktop\\pygame\\background.png")

#스프라이트 불러오기
character = pygame.image.load("C:\\Users\\USER\\Desktop\\pygame\\character.png")
character_size = character.get_rect().size #이미지 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_hight = character_size[1] #캐릭터의 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로의 절반 크기, 즉 화면 중앙에 위치하게 설정함
character_y_pos = screen_height - character_hight #화면 세로의 가장 아래에 위치하게 설정함

#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#적 캐릭터
enemy = pygame.image.load("C:\\Users\\USER\\Desktop\\pygame\\enemy.png")
enemy_size = enemy.get_rect().size #이미지 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로 크기
enemy_hight = enemy_size[1] #캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로의 절반 크기, 즉 화면 중앙에 위치하게 설정함
enemy_y_pos =( screen_height / 2) - (enemy_hight / 2) #화면 세로의 가장 아래에 위치하게 설정함


#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks() #현재 tick을 받아옴


#이벤트 루프
running = True #게임이 진행중인가?
while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수 설정

    for event in pygame.event.get(): #어떤 이벤트가 발생하는 상태인 건지 체크
        if event.type == pygame.QUIT: #x창을 눌러 게임을 껐을 때 발생하는 이벤트
            running = False #게임이 진행중이 아닐때

        if event.type == pygame.KEYDOWN: #키보드의 키가 눌러졌는지 확인
            if  event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x - 5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        
        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    #가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_hight:
        character_y_pos = screen_height - character_hight


    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False
        


    
    screen.blit(background, (0, 0)) #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    #타이머 집어넣기
    #경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과 시간을 1000으로 나눠서 초 단위로 표시해줌

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    #출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    #시간 카운트 초가 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임 아웃!")
        running = False


    pygame.display.update() #게임화면을 다시 그리기!

#종료 직전 잠시 대기
pygame.time.delay(2000) #2초 정도 대기

#pygame 종료
pygame.quit()