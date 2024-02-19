import pgzrun
import os 
from pgzhelper import *
import random
import time
os.environ["SDL_VIDEO_CENTERED"] = "1"
WIDTH = 1000
HEIGHT = 700 
TITLE = 'GAME'


#-------menu---------
backGrand1 = Actor("menu1", (500, 350))
minMenu = True
play = Actor ('play1', (500, 200))
ok = Actor ('ok', (500, 500))
backGrand2 = Actor ('qvanin', (500, 350))
qvanin = None
playGame = False
exit_game = Actor ('exit1', (500, 550))
exitArt = Actor ('exitgame', (500, 350))
exitGame = False
yes = Actor ('yes', (400, 500))
no = Actor ('no', (600, 500))
about = Actor ('about1', (500, 350))
about_icon = Actor ('abouticon1', (500, 350))
aboutGame = False
ok2 = Actor ('ok', (650, 500))
gameOverArt = Actor ('youlost', (500, 350))


pool = 2
score = 0 
gameOver = False
button_pos = 0, 0
carecterSave = None

skeletonAttackSpeed = 0
skeletonSpeed = 1

skeletonAttackSpeed2 = 0
skeletonSpeed2 = 1

skeletonAttackSpeed2 = 0
skeletonSpeed2 = 1

skeletonAttackSpeed3 = 0
skeletonSpeed3 = 1

skeletonAttackSpeed4 = 0
skeletonSpeed4 = 1

skeletonAttackSpeed5 = 0
skeletonSpeed5 = 1

skeletonAttackSpeed6 = 0
skeletonSpeed6 = 1

skeletonAttackSpeed7 = 0
skeletonSpeed7 = 1

skeletonAttackSpeed8 = 0
skeletonSpeed8 = 1

skeletonAttackSpeed9 = 0
skeletonSpeed9 = 1

skeletonAttackSpeed9 = 0
skeletonSpeed9 = 1


arowShat = 0
arowShat2 = 0
arowShat3 = 0
arowShat4 = 0
arowShat5 = 0
arowShat6 = 0
arowShat7 = 0
arowShat8 = 0
arowShat9 = 0

# x = [1050, 1100, 1150]
# y = [350, 450, 550]
# yRandom = random.choice (y)
# xRandom = random.choice (x)

backGrand = Actor ("backgrand2_11zon", (500, 350))
pause = Actor ('pause', (900, 100))
pauesGame = False
pauseBack = Actor ('backgrand', (500, 350))
resume = Actor ('resume', (500, 300))
resume2 = Actor ('resume', (500, 350))
backMenu = Actor ('exit1', (500, 450))
#---------------idle character-----------------

archer = Actor ('archr', (50, 50))
archer2 = Actor ('archr', (-50, -50))
archer2.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer2.fps = 3

archer3 = Actor ('archr', (-50, -50))
archer3.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer3.fps = 3

archer4 = Actor ('archr', (-50, -50))
archer4.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer4.fps = 3

archer5 = Actor ('archr', (-50, -50))
archer5.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer5.fps = 3

archer6 = Actor ('archr', (-50, -50))
archer6.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer6.fps = 3

archer7 = Actor ('archr', (-50, -50))
archer7.images = ['archr2', 'archr3', 'archr4', 'archr5', 'archr6',]
archer7.fps = 3
#------------------attack character---------------------

attachArcher = Actor ('attack', (-50, -50))
attachArcher.images = ['attack2', 'attack3', 'attack4', 'attack5', 'attack6', 'attack7', 'attack8', 'attack9', 'attack10', 'attack11', 'attack12', 'attack13', 'attack14', 'attack15']
attachArcher.fps = 5

arow = Actor ("arow", (100, 1350))
arow2 = Actor ("arow", (150, 1350))
arow3 = Actor ("arow", (100, 1450))
arow4 = Actor ("arow", (150, 1450))
arow5 = Actor ("arow", (100, 1550))
arow6 = Actor ("arow", (150, 1550))
#-----------------skeleton---------------
skeleton = Actor ('skeleton', (1050, 350))
skeleton.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeletonDamage = Actor ('damagesk', (50, 50))
skeletonDamage.images = ['damagesk', 'damagesk1']
skeletonDamage.fps = 0.25
skeletonAttck = Actor ('skeleton')
skeletonAttck.images = ['attacks1', 'attacks2', 'attacks3']

