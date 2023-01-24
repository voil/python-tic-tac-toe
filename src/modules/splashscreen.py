from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget

from src.game import game
from src.modules.gameplay import gameplay


"""
" Splashscreen class scene
"""
class Splashscreen():

  """
  " Constructor of class.
  """
  def __init__(self):
    super().__init__()

  """
  " Public method show scene.
  " @public
  """
  def ShowScene(self): 
    game.GetWindow().setCentralWidget(self.__CreateScene())

  """
  " Private method to create start button.
  " @private
  " @return {QPushButton}
  """
  def __CreateStartButton(self) -> QPushButton:
    button = QPushButton("Start new game")
    button.setGeometry(500, 500, 320, 210)

    button.clicked.connect(gameplay.ShowScene)

    return button

  """
  " Private method to create scene container.
  " @private
  " @return {QWidget}
  """
  def __CreateScene(self) -> QWidget:
    layout = QVBoxLayout()
    layout.addWidget(self.__CreateStartButton())

    widget = QWidget()
    widget.setLayout(layout)

    return widget

splashscreen = Splashscreen()