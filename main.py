from tkinter import *
from tkinter.messagebox import *
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk
from pickle import *
import json
from tkinter import ttk

BG_COLOR = "#171D25"

def activeBtnUnderline(activeBtn: Button, oldBtn: Button):
    if not("underline" in activeBtn["font"]):
        activeBtn.config(font=f"{activeBtn['font']} underline", fg="#1A9FFF")
    if "underline" in oldBtn["font"]:
        oldBtn.config(font=f"{activeBtn['font'][:-9]}", fg="#ffffff")

class Game:
    def __init__(self, name, price, discount, description, image):
        self.name = name
        self.price = price
        self.discount = discount
        self.description = description
        self.image = image

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getDiscount(self):
        return self.discount

    def getDescription(self):
        return self.description

    def getImage(self):
        return self.image


def getPhotos():
    linksOnPhoto = ["darktide", "division", "ghostrecon", "remnant", "codevein", "arma", "battlefield"]
    photos = []
    for i in range(len(linksOnPhoto)):
        oldImg = f"gameImgs/{linksOnPhoto[i]}.png"
        # resImg = oldImg.resize((274, 158))
        # img = ImageTk.PhotoImage(resImg)
        photos.append(oldImg)
    return photos





class Shop:
    def __init__(self, master: Frame):
        self.master = master
        profFrame.place_forget()
        logFrame.place_forget()
        regFrame.place_forget()
        gameViewFrame.place_forget()
        editProfileFrame.place_forget()
        shopFrame.place(relx=0, rely=0.1)


        self.setGames()


        # smrSaleImg = Image.open("images/summerSale.png")
        # resSmrSaleImg = smrSaleImg.resize((1262, 798))
        # smrImg = ImageTk.PhotoImage(resSmrSaleImg)
        # # Label(self.master, image=smrImg).place(relx=0, rely=0.1)
        # # summerSaleImgLbl.place(relx=0.05, rely=0.1)
        # imagesCanvas = Canvas(self.master, width=1262, height=700, bg="#000000", highlightthickness=0)
        # imagesCanvas.place(relx=0.0, rely=0.1)
        # imagesCanvas.create_image(0, 0, anchor=NW, image=smrImg)
        # imagesCanvas.image = smrImg

    def setGames(self):
        photos = getPhotos()
        darktide = Game(name="Darktide", price=29.99, discount=0, description="Отбейте город Терциум от полчищ кровожадных врагов в напряженном и брутальном шутере. Warhammer 40,000: Darktide — новая кооперативная игра от удостоенной наград команды создателей серии Vermintide. Терциум падет, отверженные восстанут.", image=photos[0])
        division = Game(name="Division", price=16.49, discount=70, description="ИСТОРИЯ НЕ ЗАБУДЕТ Tom Clancy’s The Division® 2: судьба мира зависит от вас Возглавьте отряд спецагентов и наведите порядок в Вашингтоне, пострадавшем от эпидемии.", image=photos[1])
        ghostrecon = Game(name="GhostRecon", price=0, discount=0, description="Станьте «Призраком» и победите других спецназовцев – «Волков» в обновленной игре серии Tom Clancy's Ghost Recon!", image=photos[2])
        remnant = Game(name="Remnant", price=18.49, discount=65, description="В роли одного из последних представителей человечества, в одиночку или в компании одного-двух товарищей, вам предстоит сразиться с ордами монстров и эпическими боссами, пытаясь закрепиться на чужой земле, отстроиться и вернуть себе утраченное.", image=photos[3])
        codevien = Game(name="CodeVien", price=0, discount=85, description="Создайте своего бессмертного, найдите союзников и преодолейте испытания, чтобы вспомнить прошлое и вырваться из ада в игре CODE VEIN.", image=photos[4])
        arma = Game(name="Arma", price=29.99, discount=75, description="Испытайте вкус боевых действий в массовой военной игре. C более чем 20 видами техники и 40 видами оружия, различными режимами игры и безграничными возможностями создания контента, вы получаете наилучший реализм и разнообразие в Arma 3.", image=photos[5])
        battlefield = Game(name="Battlefield", price=59.99, discount=0, description="Вступайте в игровое сообщество Battlefield и откройте для себя зарю мировых войн в командных сетевых боях или в увлекательной одиночной кампании.", image=photos[6])

        # #Запись игр в файл
        # with open("Files/gamesData.json", "w") as FileHandler:
        #     slov = {}
        #     for i in [darktide, division, ghostrecon, remnant, codevien, arma, battlefield]:
        #         slov[i.name] = {
        #             "name": i.name,
        #             "price": i.price,
        #             "discount": i.discount,
        #             "description": i.description,
        #             "image": i.image,
        #             "purchase": 0
        #         }
        #     json.dump(slov, FileHandler)

        #Получение всех игр
        with open("Files/gamesData.json", "r") as FileHandler:
            classesDict = json.loads(FileHandler.readline())

        #Добавление игр в лист
        self.gamesList = []
        for key, val in classesDict.items():
            print(f"{key}")
            print(val["image"])
            oldImg = Image.open(val["image"])
            val["image"] = oldImg

            self.gamesList.append(val)

        self.passedGameCount = 0
        self.addSmallGames()
        self.addBigGames()
        self.createHoverCanvas()


        # try:
        #     with open("Files/gamesData.json", "wb") as FileHandler:
        #         json.dump({}, FileHandler)
        # except Exception as e:
        #     print("Файл очистился.")
            # obj = {
            #     "name": division.name,
            #     "price": division.price,
            #     "discount": division.discount,
            #     "description": division.description,
            #     "image": str(division.image)
            # }
            # json.dump(obj, FileHandler)
        #
        # canvasList = []
        # posX = 0.035
        # positionForCanvasInfo = [posX]
        #371x241
        # gamesCount = 0
        #
        #
        #
        # for i in range(4):
        #     curClass = classesList[i]
        #     canvas = Canvas(self.master, width=274, height=186, bg=BG_COLOR, highlightthickness=0, cursor="hand2")
        #     canvas.create_image(0, 79, anchor=W, image=curClass["image"])
        #     canvas.image = curClass["image"]
        #     textName = canvas.create_text(41, 171, text=curClass["name"], fill="white", font="Arial 11 bold", anchor=NW)
        #
        #     if curClass["price"] == 0:
        #         canvas.create_rectangle(160, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(220, 171, text="Бесплатно", font="Arial 12 bold")
        #     elif curClass["discount"] == 0:
        #         canvas.create_rectangle(190, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(232, 171, text=f"${curClass['price']}", font="Arial 12 bold")
        #     else:
        #         canvas.create_rectangle(213, 157, 274, 186, fill="#A1CD44")
        #         canvas.create_text(244, 171, text=f"- {curClass['discount']}%", font="Arial 12 bold")
        #         canvas.create_text(185, 171, text=f"${curClass['price']}", font="Arial 10 overstrike", fill="#808A8F")
        #         canvas.create_text(137, 172, text=f"${round(float(curClass['price'] - (curClass['price'] * (curClass['discount']/100))), 2)}", font="Arial 11 bold", fill="#ffffff")
        #
        #     canvas.place(relx=posX, rely=0.3)
        #     canvasList.append(canvas)
        #     posX += 0.239
        #     positionForCanvasInfo.append(posX)
        # print(canvasList)
        # # for i in range(4):
        # #     canvasList[i].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[i], pos=positionForCanvasInfo[i]))
        # #     canvasList[i].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[0].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[0], pos=positionForCanvasInfo[0]))
        # canvasList[0].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[1].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[1], pos=positionForCanvasInfo[1]))
        # canvasList[1].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[2].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[2], pos=positionForCanvasInfo[2]))
        # canvasList[2].bind("<Leave>", lambda event: self.outCanvas())
        # canvasList[3].bind("<Enter>", lambda event: self.inCanvas(gameClass=classesList[3], pos=positionForCanvasInfo[3], isLast=True))
        # canvasList[3].bind("<Leave>", lambda event: self.outCanvas())
        # self.infoCanvas = Canvas(self.master, width=305, height=162, highlightthickness=0, background=BG_COLOR)
        # self.intoInfoCanvas = self.infoCanvas.create_rectangle(8, 0, 305, 269, fill="#CEDAE3")
        # self.infoCanvasPolygon = self.infoCanvas.create_polygon(0, 30, 10, 21, 10, 39, fill="#CEDAE3")
        # self.infoCanvasTitle = self.infoCanvas.create_text(22, 10, text="", font="Arial 15", fill="#4B5563", anchor=NW)
        # self.infoCanvasDescription = self.infoCanvas.create_text(23, 40, text="", font="Arial 9", fill="#778696", anchor=NW, width=260)



    def addSmallGames(self):
        posX = 0.035
        self.canvasList = []
        positionForCanvasInfo = [posX]
        hasEndedGames = False

        for i in range(4):
            if i+1 > len(self.gamesList) - self.passedGameCount:
                self.passedGameCount = len(self.gamesList)
                hasEndedGames = True
                break

            curGame = self.gamesList[i + self.passedGameCount]
            #Создание канваса
            print(self.gamesList)
            print(curGame)
            canvas = Canvas(self.master, width=274, height=186, bg=BG_COLOR, highlightthickness=0, cursor="hand2")
            print(curGame["image"])
            resImg = curGame["image"].resize((274, 158))
            wholeImg = ImageTk.PhotoImage(resImg)
            canvas.create_image(0, 79, anchor=W, image=wholeImg)
            canvas.image = wholeImg
            canvas.create_text(3, 163, text=curGame["name"], fill="white", font="Arial 11 bold", anchor=NW)


            #Размещение всех комплектов канваса на канвас
            if curGame["price"] == 0:
                canvas.create_rectangle(160, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(220, 171, text="Бесплатно", font="Arial 12 bold")
            elif curGame["discount"] == 0:
                canvas.create_rectangle(190, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(232, 171, text=f"${curGame['price']}", font="Arial 12 bold")
            else:
                canvas.create_rectangle(213, 157, 274, 186, fill="#A1CD44")
                canvas.create_text(244, 171, text=f"- {curGame['discount']}%", font="Arial 12 bold")
                canvas.create_text(185, 171, text=f"${curGame['price']}", font="Arial 10 overstrike", fill="#808A8F")
                canvas.create_text(137, 172, text=f"${round(float(curGame['price'] - (curGame['price'] * (curGame['discount'] / 100))), 2)}", font="Arial 11 bold", fill="#ffffff")

            #Размещение канвасов на фрейм
            canvas.place(relx=posX, rely=0.15)
            self.canvasList.append(canvas)
            posX += 0.239
            positionForCanvasInfo.append(posX)

            # canvas.bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[i], pos=positionForCanvasInfo[0]))
            # canvas.bind("<Leave>", lambda event: self.outCanvas())

        some = self.passedGameCount

        #Создание событий для наведения на канвас
        self.canvasList[0].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some], pos=positionForCanvasInfo[0]))
        self.canvasList[0].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[0].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 7]))
        self.canvasList[1].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some + 1], pos=positionForCanvasInfo[1]))
        self.canvasList[1].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[1].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 6]))
        self.canvasList[2].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some + 2], pos=positionForCanvasInfo[2]))
        self.canvasList[2].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[2].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 5]))
        self.canvasList[3].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some + 3], pos=positionForCanvasInfo[3], isLast=True))
        self.canvasList[3].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[3].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 4]))


        if not (hasEndedGames):
            self.passedGameCount += 4



    def addBigGames(self):
        # gamesCount = 3
        # if (len(self.gamesList) - self.passedGameCount) > 0:
        #     if (len(self.gamesList) - self.passedGameCount) < 3:
        #         gamesCount = (len(self.gamesList) - self.passedGameCount)
        #
        posX = 0.035
        self.canvasList = []
        positionForCanvasInfo = [posX]
        hasEndedGames = False

        for i in range(3):
            print("FF")
            if i+1 > len(self.gamesList) - self.passedGameCount:
                self.passedGameCount = len(self.gamesList)
                hasEndedGames = True
                break


            curGame = self.gamesList[i + self.passedGameCount]
            # Создание канваса
            canvas = Canvas(self.master, width=371, height=270, highlightthickness=0, cursor="hand2", background=BG_COLOR)
            resImg = curGame["image"].resize((371, 241))
            wholeImg = ImageTk.PhotoImage(resImg)
            canvas.create_image(0, 0, anchor=NW, image=wholeImg)
            canvas.image = wholeImg
            canvas.create_text(3, 248, text=curGame["name"], fill="white", font="Arial 11 bold", anchor=NW)

            # Размещение всех комплектов канваса на канвас
            if curGame["price"] == 0:
                canvas.create_rectangle(256, 240, 370, 269, fill="#A1CD44")
                canvas.create_text(315, 256, text="Бесплатно", font="Arial 12 bold")
            elif curGame["discount"] == 0:
                canvas.create_rectangle(286, 240, 370, 269, fill="#A1CD44")
                canvas.create_text(327, 256, text=f"${curGame['price']}", font="Arial 12 bold")
            else:
                canvas.create_rectangle(309, 240, 370, 269, fill="#A1CD44")
                canvas.create_text(339, 256, text=f"- {curGame['discount']}%", font="Arial 12 bold")
                canvas.create_text(280, 256, text=f"${curGame['price']}", font="Arial 10 overstrike", fill="#808A8F")
                canvas.create_text(232, 257, text=f"${round(float(curGame['price'] - (curGame['price'] * (curGame['discount'] / 100))), 2)}", font="Arial 11 bold", fill="#ffffff")

            # Размещение канвасов на фрейм
            canvas.place(relx=posX, rely=0.45)
            self.canvasList.append(canvas)
            posX += 0.321
            positionForCanvasInfo.append(posX)

        print(f"ffff{self.passedGameCount}")
        print(len(self.gamesList))
        print(self.gamesList)

        some = self.passedGameCount

        # Создание событий для наведения на канвас
        self.canvasList[0].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some], pos=positionForCanvasInfo[0]+0.08, posY=0.45, isBig=True))
        self.canvasList[0].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[0].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 3]))
        self.canvasList[1].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some+1], pos=positionForCanvasInfo[1]+0.08, posY=0.45, isBig=True))
        self.canvasList[1].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[1].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 2]))
        self.canvasList[2].bind("<Enter>", lambda event: self.inCanvas(gameClass=self.gamesList[some+2], pos=positionForCanvasInfo[2]-0.062, posY=0.45, isLast=True, isBig=True))
        self.canvasList[2].bind("<Leave>", lambda event: self.outCanvas())
        self.canvasList[2].bind("<ButtonPress>", lambda event: turnOnGameView(game=self.gamesList[self.passedGameCount - 1]))

        if not (hasEndedGames):
            self.passedGameCount += 3

    def createHoverCanvas(self):
        # Создание канваса при наведении на него
        self.infoCanvas = Canvas(self.master, width=305, height=162, highlightthickness=0, background=BG_COLOR)
        self.intoInfoCanvas = self.infoCanvas.create_rectangle(8, 0, 305, 269, fill="#CEDAE3", outline=BG_COLOR)
        self.infoCanvasPolygon = self.infoCanvas.create_polygon(0, 30, 10, 21, 10, 39, fill="#CEDAE3")
        self.infoCanvasTitle = self.infoCanvas.create_text(22, 10, text="", font="Arial 15", fill="#4B5563", anchor=NW)
        self.infoCanvasDescription = self.infoCanvas.create_text(23, 40, text="", font="Arial 9", fill="#778696", anchor=NW, width=260)

    def inCanvas(self, gameClass, pos, isLast = False, posY = 0.15, isBig = False):
        if isLast:
            self.infoCanvas.place(relx=pos-0.245, rely=posY)
            self.infoCanvas.coords(self.intoInfoCanvas, 0, 0, 297, 269)
            self.infoCanvas.coords(self.infoCanvasPolygon, 296, 39, 296, 21, 306, 30)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, text=gameClass["name"])
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, text=gameClass["description"])
        else:
            self.infoCanvas.place(relx=pos+0.215, rely=posY)
            self.infoCanvas.coords(self.intoInfoCanvas, 8, 0, 305, 269)
            self.infoCanvas.coords(self.infoCanvasPolygon, 0, 30, 10, 21, 10, 39)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, text=gameClass["name"])
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, text=gameClass["description"])

        if isBig:
            self.infoCanvas.config(width=393, height=190)
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, font="Arial 11", width=350)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, font="Arial 18")
            self.infoCanvas.coords(self.infoCanvasDescription, 23, 47)
            if isLast:
                self.infoCanvas.coords(self.intoInfoCanvas, 0, 0, 380, 269)
                self.infoCanvas.coords(self.infoCanvasPolygon, 379, 39, 379, 21, 389, 30)
            else:
                self.infoCanvas.coords(self.intoInfoCanvas, 8, 0, 392, 269)
                self.infoCanvas.coords(self.infoCanvasPolygon, 0, 30, 10, 21, 10, 39)
        else:
            self.infoCanvas.config(width=305, height=162)
            self.infoCanvas.itemconfigure(self.infoCanvasDescription, font="Arial 9", width=260)
            self.infoCanvas.itemconfigure(self.infoCanvasTitle, font="Arial 15")
            self.infoCanvas.coords(self.intoInfoCanvas, 8, 0, 305, 269)
            self.infoCanvas.coords(self.infoCanvasDescription, 23, 40)
            if isLast: self.infoCanvas.coords(self.intoInfoCanvas, 0, 0, 297, 269)

    def outCanvas(self):
        self.infoCanvas.place_forget()