skeleton2 = Actor ('skeleton', (1100, 350))
skeleton2.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton3 = Actor ('skeleton', (1100, 350))
skeleton3.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton4 = Actor ('skeleton', (1050, 450))
skeleton4.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton5 = Actor ('skeleton', (1100, 450))
skeleton5.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton6 = Actor ('skeleton', (1100, 450))
skeleton6.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton7 = Actor ('skeleton', (1050, 550))
skeleton7.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton8 = Actor ('skeleton', (1100, 550))
skeleton8.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4
skeleton9 = Actor ('skeleton', (1100, 550))
skeleton9.images = ['skeleton1', 'skeleton2', 'skeleton3', 'skeleton4', 'skeleton5', 'skeleton6', 'skeleton7']
skeleton.fps = 4



def update() :
    global arowShat, gameOver, skeletonSpeed, skeletonSpeed2, arowShat2, arowShat3, arowShat4, arowShat5, arowShat6, arowShat7, arowShat8, arowShat9, score, pool
    # def minMenu() :
        
    
    
    
    
    
    
    
    if not minMenu and not gameOver and not pauesGame :
        # archer3.animate()
        # archer4.animate()
        # archer5.animate()
        # archer6.animate()
        skeleton.animate()
        skeleton.flip_x = True
        skeleton.x -= skeletonSpeed
        if score >= 8 :
            skeleton2.animate()
            skeleton2.flip_x = True
            skeleton2.x -= skeletonSpeed2
        if score >= 14 :
            skeleton3.animate()
            skeleton3.flip_x = True
            skeleton3.x -= skeletonSpeed3
        if score >= 4 :
            skeleton4.animate()
            skeleton4.flip_x = True
            skeleton4.x -= skeletonSpeed4
        if score >= 10 :
            skeleton5.animate()
            skeleton5.flip_x = True
            skeleton5.x -= skeletonSpeed5
        if score >= 16 :
            skeleton6.animate()
            skeleton6.flip_x = True
            skeleton6.x -= skeletonSpeed6
        if score >= 6 :
            skeleton7.animate()
            skeleton7.flip_x = True
            skeleton7.x -= skeletonSpeed7
        if score >= 12 :
            skeleton8.animate()
            skeleton8.flip_x = True
            skeleton8.x -= skeletonSpeed8
        if score >= 18 :
            skeleton9.animate()
            skeleton9.flip_x = True
            skeleton9.x -= skeletonSpeed9
    #---------------archer2,3---------------
        if skeleton.x <= 1000 and skeleton.y == 350 or skeleton2.x <= 1000 and skeleton2.y == 350 or skeleton3.x <= 1000 and skeleton3.y == 350 :
            archer2.image = attachArcher.image
            attachArcher.animate()
        else :
            archer2.image = archer2.image
        if skeleton.x <= 1000 and skeleton.y == 350 or skeleton2.x <= 1000 and skeleton2.y == 350 or skeleton3.x <= 1000 and skeleton3.y == 350 :
            archer3.image = attachArcher.image
            attachArcher.animate()
        else :
            archer3.image = archer3.image
    #----------archer 4,5-----------
        if skeleton4.x <= 1000 and skeleton4.y == 450 or skeleton5.x <= 1000 and skeleton5.y == 450 or skeleton6.x <= 1000 and skeleton6.y == 450 :
            archer4.image = attachArcher.image
            attachArcher.animate()
        else :
            archer4.image = archer4.image
        if skeleton4.x <= 1000 and skeleton4.y == 450 or skeleton5.x <= 1000 and skeleton5.y == 450 or skeleton6.x <= 1000 and skeleton6.y == 450 :
            archer5.image = attachArcher.image
            attachArcher.animate()
        else :
            archer5.image = archer5.image       

    #---------archer 6,7--------------
        if skeleton7.x <= 1000 and skeleton7.y == 550 or skeleton8.x <= 1000 and skeleton8.y == 550 or skeleton9.x <= 1000 and skeleton9.y == 550 :
            archer6.image = attachArcher.image
            attachArcher.animate()
        else :
            archer6.image = archer6.image
        if skeleton7.x <= 1000 and skeleton7.y == 550 or skeleton8.x <= 1000 and skeleton8.y == 550 or skeleton9.x <= 1000 and skeleton9.y == 550 :
            archer7.image = attachArcher.image
            attachArcher.animate()
        else :
            archer7.image = archer7.image        


    #------------arow--------------------
        if  arow.colliderect(skeleton)  :
            skeletonDamage.animate()
            skeleton.image = skeletonDamage.image
            arow.x = 100
            arowShat += 1 
        elif arow.colliderect(skeleton2) :
            skeletonDamage.animate()
            skeleton2.image = skeletonDamage.image
            arow.x = 100
            arowShat2 += 1

        elif arow.colliderect(skeleton3) :
            skeletonDamage.animate()
            skeleton3.image = skeletonDamage.image
            arow.x = 100
            arowShat3 += 1

        if  arow2.colliderect(skeleton)  :
            skeletonDamage.animate()
            skeleton.image = skeletonDamage.image
            arow2.x = 150
            arowShat += 1 
        elif arow2.colliderect(skeleton2) :
            skeletonDamage.animate()
            skeleton2.image = skeletonDamage.image
            arow2.x = 150
            arowShat2 += 1
        elif arow2.colliderect(skeleton3) :
            skeletonDamage.animate()
            skeleton3.image = skeletonDamage.image
            arow2.x = 150
            arowShat3 += 1

        if  arow3.colliderect(skeleton4)  :
            skeletonDamage.animate()
            skeleton4.image = skeletonDamage.image
            arow3.x = 150
            arowShat4 += 1 
        elif arow3.colliderect(skeleton5) :
            skeletonDamage.animate()
            skeleton5.image = skeletonDamage.image
            arow3.x = 150
            arowShat5 += 1
        elif arow3.colliderect(skeleton6) :
            skeletonDamage.animate()
            skeleton6.image = skeletonDamage.image
            arow3.x = 100
            arowShat6 += 1

        if  arow4.colliderect(skeleton4)  :
            skeletonDamage.animate()
            skeleton4.image = skeletonDamage.image
            arow4.x = 150
            arowShat4 += 1 
        elif arow4.colliderect(skeleton5) :
            skeletonDamage.animate()
            skeleton6.image = skeletonDamage.image
            arow4.x = 150
            arowShat5 += 1
        elif arow4.colliderect(skeleton6) :
            skeletonDamage.animate()
            skeleton6.image = skeletonDamage.image
            arow4.x = 150
            arowShat6 += 1

        if  arow5.colliderect(skeleton7)  :
            skeletonDamage.animate()
            skeleton7.image = skeletonDamage.image
            arow5.x = 150
            arowShat7 += 1 
        elif arow5.colliderect(skeleton8) :
            skeletonDamage.animate()
            skeleton8.image = skeletonDamage.image
            arow5.x = 100
            arowShat8 += 1
        elif arow5.colliderect(skeleton9) :
            skeletonDamage.animate()
            skeleton9.image = skeletonDamage.image
            arow5.x = 100
            arowShat9 += 1

        if  arow6.colliderect(skeleton7)  :
            skeletonDamage.animate()
            skeleton7.image = skeletonDamage.image
            arow6.x = 150
            arowShat7 += 1 
        elif arow6.colliderect(skeleton8) :
            skeletonDamage.animate()
            skeleton8.image = skeletonDamage.image
            arow6.x = 150
            arowShat8 += 1
        elif arow6.colliderect(skeleton9) :
            skeletonDamage.animate()
            skeleton9.image = skeletonDamage.image
            arow6.x = 150
            arowShat9 += 1


    #-----------------arow shat --------------
        if arowShat >= 5 :
            skeleton.x = 1100
            skeleton.y = 350
            arowShat = 0
            score += 2
            pool += 2
        if arowShat2 >= 5 :
            skeleton2.x = 1100
            skeleton2.y = 350
            arowShat2 = 0 
            score += 2  
            pool += 2 
        if arowShat3 >= 5 :
            skeleton3.x = 1100
            skeleton3.y = 350
            arowShat3 = 0
            score += 2
            pool += 2
        if arowShat4 >= 5 :
            skeleton4.x = 1100
            skeleton4.y = 450
            arowShat4 = 0
            score += 2
            pool += 2
        if arowShat5 >= 5 :
            skeleton5.x = 1100
            skeleton5.y = 450
            arowShat5 = 0
            score += 2
            pool += 2
        if arowShat6 >= 5 :
            skeleton6.x = 1100
            skeleton6.y = 450
            arowShat6 = 0
            score += 2
            pool += 2
        if arowShat7 >= 5 :
            skeleton7.x = 1100
            skeleton7.y = 550
            arowShat7 = 0
            score += 2
            pool += 2
        if arowShat8 >= 5 :
            skeleton8.x = 1100
            skeleton8.y = 550
            arowShat8 = 0
            score += 2
            pool += 2
        if arowShat9 >= 5 :
            skeleton9.x = 1100
            skeleton9.y = 550
            arowShat9 = 0
            score += 2
            pool += 2   





        if archer2.x == 100  :
            if arow.x < 1050 :
                arow.x += 5
            else :
                arow.x = 100 
        if archer3.x == 150 : 
            if arow2.x < 1050 :
                arow2.x += 5
            else :
                arow2.x = 150 
        if archer4.x == 100 : 
            if arow3.x < 1050 :
                arow3.x += 5
            else :
                arow3.x = 100 
        if archer5.x == 150 : 
            if arow4.x < 1050 :
                arow4.x += 5
            else :
                arow4.x = 150 
        if archer6.x == 100 : 
            if arow5.x < 1050 :
                arow5.x += 5
            else :
                arow5.x = 100 
        if archer7.x == 150 : 
            if arow6.x < 1050 :
                arow6.x += 5
            else :
                arow6.x = 150 



        if skeleton.colliderect(archer2) or skeleton.colliderect(archer3) or skeleton.colliderect(archer4) or skeleton.colliderect(archer5) or skeleton.colliderect(archer6) or skeleton.colliderect(archer7) :
            skeletonSpeed = skeletonAttackSpeed
            skeletonAttck.animate()
            skeleton.image = skeletonAttck.image
        if skeleton2.colliderect(archer2) or skeleton2.colliderect(archer3) or skeleton2.colliderect(archer4) or skeleton2.colliderect(archer5) or skeleton2.colliderect(archer6) or skeleton2.colliderect(archer7) :
            skeletonSpeed2 = skeletonAttackSpeed2
            skeletonAttck.animate()
            skeleton2.image = skeletonAttck.image    

        if skeleton.x == -50 or skeleton2.x == -50 or skeleton3.x == -50 or skeleton4.x == -50 or skeleton5.x == -50 or skeleton6.x == -50 or skeleton7.x == -50 or skeleton8.x == -50 or skeleton9.x == -50  :
            gameOver = True
            print(gameOver)
            skeleton.x = 1050
            skeleton2.x = 1100
            skeleton3.x = 1100
            skeleton4.x = 1100
            skeleton5.x = 1100
            skeleton6.x = 1100
            skeleton7.x = 1100
            skeleton8.x = 1100
            skeleton9.x = 1100
            pool = 2
            score = 0
            archer2.x = -50
            archer3.x = -50
            archer4.x = -50
            archer5.x = -50
            archer6.x = -50
            archer7.x = -50
            
        # if archer2.y == 320 and pool >= 2 or archer3.y == 320 and pool > 2 or archer4.y == 420 and pool > 2 or archer5.y == 420 and pool > 2 or archer6.y == 520 and pool > 2 or archer7.y == 520 and pool > 2 :
        #     pool -= 2
        


        



