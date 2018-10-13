import copy
import pygame
import random
#方块大小及数量颜色
SIZE = 30
H =20
W =10
Color = (125, 125, 125)
screen = pygame.display.set_mode((W * SIZE, H * SIZE))
pygame.display.set_caption("block", "mined block")
pygame.display.flip()
wall = []
speedlev = 40

class block:

    def __init__(self):
        self.x = random.randint(1, W-3)
        self.y = 0
        self.rects = []
        self.rect_one = []
        self.rect_two = []
        self.rect_three = []
        self.rect_four = []
        self.teg = 1
        self.model = 0
        #是否到达底部
        self.bottom = False

    def get_model(self, model):
        self.model = model
        if model == 1:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x, self.y + 1]
            self.rect_three =[self.x + 1, self.y]
            self.rect_four =[self.x + 1, self.y + 1]

        #      self.rects = [[self.x, self.y], [self.x, self.y + 1], [self.x + 1, self.y], [self.x + 1, self.y + 1]]
        elif model == 2:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x + 1, self.y]
            self.rect_three =[self.x + 1, self.y + 1]
            self.rect_four = [self.x + 2, self.y + 1]

      #      self.rects = [[self.x, self.y], [self.x + 1, self.y], [self.x + 1, self.y + 1], [self.x + 2, self.y + 1]]
        elif model == 3:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x + 1, self.y]
            self.rect_three =[self.x - 1, self.y + 1]
            self.rect_four = [self.x, self.y + 1]

       #     self.rects = [[self.x, self.y], [self.x + 1, self.y], [self.x - 1, self.y + 1], [self.x, self.y + 1]]
        elif model == 4:
            self.rect_one =[self.x, self.y]
            self.rect_two = [self.x, self.y + 1]
            self.rect_three = [self.x, self.y + 2]
            self.rect_four =[self.x + 1, self.y + 2]

        #    self.rects = [[self.x, self.y], [self.x, self.y + 1], [self.x, self.y + 2], [self.x + 1, self.y + 2]]
        elif model == 5:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x, self.y + 1]
            self.rect_three =[self.x, self.y + 2]
            self.rect_four =[self.x - 1, self.y + 2]

         #   self.rects = [[self.x, self.y], [self.x, self.y + 1], [self.x, self.y + 2], [self.x - 1, self.y + 2]]
        elif model == 6:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x, self.y + 1]
            self.rect_three =[self.x, self.y + 2]
            self.rect_four =[self.x, self.y + 3]

          #  self.rects = [[self.x, self.y], [self.x, self.y + 1], [self.x, self.y + 2], [self.x, self.y + 3]]
        elif model == 7:
            self.rect_one =[self.x, self.y]
            self.rect_two =[self.x - 1, self.y + 1]
            self.rect_three =[self.x, self.y + 1]
            self.rect_four =[self.x + 1, self.y + 1]

           # self.rects = [[self.x, self.y], [self.x - 1, self.y + 1], [self.x, self.y + 1], [self.x + 1, self.y + 1]]
        self.tag = 1
        self.rects = [self.rect_one,self.rect_two ,self.rect_three ,self.rect_four  ]
    def down(self):

#判断下方是否为墙壁
        for rect in self.rects:
            if rect[1] == H - 1:
                self.bottom = True
                break
            for wallrect in wall:
                if rect[0] == wallrect[0] and rect[1] == wallrect[1]-1:
                    self.bottom = True
                    break
#如果下方是墙壁，则说明方块已经到达底部
        if self.bottom == True:
            for rect in block1.rects:
                wall.append(rect)
#如果没有到达底部，则继续增加
        else:
            for rect in self.rects:
                rect[1] = rect[1] + 1



            pass
