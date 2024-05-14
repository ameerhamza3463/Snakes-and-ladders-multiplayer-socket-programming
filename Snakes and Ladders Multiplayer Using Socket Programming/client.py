import pygame
import time
from network import Network
from random import randint

#Initialize
pygame.init()
w = 1366
h = 768
GD=pygame.display.set_mode((w,h),pygame.FULLSCREEN)
clock = pygame.time.Clock()

#Graphics:
black=(10,10,10)
white=(250,250,250)
red= (200,0,0)
b_red=(240,0,0)
green=(0,200,0)
b_green=(0,230,0)
blue=(0,0,200)
grey=(50,50,50)
yellow=(150,150,0)
purple=(43,3,132)
b_purple=(60,0,190)

board= pygame.image.load("./staticfiles/Snakes-and-Ladders-Bigger.jpg")
dice1=pygame.image.load("./staticfiles/Dice1.png")
dice2=pygame.image.load("./staticfiles/Dice2.png")
dice3=pygame.image.load("./staticfiles/Dice3.png")
dice4=pygame.image.load("./staticfiles/Dice4.png")
dice5=pygame.image.load("./staticfiles/Dice5.png")
dice6=pygame.image.load("./staticfiles/Dice6.png")

redgoti=pygame.image.load("./staticfiles/redgoti.png")
yellowgoti=pygame.image.load("./staticfiles/yellowgoti.png")
greengoti=pygame.image.load("./staticfiles/greengoti.png")
bluegoti=pygame.image.load("./staticfiles/bluegoti.png")
menubg=pygame.image.load("./staticfiles/menu.jpg")
p=pygame.image.load("./staticfiles/playbg.jpg")
intbg=pygame.image.load("./staticfiles/intropic.png")
intbg2=pygame.image.load("./staticfiles/intropic2.jpg")
intbg3=pygame.image.load("./staticfiles/intropic3.jpg")
intbg4=pygame.image.load("./staticfiles/intropic4.jpg")
intbg5=pygame.image.load("./staticfiles/intropic5.jpg")

pygame.mixer.music.load("./staticfiles/music.wav")
snakesound=pygame.mixer.Sound("./staticfiles/snake.wav")
win=pygame.mixer.Sound("./staticfiles/win.wav")
lose=pygame.mixer.Sound("./staticfiles/lose.wav")
ladder=pygame.mixer.Sound("./staticfiles/ladder.wav")

#mouse pos
mouse=pygame.mouse.get_pos()
click=pygame.mouse.get_pressed()

#Ladder check
def ladders(x):
    if x==1: return 38
    elif x==4:return 14
    elif x==9:return 31
    elif x==28:return 84
    elif x==21:return 42
    elif x==51:return 67
    elif x==80:return 99
    elif x==72:return 91
    else:return x

#Snake Check
def snakes(x): 
    if x==17:return 7
    elif x==54:return 34
    elif x==62:return 19
    elif x==64:return 60
    elif x==87:return 36
    elif x==93:return 73
    elif x==95: return 75
    elif x==98: return 79
    else:return x

# Display dice
def dice(a):
    if a==1:
        a=dice1
    elif a==2:
        a=dice2
    elif a==3:
        a=dice3
    elif a==4:
        a=dice4
    elif a==5:
        a=dice5
    elif a==6:
        a=dice6

    time=pygame.time.get_ticks()
    while pygame.time.get_ticks()-time<1000:
        GD.blit(a,(300,500))
        pygame.display.update()    

#Goti movement function
def goti(a):
    l1=[[406,606],[456,606],[506,606],[556,606],[606,606],[656,606],[706,606],[756,606],[806,606],[856,606],[906,606],[906,560],[856,560],[806,560],[756,560],[706,560],[656,560],[606,560],[556,560],[506,560],[456,560],[456,506],[506,506],[556,506],[606,506],[656,506],[706,506],[756,506],[806,506],[856,506],[906,506],[906,460],[856,460],[806,460],[756,460],[706,460],[656,460],[606,460],[556,460],[506,460],[456,460],[456,406],[506,406],[556,406],[606,406],[656,406],[706,406],[756,406],[806,406],[856,406],[906,406],[906,360],[856,360],[806,360],[756,360],[706,360],[656,360],[606,360],[556,360],[506,360],[456,360],[456,306],[506,306],[556,306],[606,306],[656,306],[706,306],[756,306],[806,306],[856,306],[906,306],[906,260],[856,260],[806,260],[756,260],[706,260],[656,260],[606,260],[556,260],[506,260],[456,260],[456,206],[506,206],[556,206],[606,206],[656,206],[706,206],[756,206],[806,206],[856,206],[906,206],[906,160],[856,160],[806,160],[756,160],[706,160],[656,160],[606,160],[556,160],[506,160],[456,160]]
    l2=l1[a]
    x=l2[0]-25
    y=l2[1]-25
    return x,y


