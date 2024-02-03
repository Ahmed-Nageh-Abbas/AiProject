from tkinter import *
from tkinter import messagebox
import pygame
from copy import deepcopy

def form3(Admin):
  background ="#000000"
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #frame = Frame(root,width=950,height=650)
  #insert image 2
  image_path = "img/ppy.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")
  # enter id 
  def on_enter(e):
    code.delete(0,'end')

  def on_leave(e):
    name = code.get()
    if name == '':
      code.insert(0,'ID')

  code = Entry(width=25,fg='#333366',border=0,bg='black',font=('Times',16,'bold'))
  code.place(x=640,y=130)
  code.insert(0,'ID')
  code.bind('<FocusIn>',on_enter)
  code.bind('<FocusOut>',on_leave)
  Frame(width=200,height=1,bg='#333366').place(x=625,y=160)

  #Button 1
  button = Button(width=17, pady=4, text="Solution 1", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,1,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=200)

  #Button 2
  button = Button(width=17, pady=4, text="Solution 2", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,2,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=270)

  #Button 3
  button = Button(width=17, pady=4, text="Solution 3", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,3,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=340)

  #Button 4
  button = Button(width=17, pady=4, text="Solution 4", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,4,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=410)

    #Button 5
  button = Button(width=17, pady=4, text="Solution 5", bg='#333366', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(5,5,code.get()),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=645, y=480)



  root.mainloop()