#移动
    def move(self,direct):
        #是否可以左右移动
        self.leftmove = True
        self.rightmove = True

        for rect in self.rects:
            for wallrect in wall:
                if rect[0] == wallrect[0] - 1 and rect[1] == wallrect[1]:
                    self.rightmove = False
                elif rect[0] == wallrect[0] + 1 and rect[1] == wallrect[1]:
                    self.leftmove = False
        for rect in self.rects:
            if rect[0] >= W-1:
                self.rightmove = False
            if rect[0] <= 0:
                self.leftmove = False
        if direct == 'left' and self.leftmove == True :
            for rect in self.rects:
                rect[0] = rect[0] - 1
        elif direct == 'right' and self.rightmove == True :
            for rect in self.rects:
                rect[0] = rect[0] + 1



#判断旋转撞墙
    def rotateinwall(self):

        bl = False
        br = False
        for rect in self.rects:
            if rect[0]<0:
                bl = True
            elif rect[0]>W-1:
                br = True
        if bl == True:
            for rect in self.rects:
                rect[0]+=1
        elif br == True:
            for rect in self.rects:
                rect[0]-=1
##此处判断是否撞击已为墙壁方块
        flag = False
        for rect in self.rects:
            for wallrect in wall:
                if rect == wallrect:
                    flag = True
        return flag


#进墙后操作
    def rotatemove(self,oldself,oldtag):
        inwall = True
        flag = 0
        #以一号方块为中心移动至周围九宫格来判断是否有合适位置。
        while inwall:
            if (flag == 0):
                for rect in self.rects:
                    rect[0] = rect[0] - 1
                    rect[1] = rect[1] - 1

                pass
            elif(flag <3):
                for rect in self.rects:
                    rect[0] = rect[0] +1

            elif(flag ==3):
                for rect in self.rects:
                    rect[0] = rect[0] - 2
                    rect[1]=rect[1]+1

            elif(flag <6):
                for rect in self.rects:
                    rect[0] = rect[0] +1

            elif(flag == 6):
                for rect in self.rects:
                    rect[0] = rect[0] - 2
                    rect[1]=rect[1]+1

            elif(flag <9):

                for rect in self.rects:
                    rect[0] = rect[0] +1
                flag=flag+1
            else:
                #九宫格没有合适位置
                self.rects =list(oldself)
                self.tag = oldtag
                print("无位置")
                print(oldself)
                print(self.rects)
                break
                pass
            inwall= self.rotateinwall()
            flag = flag + 1

        pass
##旋转
    def rotate(self):
        oldself = copy.deepcopy(self.rects)