class GameView:
    def __init__(self, master: Frame, game):
        logFrame.place_forget()
        shopFrame.place_forget()
        regFrame.place_forget()
        profFrame.place_forget()
        editProfileFrame.place_forget()
        gameViewFrame.place(relx=0, rely=0.1)

        self.master = master
        self.game = game

        self.widgets()

    def widgets(self):
        Label(self.master, font="Arial 25", text=self.game["name"], anchor=NW, background=BG_COLOR, fg="#ffffff").place(relx=0.2, rely=0.08)
        self.canvas = Canvas(self.master, width=800, height=400, background="#18222D", highlightcolor="#C6D4DF", highlightbackground="#C6D4DF", highlightthickness=1)
        image = ImageTk.PhotoImage(self.game["image"].resize((500, 290)))
        self.canvas.create_image(0, 0, image=image, anchor=NW)
        self.canvas.image = image
        self.canvas.create_text(530, 15, text=self.game["name"], font="Arial 24", fill="#ffffff", anchor=NW)
        self.canvas.create_text(530, 60, text=self.game["description"], font="Arial 12", fill="#C6D4DF", width=250, anchor=NW)
        self.canvas.place(relx=0.2, rely=0.2)
        btnImg = ImageTk.PhotoImage(Image.open("images/basketButtonGrad.png").resize((700, 50)))
        btn = Button(self.master, image=btnImg, width=700, height=50, command=self.basket, border=0, borderwidth=0)
        btn.place(relx=0.23, rely=0.65)
        btn.image = btnImg
        Label(self.master, text="Купить", fg="#ffffff", font="Arial 15", background="#609529").place(relx=0.477, rely=0.666)

    def basket(self):
        if shopHeaderOfficeBtn["text"] == "USER":
            showerror("Ошибка", "Вы должны зайти в аккаунт, чтобы купить игру.")
        else:
            with open("Files/usersData.json", "r") as FileHandler:
                usersData = json.loads(FileHandler.readline())

            try:
                with open("Files/usersData.json", "wb") as FileHandler:
                    json.dump({}, FileHandler)
            except Exception as e:
                print("Файл очистился.")

            with open("Files/usersData.json", "w") as FileHandler:
                for key, val in usersData.items():
                    if key.lower() == shopHeaderOfficeBtn["text"].lower():
                        if not(self.game["name"] in usersData[key]["games"]):
                            usersData[key]["games"].append(self.game["name"])
                            showinfo("Успешно!", "Вы успешно купили игру.")
                        else:
                            showerror("Ошибка", "У вас уже имеется эта игра.")
                        json.dump(usersData, FileHandler)