def form2(Admin):
  background ="#000000"
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #insert image 2
  image_path = "img/iio.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")

  # Create a Label for text on the right side
  heading = Label(text='Choose Level',fg="#990066",bg=background,font=('Times',25,'bold'))
  heading.place(x=580,y=100)

  #Button 1
  button = Button(width=15, pady=4, text="Level 1", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(111),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=190)

  #Button 2
  button = Button(width=15, pady=4, text="Level 2", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(222),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=290)
  #Button 3

  button = Button(width=15, pady=4, text="Level 3", bg='#990066', fg='#000000', border=0, cursor='hand2',command=lambda:[Admin.change(333),root.destroy()],
                  font=('Times', 12, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=460, y=390)

  # Create a Label for id 1
  heading = Label(text='ID = 111',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=190)

  # Create a Label for id 2
  heading = Label(text='ID = 222',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=290)

    # Create a Label for id 3
  heading = Label(text='ID = 333',fg="#cc0066",bg=background,font=('Times',16,'bold'))
  heading.place(x=710,y=390)
  root.mainloop()

def form1(Admin):
  background ="#000000"
  framebg ="#EDEDED"
  framefg="#6666cc" 
  root=Tk()
  root.title("Try Catch Me")
  root.geometry("950x650+10+10")
  root.config(bg=background)
  root.resizable(False,False)
  #insert image
  image_path = "img/pf.png"  
  image = PhotoImage(file=image_path)
  # Create a Label to display the image
  image_label = Label(root, image=image, bg=background)
  image_label.grid(row=0, column=0, padx=0, pady=0, sticky="e")

  # Create a Label for text on the right side
  heading = Label(text='Welcome to our Game',fg=framefg,bg=background,font=('Times',25,'bold'))
  heading.place(x=510,y=50)

  #Button 1
  button = Button(width=20, pady=5, text="You Play", bg='#6666cc', fg='#000000', border=2, cursor='hand2', command=lambda:[Admin.change(2),root.destroy()],
                  font=('Times', 14, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=560, y=220)
  #Button(width=20,pady=5,text="You Play",bg='#6666cc',fg='white',border=2,cursor='hand2',font=('Arial',14,'bold')).place(x=560,y=220)
  # Button 2
  button = Button(width=20, pady=5, text="I Play", bg='#6666cc', fg='#000000', border=2, cursor='hand2',command=lambda:[Admin.change(3),root.destroy()],
                  font=('Times', 14, 'bold'), relief="ridge")  # Change "relief" to your desired style
  button.place(x=560, y=350)
  root.mainloop()

def form6(state,Admin):
    
    pygame.init()

    clock = pygame.time.Clock()

    font1 = pygame.font.Font('fonts/SpaceStory.otf', 35)
    font2 = pygame.font.Font('fonts/SpaceStory.otf', 20)

    rects = rectangles(left=0, top=0, rows=10, cols=10, rect_size=55, rect_border=0, side_width=20)

    screen_bottom_side = 70
    screen = pygame.display.set_mode((rects.over_all_width(), rects.over_all_height() + screen_bottom_side))
    pygame.display.set_caption('Try Catch Me')
    pygame.display.set_icon(pygame.image.load('icons\P.png'))

    button_color1,button_color2 = '#990066','#555555'
    button_y = rects.over_all_height() + (screen_bottom_side / 2)
    back_button = button(centerleft=rects.over_all_width()/2 - 20 , centertop=button_y, width=140, height=35, text='BACK'    , radius=8, rects_distance=3, value=5, color1=button_color1, color2=button_color2, textColor='#aaaaaa')

    c = pygame.transform.smoothscale(pygame.image.load('icons\C1.png').convert_alpha(), (rects.rect_size+15, rects.rect_size+15))
    o = pygame.transform.smoothscale(pygame.image.load('icons\#2.jpg').convert_alpha(), (rects.rect_size-10, rects.rect_size-10))
    m = pygame.transform.smoothscale(pygame.image.load('icons\M1.png').convert_alpha(), (rects.rect_size+10, rects.rect_size+10))
    e = pygame.transform.smoothscale(pygame.image.load('icons\E.png').convert_alpha(), (rects.rect_size, rects.rect_size))
    p = pygame.transform.smoothscale(pygame.image.load('icons\P.png').convert_alpha(), (rects.rect_size, rects.rect_size))
    
    pflipped = pygame.transform.flip(p,1,0)
    pNotflipped = p
    flipped = 0
    
    win_background = pygame.image.load('icons\win.jpg').convert_alpha()
    win_background_rect = win_background.get_rect(center=(screen.get_width()/2,screen.get_height()/2))
    
    game_over_background = pygame.image.load('icons\game_over.jpg').convert_alpha()
    game_over_background = pygame.transform.smoothscale_by(game_over_background, 0.8)
    game_over_background_rect = game_over_background.get_rect(center=(screen.get_width()/2,screen.get_height()/2))

    bottom_side = pygame.Surface((rects.over_all_width(), screen_bottom_side))
    bottom_side.fill('black')

    gates = set()
    for i in range(10):
        for j in range(10):
            if state[i][j] == 'P':
                state[i][j] = '.' 
                p_x, p_y = i+1, j+1
            if state[i][j] == 'E': gates.add((i,j))
    moves = [(p_x, p_y)]
    updates = []

    screen.fill('black')
    display_state(screen, rects, state, o, m, e)
    p_rect = p.get_rect(midbottom = rects.rects[p_x][p_y].midbottom)
    screen.blit(p, p_rect)

    background_sound = pygame.mixer.Sound('music/you_play_sound.mp3')
    step_forward_sound = pygame.mixer.Sound('music/step_forward2.mp3')
    step_back_sound = pygame.mixer.Sound('music/step_back.mp3')
    game_over_sound = pygame.mixer.Sound('music/game_over.mp3')
    win_sound = pygame.mixer.Sound('music/win.mp3')

    background_sound.play(loops=-1)
    background_sound.set_volume(0.3)

    GameState = 1
    key_pressed = 0
    GameIsRunning = True
    while GameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Admin.change(2)
                GameIsRunning = False

            if GameState == 1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_button.rect1.collidepoint(pygame.mouse.get_pos()) and back_button.value > 0: 
                        back_button.rect1.bottom += back_button.rects_distance

                if event.type == pygame.MOUSEBUTTONUP:
                    if back_button.rect1.collidepoint(pygame.mouse.get_pos()) and back_button.value > 0: 
                        if len(moves) > 1: 
                            back_button.value -= 1

                            l = moves[-1]
                            step_back_sound.play()
                            pygame.draw.rect(screen, 'black', rects.rects[l[0]][l[1]])
                            moves.pop()
                            p_x, p_y = moves[-1]

                            if p_y - l[1] > 0 and flipped:
                                p = pNotflipped
                                flipped = 0
                            if l[1] - p_y > 0 and flipped == 0:
                                p = pflipped
                                flipped = 1
                            
                            discard_update(screen, rects, state, updates, gates, e)
                            p_rect.midbottom = rects.rects[p_x][p_y].midbottom
                            screen.blit(p, p_rect)
                        if back_button.value == 0: back_button.color1 = back_button.color2
                    if back_button.value > 0 and back_button.rect1.bottom == back_button.rect2.bottom: 
                        back_button.rect1.bottom -= back_button.rects_distance

                if event.type == pygame.KEYDOWN:
                    k = event.key
                    if k == pygame.K_LEFT: p_left, p_top = -1, 0; key_pressed += 1
                    if k == pygame.K_RIGHT: p_left, p_top = 1, 0; key_pressed += 1
                    if k == pygame.K_UP: p_left, p_top = 0, -1  ; key_pressed += 1
                    if k == pygame.K_DOWN: p_left, p_top = 0, 1 ; key_pressed += 1
                    if key_pressed == 1:
                        p_x += p_top; p_y += p_left
                        if p_x > 0 and p_x <= 10 and p_y > 0 and p_y <= 10 and state[p_x-1][p_y-1] != '#':
                            l = moves[-1]
                            pygame.draw.rect(screen, 'black', rects.rects[l[0]][l[1]])
                            moves.append((p_x, p_y))

                            if p_left > 0 and flipped:
                                p = pNotflipped
                                flipped = 0
                            if p_left < 0 and flipped == 0:
                                p = pflipped
                                flipped = 1
                            
                            update_state(screen, rects, state, updates, c)
                            p_rect.midbottom = rects.rects[p_x][p_y].midbottom
                            screen.blit(p, p_rect)
                            step_forward_sound.play()
                        else: p_x -= p_top; p_y -= p_left

                if event.type == pygame.KEYUP:
                    k = event.key
                    if k == pygame.K_LEFT or k == pygame.K_RIGHT or k == pygame.K_UP or k == pygame.K_DOWN:
                        key_pressed -= 1
                        if state[p_x-1][p_y-1] == 'E':
                            GameState = 2
                        if state[p_x-1][p_y-1] == 'C' or state[p_x-1][p_y-1] == 'M':
                            GameState = 3

        if GameState == 1:
            screen.blit(bottom_side, (0,rects.over_all_height()))
            pygame.draw.line(screen, '#333333', (20,rects.over_all_height()),(rects.over_all_width()-20,rects.over_all_height()))
            back_button.display(screen, font2, font1)
        
        if GameState == 2:
            background_sound.stop()
            win_sound.play()
            pygame.time.delay(300)
            screen.fill('black')
            screen.blit(win_background, win_background_rect)
            GameState = -1
            
        if GameState == 3:
            background_sound.stop()
            game_over_sound.play()
            pygame.time.delay(1000)
            screen.fill('black')
            screen.blit(game_over_background, game_over_background_rect)
            GameState = -1

        pygame.display.update()

        if GameState == -1:
            Admin.change(2)
            GameIsRunning = False
            pygame.time.delay(2000)
           
        clock.tick(60)
    pygame.quit()

def form5(state, player_poses,Admin):
    
    pygame.init()

    clock = pygame.time.Clock()

    rects = rectangles(left=0, top=0, rows=10, cols=10, rect_size=55, rect_border=0, side_width=20)

    screen = pygame.display.set_mode((rects.over_all_width(), rects.over_all_height()))
    pygame.display.set_caption('Try Catch Me')
    pygame.display.set_icon(pygame.image.load('icons\P.png'))
    c = pygame.transform.smoothscale(pygame.image.load('icons\C1.png').convert_alpha(), (rects.rect_size+15, rects.rect_size+15))
    o = pygame.transform.smoothscale(pygame.image.load('icons\#2.jpg').convert_alpha(), (rects.rect_size-10, rects.rect_size-10))
    m = pygame.transform.smoothscale(pygame.image.load('icons\M1.png').convert_alpha(), (rects.rect_size+10, rects.rect_size+10))
    e = pygame.transform.smoothscale(pygame.image.load('icons\E.png').convert_alpha(), (rects.rect_size, rects.rect_size))
    p = pygame.transform.smoothscale(pygame.image.load('icons\P.png').convert_alpha(), (rects.rect_size, rects.rect_size))
    p_rect = p.get_rect(midbottom = rects.rects[player_poses[0][0]+1][player_poses[0][1]+1].midbottom)
    
    pflipped = pygame.transform.flip(p,1,0)
    pNotflipped = p
    flipped = 0
    
    NoSolution_background = pygame.image.load('icons/nosolution.png').convert_alpha()
    NoSolution_background = pygame.transform.smoothscale_by(NoSolution_background, 0.5)
    NoSolution_background_rect = NoSolution_background.get_rect(center=(screen.get_width()/2,screen.get_height()/2))

    NoSolution_sound = pygame.mixer.Sound('music/nosolution.mp3')
    background_sound = pygame.mixer.Sound('music/you_play_sound.mp3')
    step_forward_sound = pygame.mixer.Sound('music/step_forward2.mp3')

    #player_poses = [(-1,-1)]

    if player_poses != [(-1,-1)]:
        background_sound.play(loops=-1)
        background_sound.set_volume(0.3)
        display_state(screen, rects, state, o, m, e)
    else:
        NoSolution_sound.play()

    s = 60
    timer = 0
    GameIsRunning = True
    while GameIsRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
                GameIsRunning = False
        
        if player_poses == [(-1,-1)]:
            screen.blit(NoSolution_background, NoSolution_background_rect)
            if timer/s == 14:
                
                GameIsRunning = False
        else:
            i = int(timer / s)

            if i == len(player_poses):
                
                GameIsRunning = False
                pygame.time.delay(1000)
            
            if timer%s == 0 and i < len(player_poses):
                l = player_poses[max(i-1,0)]
                n = player_poses[i]
                
                if n[1] - l[1] > 0 and flipped:
                    p = pNotflipped
                    flipped = 0
                if l[1] - n[1] > 0 and flipped == 0:
                    p = pflipped
                    flipped = 1

                pygame.draw.rect(screen, 'black', rects.rects[l[0]+1][l[1]+1])
                if i: 
                    update_state2(screen, rects, state, c)
                    step_forward_sound.play()
                p_rect.midbottom = rects.rects[n[0]+1][n[1]+1].midbottom
                screen.blit(p, p_rect)
            
        timer += 1
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

class button:
    def __init__(self, centerleft = 0, centertop = 0, width = 0, height = 0, text = '', radius = 0, rects_distance = 0, value = 0, color1 = 'black', color2 = 'black', textColor = 'white') -> None:
        self.color1, self.color2, self.textColor = color1, color2, textColor
        self.centerleft, self.centertop = centerleft, centertop
        self.width ,self.height = width, height
        self.text, self.radius = text, radius
        self.rects_distance = rects_distance
        self.value = value

        self.rect1 = pygame.Rect(0, 0, self.width, self.height)
        self.rect2 = pygame.Rect(0, 0, self.width, self.height)
        self.rect1.centerx = self.rect2.centerx = centerleft
        self.rect1.centery , self.rect2.centery = centertop - rects_distance , centertop
    def display(self, surface, text_font, value_font):
        pygame.draw.rect(surface, self.color2, self.rect2, 0, self.radius)
        pygame.draw.rect(surface, self.color1, self.rect1, 0, self.radius)

        text_surf = text_font.render(self.text, True, self.textColor)
        surface.blit(text_surf, text_surf.get_rect(center = self.rect1.center))

        value_surf = value_font.render(str(self.value), True, self.textColor)
        value_rect = value_surf.get_rect(midleft = self.rect2.midright)
        value_rect.right += 20
        surface.blit(value_surf, value_rect)

class rectangles:
    def __init__(self, left = 0, top = 0, rows = 0, cols = 0, rect_size = 0, rect_border = 0, side_width = 0):
        self.left, self.top = left, top
        self.rows ,self.cols = rows, cols
        self.rect_size = rect_size
        self.rect_border = rect_border
        self.side_width = side_width

        self.rects = []
        for i in range(self.rows + 1):
            row = []
            for j in range(self.cols + 1):
                row.append(pygame.Rect(0, 0, 0, 0))
            self.rects.append(row)

        for i in range(self.rows + 1): self.rects[i][0].x = left + self.side_width
        for i in range(self.cols + 1): self.rects[0][i].y = top +  self.side_width

        for i in range(self.rows):
            for j in range(self.cols):
                x = self.rects[i + 1][j].midright[0] + rect_border
                y = self.rects[i][j + 1].midbottom[1] + rect_border
                self.rects[i + 1][j + 1].x = x
                self.rects[i + 1][j + 1].y = y
                self.rects[i + 1][j + 1].width = rect_size
                self.rects[i + 1][j + 1].height = rect_size

        self.board_width =  (rows)*rect_size + side_width + (rows+1)*rect_border
        self.board_height = (cols)*rect_size + side_width + (cols+1)*rect_border
        self.board_left = self.rects[1][1].x - (side_width/2) - rect_border
        self.board_top =  self.rects[1][1].y - (side_width/2) - rect_border
        self.board_rect = pygame.Rect(self.board_left, self.board_top, self.board_width, self.board_height)

        self.icons = []
        for i in range(self.rows + 1):
            row = []
            for j in range(self.cols + 1):
                row.append(0)
            self.icons.append(row)

    def showIcon(self, screen, icon, x, y):
        icon_rect = icon.get_rect(center = self.rects[x][y].center)
        screen.blit(icon, icon_rect)

    def over_all_width(self):
        return self.side_width + self.board_width
    def over_all_height(self):
        return self.side_width + self.board_height

def display_state(screen, rects, state, o, m, e):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == '#':
                rects.showIcon(screen, o, i+1, j+1)
            if state[i][j] == 'M':
                rects.showIcon(screen, m, i+1, j+1)
            if state[i][j] == 'E':
                rects.showIcon(screen, e, i+1, j+1)

def update_state(screen, rects, state, updates, c):
    updates.append([])
    ar = [ 0,0,1,-1 ]
    ac = [ 1,-1,0,0 ]
    def valid(i, j): return i >= 0 and i < len(state) and j >= 0 and j < len(state)
    new_state = deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if new_state[i][j] == 'C' or new_state[i][j] == 'M':
                for k in range(4):
                    ii = i + ar[k]
                    jj = j + ac[k]
                    if valid(ii, jj) and new_state[ii][jj] != 'C' and new_state[ii][jj] != 'M' and new_state[ii][jj] != '#':
                        state[ii][jj] = 'C'
                        updates[-1].append((ii,jj))
                        pygame.draw.rect(screen, 'black', rects.rects[ii+1][jj+1])
                        rects.showIcon(screen, c, ii+1, jj+1)

def discard_update(screen, rects, state, updates, gates, e):
    for (i,j) in updates[-1]:
        state[i][j] = '.'
        pygame.draw.rect(screen, 'black', rects.rects[i+1][j+1])
        if (i,j) in gates:
            state[i][j] = 'E'
            e_rect = e.get_rect(midbottom = rects.rects[i+1][j+1].midbottom)
            screen.blit(e, e_rect)
    updates.pop()

def update_state2(screen, rects, state, c):
    ar = [ 0,0,1,-1 ]
    ac = [ 1,-1,0,0 ]
    def valid(i, j): return i >= 0 and i < len(state) and j >= 0 and j < len(state)
    new_state = deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if new_state[i][j] == 'C' or new_state[i][j] == 'M':
                for k in range(4):
                    ii = i + ar[k]
                    jj = j + ac[k]
                    if valid(ii, jj) and new_state[ii][jj] != 'C' and new_state[ii][jj] != 'M' and new_state[ii][jj] != '#':
                        state[ii][jj] = 'C'
                        pygame.draw.rect(screen, 'black', rects.rects[ii+1][jj+1])
                        rects.showIcon(screen, c, ii+1, jj+1)