#        print("当前方块")
 #       print(oldself)

        oldtag = self.tag
        if self.model == 2:
            if self.tag == 1:
                self.rect_one[0]+=2
                self.rect_one[1]-=1
                self.rect_four[1]-=1
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_one[0]-=2
                self.rect_one[1]+=1
                self.rect_four[1]+=1
                self.tag = 1
            pass
        elif self.model == 3:
            if self.tag == 1:
                self.rect_two[0]-=2
                self.rect_two[1]-=1
                self.rect_three[1]-=1
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_two[0]+=2
                self.rect_two[1]+=1
                self.rect_three[1]+=1
                self.tag = 1
        elif self.model == 4:
            if self.tag == 1:
                self.rect_three[0]+=1
                self.rect_three[1]-=2
                self.rect_four[0]+=1
                self.rect_four[1]-=2
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_three[0]-=2
                self.rect_three[1]-=1
                self.rect_four[0]-=2
                self.rect_four[1]-=1
                self.tag = 3
            elif self.tag == 3:
                self.rect_three[0]-=1
                self.rect_three[1]+=2
                self.rect_four[0]-=1
                self.rect_four[1]+=2
                self.tag = 4
            elif self.tag == 4:
                self.rect_three[0]+=2
                self.rect_three[1]+=1
                self.rect_four[0]+=2
                self.rect_four[1]+=1
                self.tag = 1
        elif self.model == 5:
            if self.tag == 1:
                self.rect_three[0]+=2
                self.rect_three[1]-=1
                self.rect_four[0]+=2
                self.rect_four[1]-=1
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_three[0]-=1
                self.rect_three[1]-=2
                self.rect_four[0]-=1
                self.rect_four[1]-=2
                self.tag = 3
            elif self.tag == 3:
                self.rect_three[0]-=2
                self.rect_three[1]+=1
                self.rect_four[0]-=2
                self.rect_four[1]+=1
                self.tag = 4
            elif self.tag == 4:
                self.rect_three[0]+=1
                self.rect_three[1]+=2
                self.rect_four[0]+=1
                self.rect_four[1]+=2
                self.tag = 1
        elif self.model == 6:
            if self.tag == 1:
                self.rect_one[0]-=1
                self.rect_one[1]+=1
                self.rect_three[0]+=1
                self.rect_three[1]-=1
                self.rect_four[0]+=2
                self.rect_four[1]-=2
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_one[0]+=1
                self.rect_one[1]-=1
                self.rect_three[0]-=1
                self.rect_three[1]+=1
                self.rect_four[0]-=2
                self.rect_four[1]+=2
                self.tag = 1
        elif self.model == 7:
            if self.tag == 1:
                self.rect_two[0] += 1
                self.rect_two[1] += 1
                #a = [self.rect_one]
                self.tag = 2
            elif self.tag == 2:
                self.rect_two[0] -= 1
                self.rect_two[1] -= 1
                self.rect_one[1] += 2
                self.tag = 3
            elif self.tag == 3:
                self.rect_two[0] += 2
                self.rect_two[1] += 1
                self.rect_one[0] += 1
                self.rect_one[1] -= 2
                self.tag = 4
            elif self.tag == 4:
                self.rect_two[0] -= 2
                self.rect_two[1] -= 1
                self.rect_one[0] -= 1
                self.tag = 1
        print("front")
        print(oldself)
        if self.rotateinwall():
            self.rotatemove(oldself,oldtag)






def drawrect(id = []):
    x = id[0]
    y = id[1]
    pygame.draw.rect(screen, Color, (x*SIZE, y*SIZE, SIZE - 1, SIZE - 1))

    pass



block1 = block()
#block1.get_model(5)
block1.get_model(random.randint (1,7))
def flu():
    # 画背景墙
    pygame.draw.rect(screen, (255, 255, 255), (0, 0, W * SIZE, H * SIZE), 0)
    # 画墙上方块
    for rect in wall:
        drawrect(rect)
    # 画空中方块
    for rect in block1.rects:
        drawrect(rect)
    pygame.display.update()

def kill():
    for i in range(0,H):
        b = True #b 记录是否应该kill某列
        a = 0 # a 记录要kill的列数
        for j in range(0, W):

            #for rect in wall:
             lit = [j,i]
             if not (lit in wall):
                b = False
        if b == True:
            for j in range(0,W):
                wall.remove([j,i])
            ##上面移除一行
            ##下面消除使上方向下一格
            for col in range(0,W):
                for row in range (i,0,-1):
                    for rect in wall:
                       if  rect[0] == col and rect[1]==row:
                           rect[1]+=1

    for i in range(0,W):
        if [i,0] in wall:
            pygame.quit()
            exit()


clock = pygame.time.Clock()
downable = 0
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                block1.move('left')

            elif event.key == pygame.K_RIGHT:
                block1.move('right')
            elif event.key == pygame.K_UP:
                block1.rotate()
            elif event.key == pygame.K_DOWN:
                speedlev = 10
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                speedlev = 40


        pass
    downable = downable+1
#判断落到底部或墙上
    if block1.bottom == False:
        if downable>=speedlev:
            block1.down()
            downable = 0
    else:
        kill()
#生成新的牌子
        block1 = block()
        #block1.get_model(6)
        block1.get_model (random.randint (1,7))
    flu()

    clock.tick(100)
