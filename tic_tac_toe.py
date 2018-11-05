# -*- coding: utf-8 -*-
import time
import pygame
pygame.init()
width=800
height=600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
yellow=(255, 255,0)
pygame.font.init()
best=-1
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption('TIC_TAC_TOE')


def txt_obj(text,font):
    txtsurface=font.render(text,True,red)
    return txtsurface,txtsurface.get_rect()
def display_massage(text):
    largeText=pygame.font.SysFont('freesansbold.ttf',30)
    txtsurf,txtrect=txt_obj(text,largeText)
    txtrect.center=(width/2-100,height/2)
    screen.blit(txtsurf,txtrect)
    pygame.display.update()
    
    
def crashed():
    global best
    tmp=0
    if best==1:
        display_massage('CONGRATS YOU WON')
    elif best==0:
        display_massage('DRAW')
    else:
        display_massage('COMPUTER WON')
    time.sleep(2)
    screen.fill(black)
    display_massage('GAME OVER WANNA PLAY MORE Y/N')
    while(tmp==0):
        for event in pygame.event.get():
            screen.fill(black)
            if event.type==pygame.KEYDOWN:
                if event.type==pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.key==pygame.K_y:
                    display_massage('READY')
                    tmp=1
                    time.sleep(1)
                    screen.fill(black)
                    main()
                elif event.key==pygame.K_n:
                    display_massage('BYE BYE')
                    tmp=1
                    time.sleep(1)
                    pygame.quit()
                    exit()
        time.sleep(0.2)
    
def bord():
    screen.lock() 
    screen.fill(black)           
    pygame.draw.line(screen,red,(200,0),(200,600),8)
    pygame.draw.line(screen,red,(400,0),(400,600),8)
    pygame.draw.line(screen,red,(0,200),(600,200),8)
    pygame.draw.line(screen,red,(0,400),(600,400),8)
    screen.unlock()
    pygame.display.update()

def drawcross(x,y):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
    screen.lock()
    pygame.draw.line(screen,white,(x+20,y+20),(x+180,y+180),8)
    pygame.draw.line(screen,white,(x+180,y+20),(x+20,y+180),8)
    screen.unlock()
    pygame.display.update() 
    
def drawcircle(x,y):
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
    screen.lock()
    pygame.draw.circle(screen,yellow,(x+100,y+100),80,8)
    screen.unlock()
    pygame.display.update() 
k1=1
c1='*'
c2='*'
cells=['*']*9


def selector():
    global c1,c2,cells
    cells=['*']*9
    #c1=input('Choose X or O: ')
    j=0
    screen.fill(black)
    display_massage('CHOOSE X OR O AS YOUR SIGN : ')
    while(j==0):
        for event in pygame.event.get():
            screen.fill(black)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    drawcross(200,200)
                    c1='x'
                    j=1
                    time.sleep(1)
                    screen.fill(black)
                elif event.key==pygame.K_o:
                    drawcircle(200,200)
                    j=1
                    c1='o'
                    time.sleep(1)
                else:
                    continue
    if (c1=='x'):
        c2='o'
    else:
        c2='x'
        
def defined():
    global k,k1
    k1=2
    while(k1==2):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if(x<200 and y<200):
                    k=0
                elif(x<400 and x>200 and y<200):
                    k=1
                elif(x>400 and y<200):
                    k=2
                elif(x<200 and y<400 and y>200):
                    k=3
                elif(x<400 and x>200 and y<400 and y>200):
                    k= 4
                elif(x>400 and y>200 and y<400):
                    k= 5
                elif(x<200 and y>400):
                    k= 6
                elif(x<400 and x>200 and y>400):
                    k= 7
                elif(x>400 and y>400):
                    k= 8
                k1=0
        time.sleep(0.1)
    if(cells[k]!='*'):
        display_massage('This cell is already filled plz enter some other value')
        time.sleep(1)
        screen.fill(black)
        bord()
        prnt()
        input_val()
        return ()
    else:
        cells[k]=c1
        #print(k)
    return
def input_val():
    global c1,c2,cells,bg,pn,k1
    defined()
    return

def find_cell():
    #winning move
    global c1,c2,cells,best
    if(case1()):
        prnt()
        time.sleep(1)
        best=-1
        #print('Computer won')
        return False
    #stoping oponent
    elif(case2()):
        return True   
    elif(case4()):
        return True
    #cent9re
    elif(case3()) :
        return True
    elif(case5()):
        return True
    else:
        best=0
        return False
def case3():
    global c1,c2,cells
    if(cells[4]=='*') :
        cells[4]=c2
        return True
    return False
def case1():
    global c1,c2,cells
    #horizontal
    for i in range(3):
        sum=0
        ind=-1
        for j in range(3):
            if(cells[i*3+j]==c2):
                sum+=1
            elif(cells[i*3+j]=='*'):
                ind=j
        if(sum==2 and ind!=-1):
            cells[i*3+ind]=c2
            return True
    for i in range(3):
        sum=0
        ind=-1
        for j in range(3):
            if(cells[j*3+i]==c2):
                sum+=1
            elif(cells[j*3+i]=='*'):
                ind=j
        if(sum==2 and ind!=-1):
            cells[ind*3+i]=c2
            return True
        if(cells[0]=='*' and cells[4]==c2 and cells[8]==c2):
            cells[0]=c2
            return True
        if(cells[0]==c2 and cells[4]=='*' and cells[8]==c2):
            cells[4]=c2
            return True
        if(cells[0]==c2 and cells[4]==c2 and cells[8]=='*'):
            cells[8]=c2
            return True
        if(cells[2]=='*' and cells[4]==c2 and cells[6]==c2):
            cells[2]=c2
            return True
        if(cells[2]==c2 and cells[4]=='*' and cells[6]==c2):
            cells[4]=c2
            return True
        if(cells[2]==c2 and cells[4]==c2 and cells[6]=='*'):
            cells[6]=c2
            return True
    return False