def draw(): 
    global minMenu
    if minMenu :
        backGrand1.draw()
        play.draw()
        exit_game.draw()
        about_icon.draw()

        
        if playGame and qvanin == None :
            backGrand2.draw()
            ok.draw()
        elif playGame and qvanin != None :
            minMenu = False
        if exitGame :
            exitArt.draw()
            yes.draw()
            no.draw()
        if aboutGame :
            about.draw()
            ok2.draw()
    
        
    if not minMenu  :
        backGrand.draw()
        archer.draw()
        archer2.draw()
        archer3.draw()
        archer4.draw()
        archer5.draw()
        archer6.draw()
        archer7.draw()
        


        if archer2.x == 100 :
            arow.draw()
        if archer3.x == 150 :
            arow2.draw()
        if archer4.x == 100 :
            arow3.draw()
        if archer5.x == 150 :
            arow4.draw()
        if archer6.x == 100 :
            arow5.draw()
        if archer7.x == 150 :
            arow6.draw()
        skeleton.draw()
        skeleton2.draw()
        skeleton3.draw()
        skeleton4.draw()
        skeleton5.draw()
        skeleton6.draw()
        skeleton7.draw()
        skeleton8.draw()
        skeleton9.draw()
        screen.draw.text(f'score : {score}', topleft = (75, 100), fontsize = 35, color = (165, 0, 89))
        screen.draw.text(f'pool : {pool}', topleft = (700, 100), fontsize = 35, color = (165, 0, 89))
        pause.draw()
        if pauesGame :
            pauseBack.draw()
            resume.draw()
            backMenu.draw()
        if gameOver :
            gameOverArt.draw()
            resume2.draw()
            