def drawboard():
    GD.blit(p,(0,0))
    GD.blit(board,(w/2-250,h/2-250))
    
def drawgoti(player_goti, pos):
    GD.blit(player_goti,pos)

#Message displaying for buttons
def message_display(text,x,y,fs):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True,white)
    return textSurface, textSurface.get_rect()

#Message displaying for field
def message_display1(text,x,y,fs,c):
    largeText = pygame.font.Font('freesansbold.ttf',fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    GD.blit(TextSurf, TextRect)
    

def text_objects1(text, font,c):
    textSurface = font.render(text, True,c)
    return textSurface, textSurface.get_rect()


def text_objects1(text, font):
    textSurface = font.render(text, True,black)
    return textSurface, textSurface.get_rect()


def button1(text,xmouse,ymouse,x,y,w,h,i,a,fs):
    #mouse pos
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>xmouse>x and y+h>ymouse>y:
        pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
        if pygame.mouse.get_pressed()==(1,0,0):
            return True
        
    else:
        pygame.draw.rect(GD,i,[x,y,w,h])
    message_display(text,(x+w+x)/2,(y+h+y)/2,fs)
      

def read_pos(str):
    connected_players = str.split("/")
    t = connected_players[1].split(";")
    p = t[1].split(":")
    player_id = p[0]
    player_data = p[1].split(",")
    return int (connected_players[0]), int(t[0]), int(player_id), int(player_data[0]), int(player_data[1])

def make_pos(tup, player, turn):
    return str(turn) + ";" + str(player) + ":" + str(tup[0]) + "," + str(tup[1])


class Player:
    def __init__(self, x, y, color, pid):
        self.x = x
        self.y = y
        self.color = color        
        self.player_id = pid        
        
    #Quitting:
    def Quit(self):
        pygame.quit()
        quit()
    
    
    #Buttons:
    def play_quit_buttons(self, text,xmouse,ymouse,x,y,w,h,i,a,fs,b):
        if x+w>xmouse>x and y+h>ymouse>y:
            if b == 10:
                pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
            else:            
                pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
            if pygame.mouse.get_pressed()==(1,0,0):
                if b==1:
                    self.options()
                elif b == 10:
                    playonline()
                elif b==5:
                    return 5
                elif b==0:
                    self.Quit()
                elif b=="s" or b==2 or b==3 or b==4:
                    return b
                elif b == 11:
                    choice = self.menuscreen(b)
                    return choice
                elif b==7:
                    self.options()
                else:
                    return True
        else:
            pygame.draw.rect(GD,i,[x,y,w,h])
        message_display(text,(x+w+x)/2,(y+h+y)/2,fs)

    #for mute and unmute    
    def mute_unmute_buttons(self, text,xmouse,ymouse,x,y,w,h,i,a,fs):
        #mouse pos
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+w>xmouse>x and y+h>ymouse>y:
            pygame.draw.rect(GD,a,[x-2.5,y-2.5,w+5,h+5])
            if pygame.mouse.get_pressed()==(1,0,0):
                return True
            
        else:
            pygame.draw.rect(GD,i,[x,y,w,h])
        message_display(text,(x+w+x)/2,(y+h+y)/2,fs)    
          
    
    #Turn
    def turn(self,score,l,s):   
        a=randint(1,6) #player dice roll
        if a==6:
            six=True
        else:
            six=False
        p=dice(a)
        score+=a
        if score<=100:
            lad=ladders(score) #checking for ladders for player
            if lad!=score:
                l=True
                pygame.mixer.Sound.play(ladder)
                time=pygame.time.get_ticks()
                score=lad 
            snk=snakes(score)
            if snk!=score: #checking for snakes for player
                s=True
                pygame.mixer.Sound.play(snakesound)
                score=snk
            
        else: #checks if player score is not grater than 100
            score-=a
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<1500:
                message_display1("Can't move!",650,50,35,black)
                pygame.display.update()
        return score,l,s,six


    def play(self, b):
   
        b6=-1
        time=3000
        if b6==7:
            self.options()
        GD.blit(p,(0,0))
        GD.blit(board,(w/2-250,h/2-250))
        xcr=xcy=xcg=xcb=406-25
        ycr=ycy=ycg=ycb=606-25
        GD.blit(redgoti,(xcy,ycy))
        if 5>b>1 or b==21:
            GD.blit(yellowgoti,(xcy,ycy))
                
        if 5>b>2 or b==21:
            GD.blit(greengoti,(xcg,ycg))
                
        if 5>b>2:
            GD.blit(bluegoti,(xcb,ycb))
        p1="Player 1"
        p1score=0
        if b==21:
            p2="Computer"
            p2score=0
        if 5>b>1:
            p2="Player 2"
            p2score=0
        if 5>b>2:
            p3="Player 3"
            p3score=0
        if 5>b>3:
            p4="Player 4"
            p4score=0
        t=1
        play=True
        while True:
            l=False
            s=False
            time=3000
            GD.blit(p,(0,0))
            GD.blit(board,(w/2-250,h/2-250))
            mouse=pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                
                if event.type==pygame.QUIT:
                    self.Quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        self.Quit()

                
            if b==21:                
                if button1("Player 1",mouse[0],mouse[1],100,700,200,50,red,grey,30):
                    if t==1:
                        p1score,l,s,six = self.turn(p1score,l,s)
                        if not six:
                            t+=1
                        xcr,ycr = goti(p1score)
                        if p1score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Player 1 Wins",650,50,50,black)
                                pygame.mixer.Sound.play(win)
                                pygame.display.update()
                            break
                
                button1("Computer",mouse[0],mouse[1],400,700,200,50,yellow,grey,30)
                if True:
                    if t==2:
                        p2score,l,s,six=self.turn(p2score,l,s)
                        xcy,ycy=goti(p2score)
                        if not six:
                            t+=1
                            if b<3 or b==21:
                                t=1
                        
                        if p2score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Computer Wins",650,50,50,black)
                                pygame.mixer.Sound.play(lose)
                                pygame.display.update()
                            break
            if 5>b>1:
                if button1("Player 1",mouse[0],mouse[1],100,700,200,50,red,grey,30):
                    if t==1:
                        p1score,l,s,six=self.turn(p1score,l,s)
                        xcr,ycr=goti(p1score)
                        if not six:
                            t+=1
                        if p1score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Player 1 Wins",650,50,50,black)
                                pygame.mixer.Sound.play(win)
                                pygame.display.update()
                            break
                    
                if button1("Player 2",mouse[0],mouse[1],400,700,200,50,yellow,grey,30):
                    if t==2:
                        p2score,l,s,six=self.turn(p2score,l,s)
                        xcy,ycy=goti(p2score)
                        if not six:
                            t+=1
                            if b<3:
                                t=1
                        
                        if p2score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Player 2 Wins",650,50,50,black)
                                pygame.mixer.Sound.play(win)
                                pygame.display.update()
                            break
                    
            if 5>b>2:
                if button1("Player 3",mouse[0],mouse[1],700,700,200,50,green,grey,30):
                    if t==3:
                        p3score,l,s,six=self.turn(p3score,l,s)
                        xcg,ycg=goti(p3score)
                        if not six:
                            t+=1
                            if b<4:
                                t=1
                        
                        if p3score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Player 3 Wins",650,50,50,black)
                                pygame.mixer.Sound.play(win)
                                pygame.display.update()
                            break
                    
            if 5>b>3:   
                if button1("Player 4",mouse[0],mouse[1],1000,700,200,50,blue,grey,30):
                    if t==4:
                        p4score,l,s,six=self.turn(p4score,l,s)
                        xcb,ycb=goti(p4score)
                        if not six:
                            t+=1
                            if b<5:
                                t=1
                        
                        if p4score==100:
                            time=pygame.time.get_ticks()
                            while pygame.time.get_ticks()-time<2000:
                                message_display1("Player 4 Wins",650,50,50,black)
                                pygame.mixer.Sound.play(win)
                                pygame.display.update()
                            break

            
            b6=self.play_quit_buttons("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,7)
            GD.blit(redgoti,(xcr,ycr))
            if 5>b>1 or b==21:
                GD.blit(yellowgoti,(xcy+2,ycy))
                
                
            if 5>b>2:
                GD.blit(greengoti,(xcg+4,ycg))
                
                
            if 5>b>3:
                GD.blit(bluegoti,(xcb+6,ycb))
                
            if l:
                time=pygame.time.get_ticks()
                while pygame.time.get_ticks()-time<2000:
                    message_display1("There's a Ladder!",650,50,35,black)
                    pygame.display.update()
            if s:
                time=pygame.time.get_ticks()
                while pygame.time.get_ticks()-time<2000:
                    message_display1("There's a Snake!",650,50,35,black)
                    pygame.display.update()

            clock.tick(7)
            pygame.display.update()
        
        
    def intro(self):
        time=pygame.time.get_ticks()
        while pygame.time.get_ticks()-time<2500:
            GD.blit(intbg,(0,0))
            pygame.display.update()
        while True:
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<500:    
                GD.blit(intbg2,(0,0))
                pygame.display.update()
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<500:
                GD.blit(intbg3,(0,0))
                pygame.display.update()
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<500:
                GD.blit(intbg4,(0,0))
                pygame.display.update()
            time=pygame.time.get_ticks()
            while pygame.time.get_ticks()-time<500:
                GD.blit(intbg5,(0,0))
                pygame.display.update()
                
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    return
            pygame.display.update()

    def options(self):
        flag=True
        while flag==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.Quit()
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        self.Quit()

            #mouse pos
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            b1=b2=b3=b4=b5=-1
            GD.blit(menubg,(0,0))
            #Single player button
            b1 = self.play_quit_buttons("Single Player",mouse[0],mouse[1],(w/2-150),250,300,50,green,b_green,30,"s")
            #2 player button
            b2= self.play_quit_buttons("2 Players",mouse[0],mouse[1],(w/2)-150,350,300,50,green,b_green,30,2)
            #3 player
            b3= self.play_quit_buttons("3 Players",mouse[0],mouse[1],(w/2)-150,450,300,50,green,b_green,30,3)
            #4 player
            b4= self.play_quit_buttons("4 Players",mouse[0],mouse[1],(w/2)-150,550,300,50,green,b_green,30,4)
            #Back button
            b5= self.play_quit_buttons("Back",mouse[0],mouse[1],0,650,200,50,red,b_red,30,5)
            if b5==5:
                self.menuscreen(0)
            if b1=="s":
                self.play(21)
            if b2==2:
                self.play(2)
            if b3==3:
                self.play(3)
            if b4==4:
                self.play(4)
            
            pygame.display.update()
    
    def menuscreen(self, b):
        pygame.mixer.music.play(-1)
        menu=True
        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.Quit()
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        self.Quit()

            #mouse pos
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            
            GD.blit(menubg,(0,0))
            self.play_quit_buttons("Play",mouse[0],mouse[1],(w/2-100),h/2-100,200,100,green,b_green,22,1)
            self.play_quit_buttons("Online Multiplayer",mouse[0],mouse[1],(w/2-100),h/2+30,200,100,purple,b_purple,22,10)
            self.play_quit_buttons("Quit",mouse[0],mouse[1],(w/2-100),(h/2)+180,200,100,red,b_red,22,0)

            mouse=pygame.mouse.get_pos()
            if self.mute_unmute_buttons("Mute Music",mouse[0],mouse[1],1166,0,200,50,purple,b_purple,25):
                pygame.mixer.music.pause()
            if self.mute_unmute_buttons("Play Music",mouse[0],mouse[1],1166,75,200,50,purple,b_purple,25):
                pygame.mixer.music.unpause()

            pygame.display.update()
            if b == 11:
                menu = False
                return 100

    def credit(self):
        while True:
            GD.blit(credits1,(0,0))
            for event in pygame.event.get():
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_ESCAPE:
                        self.Quit()
            #mouse pos
            mouse=pygame.mouse.get_pos()
            click=pygame.mouse.get_pressed()
            if self.play_quit_buttons("Back",mouse[0],mouse[1],w/2-100,700,200,50,red,b_red,25,20):
                self.menuscreen(0)
                
            pygame.display.update()

    def run(self):
        self.intro()
        self.menuscreen(0)
        
        
def playonline():
    n = Network()
    data = read_pos(n.getPos())
    print("Data in client: ", data)
    connected_players, playerturn, player1_id, startPosx, startPosy = data[0], data[1], data[2], data[3], data[4]
    pygame.display.set_caption(f'Player {player1_id}')
    p = Player(startPosx,startPosy, "red", player1_id)
    player2_id = 0 
    if player1_id == 0:
        player2_id = 1 
        p2 = Player(startPosx,startPosy, "yellow", player2_id)
    else:
        player2_id = 0
        p2 = Player(startPosx,startPosy, "yellow", player2_id)
        
    clock = pygame.time.Clock()
    turn = True
    run = True
    t=1
    p1score=0
    p2score=0

    while run:
        clock.tick(60)
        l=False
        s=False
        time=3000
        drawboard()
        drawgoti(redgoti,(p.x,p.y))
        drawgoti(yellowgoti,(p2.x,p2.y))
        mouse=pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                p.Quit()
            
        if button1("Roll Dice",mouse[0],mouse[1],100,700,200,50,red,grey,30):
            if connected_players < 1:
                print("Not enough players! Waiting for other player to connect...")
                time=pygame.time.get_ticks()
                while pygame.time.get_ticks()-time<2000:
                    message_display1("Waiting for other player to connect!!!",650,50,50,black)
                    pygame.mixer.Sound.play(win)
                    pygame.display.update()
                pass
            elif playerturn == player1_id:
                if player1_id == 0:
                    playerturn = 1
                elif player1_id == 1:
                    playerturn = 0
                else:
                    pass
                p1score,l,s,six = p.turn(p1score,l,s)
                    
                p.x,p.y = goti(p1score)
                connected_players, playerturn, player_id2, p2.x, p2.y = read_pos(n.send(make_pos((p.x, p.y), player1_id, playerturn)))

                if p1score==100:
                    time=pygame.time.get_ticks()
                    while pygame.time.get_ticks()-time<2000:
                        message_display1("You Won!!!",650,50,50,black)
                        pygame.mixer.Sound.play(win)
                        pygame.display.update()
                    break  
            
        else:       
            connected_players, playerturn, player_id2, p2.x, p2.y = read_pos(n.send(make_pos((p.x, p.y), player1_id, -1)))
            print("Else: ", playerturn, player_id2, p2.x, p2.y)
            b6=p.play_quit_buttons("Back",mouse[0],mouse[1],0,0,200,50,red,b_red,30,11)
            if b6 == 100:
                run = False
                time=pygame.time.get_ticks()
                while pygame.time.get_ticks()-time<2000:
                    message_display1(f"Player {player1_id} Lose!!! Other player Win...",650,50,50,black)
                    pygame.mixer.Sound.play(lose)
                    pygame.display.update()
                break
            elif connected_players < 1 and p1score > 0:
                b7 = p.menuscreen(11)
                run = False
                time=pygame.time.get_ticks()
                while pygame.time.get_ticks()-time<2000:
                    message_display1(f"Player {player1_id} Won!!! Other player Left the game...",650,50,50,black)
                    pygame.mixer.Sound.play(win)
                    pygame.display.update()
                break
            else:
                GD.blit(redgoti,(p.x,p.y))
                GD.blit(yellowgoti,(p2.x,p2.y))
                    
                if l:
                    time=pygame.time.get_ticks()
                    while pygame.time.get_ticks()-time<2000:
                        message_display1("There's a Ladder!",650,50,35,black)
                        pygame.display.update()
                if s:
                    time=pygame.time.get_ticks()
                    while pygame.time.get_ticks()-time<2000:
                        message_display1("There's a Snake!",650,50,35,black)
                        pygame.display.update()

                clock.tick(7)
                pygame.display.update()
            
        
def main():
    C = Player(406-25, 606-25, "red", 0)
    C.run()

    
main()