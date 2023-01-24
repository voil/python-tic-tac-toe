from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QVBoxLayout, QStackedLayout
from PyQt6.QtCore  import Qt
from PyQt6 import QtGui, QtCore

from src.game import game
from src.modules.results import results

"""
" TableElement class
"""
class TableElement():
  """
  " @var {bool} taken
  """
  taken: bool = False

  """
  " @var {str} type
  """
  type: str = ""

  """
  " @var {QWidget} container
  """
  container: QWidget

  def __init__(self, container: QWidget):
    super().__init__()
    self.container = container

  def GetContainer(self) -> QWidget:
    return self.container



"""
" Gameplay class scene
"""
class Gameplay():
  """
  " @var {str} turn
  """
  turn: str = "x"

  """
  " @var {str[9]} tableElements
  """
  tableElements = [
    "top-left", "top", "top-right",
    "middle-left", "middle", "middle-right",
    "bottom-left", "bottom", "bottom-right",
  ]

  table: object = {}

  """
  " Constructor of class.
  """
  def __init__(self):
    super().__init__()

  """
  " Public method to show scene.
  " @public
  """
  def ShowScene(self):
    game.GetWindow().setCentralWidget(self.__CreateScene())

  """
  " Private method to create table board.
  " @private
  """
  def __CreateTableBoard(self):
    for element in self.tableElements:
      self.__CreateButtonElement(element)

  """
  " Private method to create button table element.
  " @private
  " @param {str} element
  """
  def __CreateButtonElement(self, element: str):
      widget = QWidget()
      layout = QStackedLayout()
      button = QPushButton()

      button.clicked.connect(lambda: self.__handleClickElementBoard(element, button))

      layout.addWidget(button)
      widget.setLayout(layout)

      self.table[element] = TableElement(widget)

  """
  " Private method to handle click element board.
  " @private
  " @param {str} element
  " @param {QPushButton} button
  """
  def __handleClickElementBoard(self, element: str, button: QPushButton):
    self.table[element].taken = True
    self.table[element].type = self.turn

    button.setIcon(QtGui.QIcon("./assets/{}.png".format(self.turn)))
    button.setIconSize(QtCore.QSize(48,48))

    button.setDisabled(True)

    self.__ChangeTurn()
    self.__CheckIsEndGame()

  """
  " Private method to change turn player.
  " @private
  """
  def __ChangeTurn(self):
    self.turn = "x" if self.turn == "o" else "o"

  """
  " Private method to check is end game.
  " @private
  """
  def __CheckIsEndGame(self):
    countTakenElements: int = 0
    for element in self.tableElements:
      self.__CheckIsPlayerWinner(element, "x")
      self.__CheckIsPlayerWinner(element, "o")
      countTakenElements = self.__CheckIsDraw(countTakenElements, element)

  """
  " Private method for check is plarye winnier.
  " @param {string} element
  " @param {string} typePlayer
  " @private
  """
  def __CheckIsPlayerWinner(self, element: str, typePlayer: str):
    arrayOfSolutions = {
      "top-left": [
        ["top-left", "top", "top-right"],
        ["top-left", "middle-left", "bottom-left"],
        ["top-left", "middle", "bottom-right"]
      ],
      "top": [
        ["top", "middle", "bottom"]
      ],
      "top-right": [
        ["top-right", "middle-right", "bottom-right"]
      ],
      "middle-left": [
        ["middle-left", "middle", "middle-right"]
      ],
      "bottom-left": [
        ["bottom-left", "bottom", "bottom-right"],
        ["bottom-left", "middle", "top-right"]
      ],
    }

    if list(arrayOfSolutions).__contains__(element) == False: 
      return
    
    for value in arrayOfSolutions[element]:
      if self.table[value[0]].type == typePlayer and self.table[value[1]].type == typePlayer and self.table[value[2]].type == typePlayer:
        game.SetResult(typePlayer.upper())
        results.ShowScene()

  """
  " Private method to check is 
  " @private
  " @return {QWidget}
  """
  def __CheckIsDraw(self, result: int, element: str) -> int:
    if self.table[element].taken == True:
      result += 1
      if result == 9:
        game.SetResult("draw")
        results.ShowScene()
        return result
      
    return result

  """
  " Private method to create scene.
  " @private
  " @return {QWidget}
  """
  def __CreateScene(self) -> QWidget:
    self.__CreateTableBoard()

    widget = QWidget()
    layout = QVBoxLayout()
    
    indexY: int = 0
    indexX: int = 0
    
    layout = QGridLayout()
    for element in self.tableElements:
      element: TableElement = self.table[element]
      layout.addWidget(element.GetContainer(), indexX, indexY)

      if indexY == 2:
        indexY = 0
        indexX += 1
      else:
        indexY += 1

    widget.setLayout(layout)
    return widget


gameplay = Gameplay()