def on_mouse_move(pos) :
    global button_pos
    button_pos = pos


def on_mouse_down(pos) :
    global playGame, pool, qvanin, exitGame, aboutGame, pauesGame, minMenu, gameOver
    if archer.collidepoint(pos):
        global carecterSave
        carecterSave = archer
        
        
    if play.collidepoint(pos) :
        playGame = True 
           
    if ok.collidepoint(pos) :
        qvanin = ok
        # print('ok')
        playGame == False
        minMenu = False
    if about_icon.collidepoint(pos) :
        aboutGame = True
    if ok2.collidepoint(pos) :
        aboutGame = False
    if pause.collidepoint(pos) :
        pauesGame = True
    if exit_game.collidepoint(pos) :
        exitGame = True
    if no.collidepoint(pos):
        exitGame = False
    if yes.collidepoint(pos) :
        quit()
    
    if resume.collidepoint(pos) :
        pauesGame = False
    if backMenu.collidepoint(pos) and pauesGame :   
        quit()
    if gameOver :
        if resume.collidepoint(pos) :
            gameOver = False

def on_key_down(key) :
    if key == keys.Q and carecterSave != None and pool >= 2 :
        archer2.x = 100
        archer2.y = 320
        arow.x = 100
        arow.y = 350
        
    elif key == keys.W and carecterSave != None and pool >= 2 :
        archer3.x = 150 
        archer3.y = 320
        arow2.x = 150
        arow2.y = 350
    elif key == keys.A and carecterSave != None and pool >= 2 :
        archer4.x = 100 
        archer4.y = 420
        arow3.x = 100
        arow3.y= 450

    elif key == keys.S and carecterSave != None and pool >= 2 :
        archer5.x = 150 
        archer5.y = 420
        arow4.x = 150
        arow4.y = 450
    elif key == keys.Z and carecterSave != None and pool >= 2 :
        archer6.x = 100 
        archer6.y = 520
        arow5.x = 100
        arow5.y = 550

    elif key == keys.X and carecterSave != None :
        archer7.x = 150 
        archer7.y = 520
        arow6.x = 150
        arow6.y = 550





pgzrun.go()

