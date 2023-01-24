from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

"""
" Main class of game.
"""
class Game():
  """
  " @var {str} name
  """

  name: str = "Tic Tac Toe"

  """
  " @var {QApplication} instance
  """

  instance: QApplication

  """
  " @var {QMainWindow} window
  """
  window: QMainWindow
  
  """
  " @var {str} result
  """
  result: str = "draw"

  """
  " @var {any} splashscreen
  """
  splashscreen: any

  """
  " Constructor of class.
  """
  def __init__(self):
    super().__init__()
    self.__CreateApplication()
    self.__CreateWindow()

  """
  " Public method to start game and show window.
  " @public
  """
  def StartGame(self, splashscreen):
    self.splashscreen = splashscreen
    self.splashscreen.ShowScene()

    self.window.show()
    self.instance.exec()

  """
  " Public method to reset game.
  " @public
  """
  def ResetGame(self):
    self.splashscreen.ShowScene()

  """
  " Public method to get window instance.
  " @public
  " @return {QMainWindow}
  """
  def GetWindow(self) -> QMainWindow:
    return self.window
  
  """
  " Public method to get results.
  " @public
  " @return {str}
  """
  def GetResult(self) -> str:
    return self.result

  """
  " Public method to set results.
  " @public
  " @param {str} result
  """
  def SetResult(self, result: str):
    self.result = result

  """
  " Private method to create main application instance.
  " @private
  """
  def __CreateApplication(self):
    self.instance = QApplication(sys.argv)

  """
  " Private method to create main window instance.
  " @private
  """
  def __CreateWindow(self):
    self.window = QMainWindow()
    self.window.setWindowTitle(self.name)
    self.window.resize(212, 212)

game = Game()