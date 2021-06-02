import tkinter as tk
import configReader
settings = configReader.readSettings()


class Canvas:
    def __init__(self):
        self.wonGame = False
        self.quitProgram = False
        self.pausedProgram = False
        self.currentTeam = None
        self.board = self.createBoardComputer()
        self.tkwindow = tk.Tk()
        # self.Frame = tk.Frame
        self.window = tk.Canvas(
            self.tkwindow, width=settings['window']['width'], height=settings['window']['height'], bg="peach puff")
        self.window.pack()
        self.teamPiecesInactive = []
        self.teamPiecesActive = []
        self.teams = self.developTeams()
        self.createPieces()
        self.decals = []
        self.__menu__()
        self.nextTurn = True
        self.__boardDecals__()

    def __boardDecals__(self):
        quadrantSize = settings['window']['width'] / settings['board']['width']
        for quad in range(settings['board']['width']):
            self.decals.append(
                self.window.create_line(
                    quadrantSize * quad,
                    quadrantSize,
                    quadrantSize * quad,
                    settings['window']['height'],
                    fill='black', width=settings['board']['lineSize']
                )
            )
        for quad in range(1, 1 + settings['board']['height']):
            self.decals.append(
                self.window.create_line(
                    0,
                    quadrantSize * quad,
                    settings['window']['width'],
                    quadrantSize * quad,
                    fill='black', width=settings['board']['lineSize']
                )
            )

    def __menu__(self):
        self.font = ("Verdana", 10)
        self.menu = tk.Menu(self.window, bg='orange')
        self.fileList = tk.Menu(tearoff=0)
        self.difficultyList = tk.Menu(tearoff=0)
        self.fileListSelection()
        self.difficultyListSelection()
        self.menu.add_cascade(label='File', menu=self.fileList)
        self.menu.add_cascade(label='Difficulty', menu=self.difficultyList)
        self.tkwindow.config(menu=self.menu)

    def fileListSelection(self):
        self.fileList.add_command(label='Pause', font=self.font, command=self.pauseProgram)
        self.fileList.add_command(label='Exit', font=self.font, command=self.exitProgram)
        self.fileList.add_command(label='Reset', font=self.font, command=self.resetProgram)

    def difficultyListSelection(self):
        self.difficultyList.add_command(label='Difficulty', font=self.font, command=self.changeDifficulty)
        self.difficultyList.add_command(label='AIState', font=self.font, command=self.changeTeamState)

    def __createBorder__(self):
        pass

    def createPieces(self):
        for newPiece in range(settings['board']['width'] * settings['board']['height']):
            self.teamPiecesInactive.append(Piece(self.window))

    @staticmethod
    def Coord(coord, quadrantSize):
        x = (settings['board']['lineSize'] / 2) + (coord[1] * quadrantSize[1])
        y = (1 + coord[0]) * quadrantSize[0] + (settings['board']['lineSize'] / 2)
        return tuple((y, x))

    def activatePiece(self, coord, color, team):
        newPiece = self.teamPiecesInactive[0]
        self.teamPiecesInactive.pop(0)
        xQuadrantSize = settings['window']['width'] / settings['board']['width']
        yQuadrantSize = settings['window']['width'] / settings['board']['width']
        coord = self.Coord(coord, (yQuadrantSize, xQuadrantSize))
        newPiece.__firstCreation__(coord[1], coord[0], color, team, xQuadrantSize - settings['board']['lineSize'])
        self.teamPiecesActive.append(newPiece)

    def deactivatePieces(self):
        for circle in reversed(self.teamPiecesActive):
            circle.removeObject()
            self.teamPiecesInactive.append(circle)
            self.teamPiecesActive.pop(-1)

    @staticmethod
    def createBoardComputer():
        board = []
        for y in range(settings['board']['height']):
            row = []
            for x in range(settings['board']['width']):
                row.append(' ')
            board.append(row)
        return board

    @staticmethod
    def developTeams():
        listOfTeams = {}
        for num in range(settings['teams']['TeamCount']):
            listOfTeams.update({
                f"Team{num}": {
                    "AI": True,
                    "Piece": settings['teams']['symbols'][num],
                    "Difficulty": settings['recursionDepth'],
                    "Color": settings['teams']['teamColors'][num]
                }})
        return listOfTeams

    def pauseProgram(self):
        """
        This simply pauses and un pauses program based on a menu button press. Simple and easy to understand
        A press of the menu pause button a second time will un pause the program.
        """
        if self.pausedProgram:
            self.pausedProgram = False
        else:
            self.pausedProgram = True
        while self.pausedProgram:
            self.tkwindow.update()
            if self.quitProgram:
                self.tkwindow.quit()
                exit()

    def exitProgram(self):
        self.quitProgram = True

    def resetProgram(self):
        self.deactivatePieces()
        self.board = self.createBoardComputer()
        self.wonGame = False

    def changeDifficulty(self):
        self.tempWindow = tk.Tk()
        self.activetemp = True
        buttonEasy = tk.Button(self.tempWindow, text='Easy', command=lambda: self.difficultySwitch('easy'))
        buttonMedium = tk.Button(self.tempWindow, text='Medium', command=lambda: self.difficultySwitch('medium'))
        buttonHard = tk.Button(self.tempWindow, text='Hard', command=lambda: self.difficultySwitch('hard'))
        buttonImpossible = tk.Button(self.tempWindow, text='Impossible', command=lambda: self.difficultySwitch('impossible'))
        buttonEasy.pack(anchor='nw')
        buttonMedium.pack(anchor='nw')
        buttonHard.pack(anchor='nw')
        buttonImpossible.pack(anchor='nw')
        while self.activetemp:
            self.tkwindow.update()
            self.tempWindow.update()
        self.tempWindow.destroy()
        self.tempWindow.quit()

    def difficultySwitch(self, change):
        if change == 'easy':
            newDif = 0
        elif change == 'medium':
            newDif = 1
        elif change == 'hard':
            newDif = 3
        else:
            newDif = 5
        for team in self.teams:
            self.teams[team]['Difficulty'] = newDif
        self.activetemp = False

    def changeTeamState(self):

        def subChange(event, teamGroup, status, number, ownSelf):
            """ I decided to nest this loop to centralise this process """
            teamGroup['AI'] = status
            # self.window.itemconfig(self.sprite, fill=self.color)
            if event == 'player':
                ownSelf.buttonPack[number * 3 + 1]['state'] = tk.DISABLED
                ownSelf.buttonPack[number * 3 + 2]['state'] = tk.NORMAL
            else:
                ownSelf.buttonPack[number * 3 + 1]['state'] = tk.NORMAL
                ownSelf.buttonPack[number * 3 + 2]['state'] = tk.DISABLED
            return

        self.tempWindow = tk.Frame(tk.Tk())
        self.activetemp = True

        # buttonEasy = tk.Button(self.tempWindow, text='Easy', command=lambda: self.difficultySwitch('easy'))
        self.buttonPack = []
        for num, team in enumerate(self.teams):
            if self.teams[team]['AI']:
                aiState = tk.DISABLED
                playerState = tk.NORMAL
            else:
                aiState = tk.NORMAL
                playerState = tk.DISABLED
            teamLabel = tk.Label(self.tempWindow, text=team, font=self.font)
            buttonPlayer = tk.Button(
                self.tempWindow, text="Player",
                command=lambda n=num: subChange('player', self.teams[team], False, n, self), state=playerState
            )
            buttonAI = tk.Button(
                self.tempWindow, text="AI",
                command=lambda n=num: subChange('ai', self.teams[team], True, n, self), state=aiState
            )
            teamLabel.grid(row=num, column=0)
            buttonPlayer.grid(row=num, column=1)
            buttonAI.grid(row=num, column=2)
            self.buttonPack.append(teamLabel)
            self.buttonPack.append(buttonPlayer)
            self.buttonPack.append(buttonAI)
        # buttonEasy.pack(anchor='nw')
        # buttonMedium.pack(anchor='nw')
        # buttonHard.pack(anchor='nw')
        # buttonImpossible.pack(anchor='nw')
        self.tempWindow.pack()
        print()
        while self.activetemp:
            try:
                self.tkwindow.update()
                self.tempWindow.update()
            except tk.TclError:
                break

        # self.tempWindow.destroy()
        # self.tempWindow.quit()


class Piece:
    def __firstCreation__(self, x, y, color, team, size):
        self.x, self.y = x, y
        self.color = color
        self.team = team
        if self.activated is False:
            self.drawObject(size)
        else:
            self.redraw(size)

    def redraw(self, size):
        self.window.coords(self.sprite, self.x, self.y, self.x + size, self.y + size)
        self.window.itemconfig(self.sprite, fill=self.color)

    def drawObject(self, size):
        self.sprite = self.window.create_oval(self.x, self.y, self.x + size, self.y + size, fill=self.color)
        self.activated = True

    def __init__(self, window):
        """ Just here to remove annoying messages mostly """
        self.window = window
        self.x, self.y = 0, 0
        self.color = 0
        self.team = 0
        self.sprite = 0
        self.activated = False

    def removeObject(self):
        self.window.coords(self.sprite, 0, 0, 0, 0)


# a = Canvas()
# a.tkwindow.mainloop()