class Login:
    def __init__(self, master: Frame):
        self.master = master
        self.widgets()
        regFrame.place_forget()
        shopFrame.place_forget()
        gameViewFrame.place_forget()
        profFrame.place_forget()
        editProfileFrame.place_forget()
        logFrame.place(relx=0, rely=0.1)


    def widgets(self):
        LOG_BG_COLOR = "#212429"
        LOG_TEXT_COLOR = "#B8B6B4"
        LOG_BG_COLOR_ENTRY = "#32353C"

        self.canvas = Canvas(self.master, width=500, height=300, background=LOG_BG_COLOR, highlightthickness=0)
        self.canvas.place(relx=0.26, rely=0.2)

        Label(self.master, text="Игровое имя", font="Arial 12", fg="#1A9FFF", anchor=NW, background=LOG_BG_COLOR).place(relx=0.268, rely=0.23)
        self.gameNameEntry = Entry(self.master, width=50, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.gameNameEntry.place(relx=0.27, rely=0.266, height=35)

        Label(self.master, text="Пароль", font="Arial 12", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.268, rely=0.38)
        self.passwordEntry = Entry(self.master, width=50, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.passwordEntry.place(relx=0.27, rely=0.416, height=35)

        Button(self.master, text="Войти в аккаунт", background="#1A9FFF", width=18, height=3, fg="#ffffff", font="Arial 10", command=self.usLogin).place(relx=0.4, rely=0.5)


    def checkEntries(self, value, valueInStr, minL, maxL):
        if len(value) < minL or len(value) > maxL:
            showerror("Ошибка", f"Количество символов в {valueInStr} должно быть больше {minL} и меньше {maxL}.")
            return True
        return False

    def usLogin(self):
        gameName = self.gameNameEntry.get()
        password = self.passwordEntry.get()


        if self.checkEntries(gameName, "игровом имени", 4, 24): return
        if self.checkEntries(password, "пароле", 4, 32): return

        hasFinded = False

        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        for key, val in usersData.items():
            if key == gameName and val["password"] == password:
                hasFinded = True
                turnOnProf(account=val, cong=False)

        if not(hasFinded):
            showerror("Ошибка", "Такого аккаунта не существует!")



class Registration:
    def __init__(self, master: Frame):
        self.master = master
        shopFrame.place_forget()
        profFrame.place_forget()
        logFrame.place_forget()
        gameViewFrame.place_forget()
        editProfileFrame.place_forget()
        regFrame.place(relx=0, rely=0.1)
        if shopHeaderOfficeBtn["text"] == "USER":
            self.widgets()
        else:
            with open("Files/usersData.json", "r") as FileHandler:
                usersData = json.loads(FileHandler.readline())
                for key, val in usersData.items():
                    if shopHeaderOfficeBtn["text"].lower() == key.lower():
                        turnOnProf(val)
                        break


    def widgets(self):
        imgCanvas = Canvas(self.master, width=1284, height=718, background="#ff0000", highlightthickness=0)
        oldImg = Image.open("images/userBackPhone.png").resize((1288, 798))
        myImg = ImageTk.PhotoImage(oldImg)
        imgCanvas.create_image(0, -2, anchor=NW, image=myImg)
        imgCanvas.image = myImg

        imgCanvas.place(relx=0, rely=0)
        LOG_BG_COLOR = "#212429"
        LOG_TEXT_COLOR = "#B8B6B4"
        LOG_BG_COLOR_ENTRY = "#32353C"
        Label(self.master, text="СОЗДАНИЕ АККАУНТА", font="Arial 25", fg="#ffffff", anchor=NW, background=LOG_BG_COLOR).place(relx=0.2, rely=0.1)
        Label(self.master, text="Ваше имя", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR). place(relx=0.2, rely=0.2)
        self.nameEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.nameEntry.place(relx=0.2, rely=0.236, height=35)
        Label(self.master, text="Ваше игровое имя", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.2, rely=0.35)
        self.gameNameEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.gameNameEntry.place(relx=0.2, rely=0.386, height=35)
        Label(self.master, text="Пол", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.2, rely=0.486)

        self.gender = StringVar(value="male")
        genderCanvas = Canvas(self.master, width=350, height=40, background=LOG_BG_COLOR, highlightthickness=2, highlightbackground=LOG_BG_COLOR_ENTRY)
        genderCanvas.place(relx=0.2, rely=0.5232)

        self.maleRadioBtn = Radiobutton(self.master, text="Мужчина", value="male", variable=self.gender, background=LOG_BG_COLOR, fg="#ffffff", font="Arial 10")
        self.femaleRadioBtn = Radiobutton(self.master, text="Женщина", value="female", variable=self.gender, background=LOG_BG_COLOR, fg="#ffffff", font="Arial 10")
        self.maleRadioBtn.place(relx=0.23, rely=0.53, height=35)
        self.femaleRadioBtn.place(relx=0.38, rely=0.53, height=35)
        Label(self.master, text="Адрес эл. почты", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.6, rely=0.2)
        self.emailEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.emailEntry.place(relx=0.6, rely=0.236, height=35)
        Label(self.master, text="Пароль", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.6, rely=0.35)
        self.passwordEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.passwordEntry.place(relx=0.6, rely=0.386, height=35)
        Label(self.master, text="Подтвердите пароль", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.6, rely=0.5)
        self.passwordConfirmEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.passwordConfirmEntry.place(relx=0.6, rely=0.536, height=35)

        captchaCanvas = Canvas(self.master, width=280, height=78, background="#222222", highlightthickness=1, highlightbackground=LOG_TEXT_COLOR)
        self.captchaValue = IntVar()
        captchaCheckBox = Checkbutton(self.master, variable=self.captchaValue, text="Я не робот", fg="#ffffff", background="#222222", font="Arial 12", border=0, borderwidth=0)
        img = ImageTk.PhotoImage(Image.open("images/captcha.png").resize((35, 35)))
        captchaCanvas.create_image(240, 32, image=img)
        captchaCanvas.image = img
        captchaCheckBox.place(relx=0.22, rely=0.636)
        captchaCanvas.place(relx=0.2, rely=0.6)
        captchaCanvas.create_text(240, 60, text="reCaptcha", fill="#ffffff")

        self.confirmCheckValue = IntVar()
        self.confirmCheckBtn = Checkbutton(self.master, variable=self.confirmCheckValue, font="Arial 10", background=LOG_BG_COLOR, text="Я подтверждаю, что мне исполнилось 13 лет, и соглашаюсь с условиями соглашения подписчика Steam и политикой конфиденциальности Valve.", fg="#ffffff")
        self.confirmCheckBtn.place(relx=0.2, rely=0.73)

        btnImg = ImageTk.PhotoImage(Image.open("images/buttonGradient.png").resize((900, 35)))
        self.confirmBtn = Button(self.master, image=btnImg, font="Arial 11", border=0, borderwidth=0, width=900, height=35, fg="#000000", command=self.register)
        Label(self.master, text="Зарегистрироваться", fg="#ffffff", font="Arial 11", background="#4B90E5").place(relx=0.48, rely=0.83)
        self.confirmBtn.image = btnImg
        self.confirmBtn.place(relx=0.2, rely=0.82)

        Button(self.master, text="Уже есть аккаунт?", fg="#808080", background=LOG_BG_COLOR, border=0, command=lambda: turnOnLog()).place(relx=0.2, rely=0.9)

    def checkEntries(self, value, valueInStr, minL, maxL):
        if len(value) < 4 or len(value) > 18:
            showerror("Ошибка", f"Количество символов в {valueInStr} должно быть больше {minL} и меньше {maxL}.")
            return True
        return False

    def register(self):
        name = self.nameEntry.get()
        gameName = self.gameNameEntry.get()
        gender = self.gender.get()
        email = self.emailEntry.get()
        password = self.passwordEntry.get()
        confirmPassword = self.passwordConfirmEntry.get()
        captchaVal = self.captchaValue.get()
        yearVal = self.confirmCheckValue.get()



        if self.checkEntries(name, "имени", 4, 18): return
        if self.checkEntries(gameName, "нике", 4, 24): return
        if self.checkEntries(email, "адресе эл. почты", 4, 32): return
        if not("@gmail.com" in email) and not("@mail.ru" in email):
            showerror("Ошибка", "В адресе эл. почты должны присутствовать домены.")
            return

        if self.checkEntries(password, "пароле", 4, 32): return

        if confirmPassword != password:
            showerror("Ошибка", "Пароли не совпадают.")
            return

        if not(captchaVal):
            showerror("Ошибка", "Вы должны подтвердить, что вы не робот.")
            return

        if not(yearVal):
            showerror("Ошибка", "Вы должны согласиться с условиями выше.")
            return

        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        try:
            with open("Files/usersData.json", "wb") as FileHandler:
                json.dump({}, FileHandler)
        except Exception as e:
            print("Файл очистился.")

        with open("Files/usersData.json", "w") as FileHandler:
            slov = {
                "name": name,
                "gameName": gameName,
                "gender": gender,
                "email": email,
                "password": password,
                "description": "Информация отсутствует.",
                "friends": [],
                "games": [],
                "avatar": "",
                "requestsOnFriends": []
            }
            usersData[gameName] = slov
            json.dump(usersData, FileHandler)

        turnOnProf(account=slov, cong=True)






class Profile:
    def __init__(self, master: Frame, account, isCong = False):
        self.passedGameCount = 0
        self.gamesList = []
        self.hasMoreGames = False
        self.passedFriendCount = 0
        self.friendsList = []
        self.hasMoreFriends = False
        self.master = master
        self.listForfBtns = [False, False, False]
        self.account = account
        self.flag = False
        shopFrame.place_forget()
        regFrame.place_forget()
        logFrame.place_forget()
        gameViewFrame.place_forget()
        editProfileFrame.place_forget()
        shopHeaderOfficeBtn.config(text=account["gameName"].upper())
        profFrame.place(relx=0, rely=0.1)

        if isCong:
            self.canvas = Canvas(self.master, width=300, height=200, background="#363537", highlightthickness=0)
            self.canvas.create_text(86, 15, text="Поздравления", font="Arial 15", fill="#ffffff", anchor=NW)
            self.canvas.create_text(20, 100, text="Вы успешно зарегистрировались!", font="Arial 13", fill="#ffffff", anchor=NW)
            self.congBtn = Button(self.master, text="Продолжить", fg="#ffffff", background="#006494", width=30, height=2, command=self.destroyCong)
            self.congBtn.place(relx=0.41, rely=0.6)
            self.canvas.place(relx=0.38, rely=0.4)
        else:
            self.widgets()

    def destroyCong(self):
        self.canvas.destroy()
        self.congBtn.destroy()
        self.widgets()


    def widgets(self):
        self.mainCanvas = Canvas(self.master, width=1000, height=718, background="#001021", highlightthickness=0)
        self.mainCanvas.place(relx=0.14, rely=0)
        TEXT_COLOR = "#B8B6B4"

        borderCanvas = Canvas(self.master, width=450, height=200, background="#2b2d42", highlightthickness=1, highlightcolor=TEXT_COLOR)
        borderCanvas.place(relx=0.52, rely=0.02)

        profImg = ""
        if self.account["avatar"] == "":
            profImg = ImageTk.PhotoImage(Image.open("images/guest.png").resize((160, 160)))
        else:
            profImg = ImageTk.PhotoImage(Image.open(self.account["avatar"]).resize((160, 160)))
        self.mainCanvas.create_image(20, 20, image=profImg, anchor=NW)
        self.mainCanvas.image = profImg
        self.mainCanvas.create_text(200, 30, text=self.account["gameName"], anchor=NW, font="Arial 16 bold", fill="#ffffff")
        self.mainCanvas.create_text(200, 80, text=self.account["description"], anchor=NW, width=400, font="Arial 11", fill=TEXT_COLOR)
        borderCanvas.create_text(10, 20, text="ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ", anchor=NW, font="Arial 19", fill="#ffffff")
        borderCanvas.create_text(10, 70, text="Имя:", anchor=NW, font="Arial 13", fill=TEXT_COLOR)
        borderCanvas.create_text(55, 70, text=self.account["name"], anchor=NW, font="Arial 12", fill="#ffffff")
        borderCanvas.create_text(10, 100, text="Пол:", anchor=NW, font="Arial 13", fill=TEXT_COLOR)
        borderCanvas.create_text(55, 100, text=self.account["gender"], anchor=NW, font="Arial 12", fill="#ffffff")
        borderCanvas.create_text(10, 130, text="Почта:", anchor=NW, font="Arial 13", fill=TEXT_COLOR)
        borderCanvas.create_text(70, 130, text=self.account["email"], anchor=NW, font="Arial 12", fill="#ffffff")
        borderCanvas.create_text(10, 160, text="Пароль:", anchor=NW, font="Arial 13", fill=TEXT_COLOR)
        borderCanvas.create_text(80, 160, text=self.account["password"], anchor=NW, font="Arial 12", fill="#ffffff")

        Button(self.master, width=15, height=2, text="Редактировать", background="#2C4251", fg="#ffffff", border=0, command=self.editProf).place(relx=0.3, rely=0.196)

        self.mainCanvas.create_text(20, 250, text="ИГРЫ", font="Arial 27", fill="#ffffff", anchor=NW)

        self.mainCanvas.create_rectangle(44, 308, 647, 689, fill="#001021", outline="#ff0000")
        if len(self.account["games"]) > 3:
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="<--").place(relx=0.15, rely=0.65)
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="-->", command=self.addGames).place(relx=0.65, rely=0.65)
            self.hasMoreGames = True
        elif len(self.account["games"]) == 0:
            self.mainCanvas.create_text(60, 390, text="У вас нет игр.", font="Arial 20", fill=TEXT_COLOR, anchor=NW)

        self.addGames()

        self.mainCanvas.create_text(720, 250, text="ДРУЗЬЯ", font="Arial 27", fill="#ffffff", anchor=NW)
        self.mainCanvas.create_rectangle(710, 308, 960, 689, fill="#001021", outline="#ff0000")
        if len(self.account["friends"]) > 3:
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="<--").place(relx=0.15, rely=0.65)
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="-->", command=self.addFriends).place(relx=0.65, rely=0.65)
        elif len(self.account["friends"]) == 0:
            self.mainCanvas.create_text(725, 470, text="У вас нет друзей.", font="Arial 20", fill=TEXT_COLOR, anchor=NW)

        # self.addFriends()


    def addFriends(self):
        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        for i in self.account["friends"]:
            self.friendsList.append(usersData[i])

        hasEndedFriends = False
        posY = 0.43

        self.friendsInfo = []
        self.friendsCanvas = []
        listForBtns = [False, False, False]

        for i in range(3):
            if i + 1 > len(self.friendsList) - self.passedFriendCount:
                self.passedFriendCount = len(self.friendsList)
                hasEndedFriends = True
                break

            curFriend = self.friendsList[i + self.passedFriendCount]

            friendCanvas = Canvas(self.master, background="#7c98b3", width=247, height=120, highlightthickness=1, highlightcolor="#bccce0")

            avaImg = ImageTk.PhotoImage(Image.open("images/guest.png").resize((120, 120)))
            if curFriend["avatar"]:
                avaImg = ImageTk.PhotoImage(Image.open(curFriend["avatar"]).resize((120, 120)))
            friendCanvas.create_image(0, 0, image=avaImg, anchor=NW)
            friendCanvas.image = avaImg

            friendCanvas.create_text(130, 10, text=curFriend["gameName"], font="Arial 13", fill="#ffffff", anchor=NW)

            listForBtns[i] = True

            self.friendsInfo.append(curFriend)
            self.friendsCanvas.append(friendCanvas)

            friendCanvas.place(relx=0.694, rely=posY)
            posY += 0.18

        if listForBtns[0]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteFriend(self.friendsInfo[0])).place(relx=0.8, rely=0.52)
        if listForBtns[1]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteFriend(self.friendsInfo[1])).place(relx=0.8, rely=0.52 + 0.18)
        if listForBtns[2]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteFriend(self.friendsInfo[2])).place(relx=0.8, rely=0.52 + 0.36)

        if not(hasEndedFriends):
            self.passedFriendCount += 3
    def editProf(self):
        turnOnEditingProf(self.account)

    def deleteFriend(self, friend):
        ...

    def addGames(self):
        with open("Files/gamesData.json", "r") as FileHandler:
            gamesData = json.loads(FileHandler.readline())

        for i in self.account["games"]:
            self.gamesList.append(gamesData[i])

        hasEndedGames = False
        posY = 0.43

        self.gamesInfo = []
        self.gamesCanvas = []
        self.listForfBtns = [False, False, False]

        for i in range(3):
            if i + 1 > len(self.gamesList) - self.passedGameCount:
                self.passedGameCount = len(self.gamesList)
                hasEndedGames = True
                break

            curGame = self.gamesList[i + self.passedGameCount]

            gameCanvas = Canvas(self.master, background="#7c98b3", width=600, height=120, highlightthickness=1, highlightcolor="#bccce0")

            gameImg = ImageTk.PhotoImage(Image.open(curGame["image"]).resize((210, 120)))
            gameCanvas.create_image(0, 0, image=gameImg, anchor=NW)
            gameCanvas.image = gameImg

            gameCanvas.create_text(220, 10, text=curGame["name"], font="Arial 14", fill="#ffffff", anchor=NW)
            gameCanvas.create_text(220, 35, text=curGame["description"], font="Arial 10", fill="#ffffff", anchor=NW, width=250)
            gameCanvas.place(relx=0.175, rely=posY)

            self.gamesInfo.append(curGame)
            self.gamesCanvas.append(gameCanvas)
            self.listForfBtns[i] = True

            posY += 0.18
        print(len(self.gamesList) - self.passedGameCount)

        if self.listForfBtns[0]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteGame(self.gamesInfo[0])).place(relx=0.555, rely=0.48)
        if self.listForfBtns[1]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteGame(self.gamesInfo[1])).place(relx=0.555, rely=0.48 + 0.18)
        if self.listForfBtns[2]:
            Button(self.master, width=12, height=2, background='#ff0000', fg="#ffffff", text="Удалить", border=0, command=lambda: self.deleteGame(self.gamesInfo[2])).place(relx=0.555, rely=0.48 + 0.36)


        if not(hasEndedGames):
            self.passedGameCount += 3

    def deleteGame(self, game):
        print(game)
        answer = askyesno("Предупреждение", "Вы действительно хотите удалить эту игру?")
        if answer:
            print(game["name"])
            with open("Files/usersData.json", "r") as FileHandler:
                usersData = json.loads(FileHandler.readline())

            try:
                with open("Files/usersData.json", "wb") as FileHandler:
                    json.dump({}, FileHandler)
            except Exception as e:
                print("Файл очистился.")

            with open("Files/usersData.json", "w") as FileHandler:
                for key, val in usersData.items():
                    if shopHeaderOfficeBtn["text"].lower() == self.account["gameName"]:
                        print("HAHAHAHAHAH")
                        self.listForfBtns = [False, False, False]
                        print(self.account)
                        print(usersData[key]["games"])
                        usersData[key]["games"].remove(game["name"])
                        self.account["games"].remove(game["name"])
                        json.dump(usersData, FileHandler)
                        turnOnProf(self.account)
        else:
            print('ADASDDSA')
            turnOnProf(self.account)