def case2():
    global c1,c2,cells
    #horizontal
    for i in range(3):
        sum=0
        ind=-1
        for j in range(3):
            if(cells[i*3+j]==c1):
                sum+=1
            elif(cells[i*3+j]=='*'):
                ind=j
        if(sum==2 and ind!=-1):
            cells[i*3+ind]=c2
            return True
    for i in range(3):
        sum=0
        ind=-1
        for j in range(3):
            if(cells[j*3+i]==c1):
                sum+=1
            elif(cells[j*3+i]=='*'):
                ind=j
        if(sum==2 and ind!=-1):
            cells[ind*3+i]=c2
            return True
        if(cells[0]=='*' and cells[4]==c1 and cells[8]==c1):
            cells[0]=c2
            return True
        if(cells[0]==c1 and cells[4]=='*' and cells[8]==c1):
            cells[4]=c2
            return True
        if(cells[0]==c1 and cells[4]==c1 and cells[8]=='*'):
            cells[8]=c2
            return True
        if(cells[2]=='*' and cells[4]==c1 and cells[6]==c1):
            cells[2]=c2
            return True
        if(cells[2]==c1 and cells[4]=='*' and cells[6]==c1):
            cells[4]=c2
            return True
        if(cells[2]==c1 and cells[4]==c1 and cells[6]=='*'):
            cells[6]=c2
            return True
    return False
def case4():
    global c1,c2,cells
    if(cells[0]=='*'):
        cells[0]=c2
        return True
    elif(cells[2]=='*'):
        cells[2]=c2
        return True
    elif(cells[6]=='*'):
        cells[6]=c2
        return True
    elif(cells[8]=='*'):
        cells[8]=c2
        return True
    else:
        return False
def case5():
    global c1,c2,cells
    if(cells[1]=='*'):
        cells[1]=c2
        return True
    elif(cells[3]=='*'):
        cells[3]=c2
        return True
    elif(cells[5]=='*'):
        cells[5]=c2
        return True
    elif(cells[7]=='*'):
        cells[7]=c2
        return True
    else:
        return False
def win():
    global c1,c2,cells
    for i in range(3):
        sum=0
        for j in range(3):
            if(cells[i*3+j]==c1):
                sum+=1
        if(sum==3):
            return True
    for i in range(3):
        sum=0
        for j in range(3):
            if(cells[j*3+i]==c1):
                sum+=1
        if(sum==3):
            return True
        if(cells[0]==c1 and cells[4]==c1 and cells[8]==c1):
            return True
        if(cells[0]==c1 and cells[4]==c1 and cells[8]==c1):
            return True
        if(cells[0]==c1 and cells[4]==c1 and cells[8]==c1):
            return True
        if(cells[2]==c1 and cells[4]==c1 and cells[6]==c1):
            return True
        if(cells[2]==c1 and cells[4]==c1 and cells[6]==c1):
            return True
        if(cells[2]==c1 and cells[4]==c1 and cells[6]==c1):
            return True
    return False  

#for printing on colsole  
# def prnt1():
#     global c1,c2,cells
#     for i in range(3):
#         print()
#         for j in range(3):
            
#             if(cells[i*3+j]=='*'):
#                 print(' ',end=' ')
#             else:
#                 print(cells[i*3+j],end=' ')
#             if(j==2):    
#                 print(' ')
#             else:
#                 print('|',end=' ')
#         print('___________')
    
def prnt():
    global c1,c2,cells,bg
    for i in range(3):
        for j in range(3):
            if(cells[i*3+j]=='o'):
                drawcircle(j*200,i*200)
            elif(cells[i*3+j]=='x'):
                drawcross(j*200,i*200)
def player():
    screen.fill(black)
    display_massage('PRESS F TO PLAY FIRST & S TO PLAY SECOND')
    j=0
    while(j==0):
        for event in pygame.event.get():
            screen.fill(black)
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_f:
                    screen.fill(black)
                    display_massage("FIRST PLAYER")
                    j=1
                    time.sleep(1)
                    screen.fill(black)
                    return True
                elif event.key==pygame.K_s:
                    screen.fill(black)
                    display_massage("SECOND PLAYER")
                    j=1
                    time.sleep(1)
                    return False
                else:
                    continue
def player1():
   global best
   while win()==False:
       input_val()
       if(win()==True):
           best=1
           prnt()
           time.sleep(1)
           break
       prnt()
       if(find_cell()==False):
           break
       prnt()
   if(win()==True):
        best=1
        prnt()
        time.sleep(1)
def drw():
    global cells
    for i in range(3):
        for j in range (3):
            if(cells[3*i+j]=='*'):
                return False
    return True
def player2():
   global best
   while win()==False:
       if(find_cell()==False):
           prnt()
           time.sleep(1)
           break
       prnt()
       if(drw()==True):
           best=0
           prnt()
           time.sleep(1)
           break;
       input_val()
       prnt()
       
   if(win()==True):
        best=1
        prnt()
def main():
   #bord()
   # if True:
   #      for event in pygame.event.get():
   #          if event.type==pygame.QUIT:
   #              pygame.quit()
   #              exit()
   global c1,c2,cells
   selector()
   
   if(player()==True):
       screen.fill(black)
       bord()
       player1()
   else:
       screen.fill(black)
       bord()
       player2()
   screen.fill(black)
   crashed()
   
   pygame.quit()
   exit()
   # trt.Screen().exitonclick()
   time.sleep(5)
   return  
main() 