class EditingProfile:
    def __init__(self, master: Frame, account):
        self.master = master
        self.account = account
        self.requestsList = []
        print(self.account)
        self.passedRequestCount = 0
        shopFrame.place_forget()
        regFrame.place_forget()
        logFrame.place_forget()
        gameViewFrame.place_forget()
        profFrame.place_forget()
        editProfileFrame.place(relx=0, rely=0.1)

        self.widgets()

    def widgets(self):
        LOG_BG_COLOR = "#001021"
        LOG_TEXT_COLOR = "#B8B6B4"
        LOG_BG_COLOR_ENTRY = "#32353C"

        self.mainCanvas = Canvas(self.master, width=950, height=718, background="#001021", highlightthickness=0)
        self.borderCanvas1 = Canvas(self.master, width=500, height=640, background=LOG_BG_COLOR, highlightthickness=1, highlightcolor="#808080")
        self.borderCanvas1.place(relx=0.15, rely=0.04)
        self.mainCanvas.place(relx=0.14, rely=0)

        self.borderCanvas1.create_text(70, 30, text="РЕДАКТИРОВАТЬ", font="Arial 30", fill="#ffffff", anchor=NW)
        self.mainCanvas.create_text(575, 30, text="ЗАПРОСЫ В ДРУЗЬЯ", font="Arial 24", fill="#ffffff", anchor=NW)

        Label(self.master, text="Ваше игровое имя", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.23, rely=0.16)
        self.gameNameEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.gameNameEntry.place(relx=0.23, rely=0.196, height=35)
        print(self.account)
        self.gameNameEntry.insert(0, self.account["gameName"])

        Label(self.master, text="Адрес эл. почты", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.16, rely=0.32)
        self.emailEntry = Entry(self.master, width=25, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.emailEntry.place(relx=0.16, rely=0.356, height=35)
        self.emailEntry.insert(0, self.account["email"])

        Label(self.master, text="Описание", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.354, rely=0.32)
        self.descriptionEntry = Entry(self.master, width=25, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.descriptionEntry.place(relx=0.354, rely=0.356, height=35)
        self.descriptionEntry.insert(0, self.account["description"])

        Label(self.master, text="Пароль", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.16, rely=0.48)
        self.passwordEntry = Entry(self.master, width=25, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.passwordEntry.place(relx=0.16, rely=0.516, height=35)
        self.passwordEntry.insert(0, self.account["password"])

        Label(self.master, text="Я забыл", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.354, rely=0.48)
        self.smthEntry = Entry(self.master, width=25, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.smthEntry.place(relx=0.354, rely=0.516, height=35)
        self.smthEntry.insert(0, self.account["password"])

        Label(self.master, text="Аватар", font="Arial 11", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.225, rely=0.64)
        Label(self.master, text="(необязательно)", font="Arial 9", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.2695, rely=0.641)
        Label(self.master, text="Вставьте ссылку на фото", font="Arial 8", fg=LOG_TEXT_COLOR, anchor=NW, background=LOG_BG_COLOR).place(relx=0.223, rely=0.73)
        self.avatarEntry = Entry(self.master, width=30, font="Arial 13", fg="#ffffff", background="#32353C", border=0)
        self.avatarEntry.place(relx=0.225, rely=0.676, height=35)
        self.avatarEntry.insert(0, self.account["avatar"])

        btnImg = ImageTk.PhotoImage(Image.open("images/buttonGradient.png").resize((403, 38)))
        self.confirmBtn = Button(self.master, image=btnImg, font="Arial 11", border=0, borderwidth=0, width=400, height=35, fg="#000000", command=self.confirmChanges)
        self.confirmBtn.image = btnImg
        self.confirmBtn.place(relx=0.18, rely=0.8)
        Label(self.master, text="Подтвердить", fg="#ffffff", font="Arial 11", background="#4A90E5").place(relx=0.3, rely=0.809)

        self.friendsCanvas = Canvas(self.master, width=350, height=570, bg=LOG_BG_COLOR, highlightthickness=1, highlightcolor="#808080")
        self.friendsCanvas.place(relx=0.58, rely=0.13)

        if len(self.account["requestsOnFriends"]) > 4:
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="<--").place(relx=0.555, rely=0.52)
            Button(self.master, width=3, height=1, border=0, background="#001021", fg="#ffffff", text="-->", command=self.addRequests).place(relx=0.857, rely=0.52)


        self.addRequests()


    def confirmChanges(self):
        gameName = self.gameNameEntry.get()
        email = self.emailEntry.get()
        description = self.descriptionEntry.get()
        password = self.passwordEntry.get()
        avatar = self.avatarEntry.get()

        if self.checkEntries(gameName, "игровом имени", 4, 24): return
        if self.checkEntries(email, "адресе эл. почты", 4, 32): return
        if self.checkEntries(description, "описании", 6, 50): return
        if self.checkEntries(password, "пароле", 4, 32): return

        try:
            if avatar:
                img = ImageTk.PhotoImage(Image.open(f"{avatar}").resize((300, 300)))
        except Exception as e:
            showerror("Ошибка", "Ссылка на аватар некорректная.")
            return

        oldAccValue = self.account
        oldGameName = self.account["gameName"]



        print(self.account)
        self.account["gameName"] = gameName
        self.account["email"] = email
        self.account["description"] = description
        self.account["password"] = password
        self.account["avatar"] = avatar
        print(self.account)

        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())


        usersData.pop(oldGameName)
        usersData[gameName] = self.account

        for key, val in usersData.items():
            if range(len(val["requestsOnFriends"])):
                for i in range(len(val["requestsOnFriends"])):
                    print(i)
                    if usersData[key]["requestsOnFriends"][i] == oldGameName:
                        usersData[key]["requestsOnFriends"][i] = gameName

            if range(len(val["friends"])):
                for i in range(len(val["friends"])):
                    print(usersData[key]["friends"][i])
                    if usersData[key]["friends"][i] == oldGameName:
                        usersData[key]["friends"][i] = gameName



        try:
            with open("Files/usersData.json", "wb") as FileHandler:
                json.dump({}, FileHandler)
        except Exception as e:
            print("Файл очистился.")

        with open("Files/usersData.json", "w") as FileHandler:
            json.dump(usersData, FileHandler)


        turnOnProf(account=self.account)

    def addRequests(self):
        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        for i in self.account["requestsOnFriends"]:
            self.requestsList.append(i)

        self.reqHumans = []
        for i in self.requestsList:
            self.reqHumans.append(usersData[i])
        print(self.reqHumans)


        hasEndedGames = False
        posY = 0.131

        self.requestsInfo = []
        self.requestsCanvas = []
        listForBtns = [False, False, False, False, False]

        for i in range(4):
            if i + 1 > len(self.reqHumans) - self.passedRequestCount:
                self.passedRequestCount = len(self.reqHumans)
                hasEndedGames = True
                break

            curRequest = self.reqHumans[i + self.passedRequestCount]

            requestCanvas = Canvas(self.master, width=350, height=100, background="#2C365E", highlightthickness=0)
            requestCanvas.place(relx=0.581, rely=posY)

            requestCanvas.create_rectangle(0, 0, 100, 100, fill="#202020")
            requestCanvas.create_text(115, 5, text=curRequest["gameName"], anchor=NW, fill="#ffffff", font="Arial 22")

            self.requestsInfo.append(curRequest)



            listForBtns[i] = True

            posY += 0.18

        print(len(self.reqHumans) - self.passedRequestCount)
        if listForBtns[0]:
            Button(self.master, width=12, background='#47A76A', fg="#ffffff", text="Принять", border=0, command=lambda: self.acceptRequest(self.requestsInfo[0])).place(height=35, relx=0.67, rely=0.2)
            Button(self.master, width=12, background='#9B2D30', fg="#ffffff", text="Отклонить", border=0, command=lambda: self.rejectRequest(self.requestsInfo[0])).place(height=35, relx=0.77, rely=0.2)
        if listForBtns[1]:
            Button(self.master, width=12, background='#47A76A', fg="#ffffff", text="Принять", border=0, command=lambda: self.acceptRequest(self.requestsInfo[1])).place(height=35, relx=0.67, rely=0.2 + 0.18)
            Button(self.master, width=12, background='#9B2D30', fg="#ffffff", text="Отклонить", border=0, command=lambda: self.rejectRequest(self.requestsInfo[1])).place(height=35, relx=0.77, rely=0.2 + 0.18)
        if listForBtns[2]:
            Button(self.master, width=10, background='#47A76A', fg="#ffffff", text="Принять", border=0, command=lambda: self.acceptRequest(self.requestsInfo[2])).place(height=35, relx=0.67, rely=0.2 + 0.36)
            Button(self.master, width=12, background='#9B2D30', fg="#ffffff", text="Отклонить", border=0, command=lambda: self.rejectRequest(self.requestsInfo[2])).place(height=35, relx=0.77, rely=0.2 + 0.36)
        if listForBtns[3]:
            Button(self.master, width=12, background='#47A76A', fg="#ffffff", text="Принять", border=0, command=lambda: self.acceptRequest(self.requestsInfo[3])).place(height=35, relx=0.67, rely=0.2 + 0.36)
            Button(self.master, width=12, background='#9B2D30', fg="#ffffff", text="Отклонить", border=0, command=lambda: self.rejectRequest(self.requestsInfo[3])).place(height=35, relx=0.77, rely=0.2 + 0.36)

        if not(hasEndedGames):
            self.passedRequestCount += 3

    def acceptRequest(self, human):
        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        print(human["gameName"])
        usersData[self.account["gameName"]]["requestsOnFriends"].remove(human["gameName"])
        usersData[self.account["gameName"]]["friends"].append(human["gameName"])
        usersData[human["gameName"]]["friends"].append(self.account["gameName"])
        if self.account["gameName"] in usersData[human["gameName"]]["requestsOnFriends"]:
            usersData[human["gameName"]]["requestsOnFriends"].remove(self.account["gameName"])

        self.account = usersData[self.account["gameName"]]

        try:
            with open("Files/usersData.json", "wb") as FileHandler:
                json.dump({}, FileHandler)
        except Exception as e:
            print("Файл очистился.")

        with open("Files/usersData.json", "w") as FileHandler:
            json.dump(usersData, FileHandler)

        turnOnEditingProf(self.account)

    def rejectRequest(self, human):
        with open("Files/usersData.json", "r") as FileHandler:
            usersData = json.loads(FileHandler.readline())

        usersData[self.account["gameName"]]["requestsOnFriends"].remove(human["gameName"])
        self.account = usersData[self.account["gameName"]]
        print(human["gameName"])

        try:
            with open("Files/usersData.json", "wb") as FileHandler:
                json.dump({}, FileHandler)
        except Exception as e:
            print("Файл очистился.")

        with open("Files/usersData.json", "w") as FileHandler:
            json.dump(usersData, FileHandler)

        turnOnEditingProf(self.account)


    def checkEntries(self, value, valueInStr, minL, maxL):
        if len(value) < minL or len(value) > maxL:
            showerror("Ошибка", f"Количество символов в {valueInStr} должно быть больше {minL} и меньше {maxL}.")
            return True
        return False


def turnOnUser():
    registr = Registration(regFrame)
    activeBtnUnderline(shopHeaderOfficeBtn, shopHeaderShopBtn)

def turnOnShop():
    shop = Shop(shopFrame)
    activeBtnUnderline(shopHeaderShopBtn, shopHeaderOfficeBtn)

def turnOnProf(account, cong=False):
    profile = Profile(profFrame, account=account, isCong=cong)

def turnOnLog():
    log = Login(logFrame)

def turnOnGameView(game):
    gameView = GameView(gameViewFrame, game)

def turnOnEditingProf(account):
    # for widget in editProfileFrame.winfo_children():
    #     widget.destroy()
    editProfile = EditingProfile(editProfileFrame, account=account)


if __name__ == '__main__':
    shopRoot = Tk()
    shopRoot.title("Steam")
    shopRoot.geometry("1284x798+160+20")
    shopRoot.resizable(False, False)
    shopRoot.config(background=BG_COLOR)
    shopFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    regFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    profFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    logFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    gameViewFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    editProfileFrame = Frame(shopRoot, width=1284, height=718, background=BG_COLOR)
    shopFrame.place(relx=0, rely=0.1)


    #Добавление кнопок на шапку программы
    shopHeaderShopBtn = Button(shopRoot, text="МАГАЗИН", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16", command=turnOnShop, anchor=NW)
    shopHeaderLibraryBtn = Button(shopRoot, text="БИБЛИОТЕКА", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16", anchor=NW)
    shopHeaderOfficeBtn = Button(shopRoot, text="USER", background=BG_COLOR, fg="#ffffff", borderwidth=0, font="Arial 16 underline", command=turnOnUser, anchor=NW)

    shopHeaderShopBtn.place(relx=0.35, rely=0.036)
    shopHeaderLibraryBtn.place(relx=0.45, rely=0.036)
    shopHeaderOfficeBtn.place(relx=0.585, rely=0.036)
    activeBtnUnderline(shopHeaderShopBtn, shopHeaderOfficeBtn)
    shop = Shop(shopFrame)

    # with open("Files/usersData.json", "r") as FileHandler:
    #     usersData = json.loads(FileHandler.readline())
    #
    # acc = {}
    # for key, val in usersData.items():
    #     if key == "baxaba123":
    #         acc = val
    #
    # turnOnProf(acc)
    shopRoot.mainloop()