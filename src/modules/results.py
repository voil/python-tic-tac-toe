from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore  import Qt

from src.game import game

"""
" Result class scene
"""
class Results():
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
    button = QPushButton("Reset game")
    button.clicked.connect(game.ResetGame)

    return button
  
  """
  " Private method to create result text.
  " @private
  " @return {QLabel}
  """
  def __CreateTextResult(self) -> QLabel:
    label: QLabel

    match game.GetResult():
      case "X" | "O":
        label = QLabel("The winner is " + game.GetResult())
      case "draw":
        label = QLabel("There is a draw")

    label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
    return label

  """
  " Private method to create scene container.
  " @private
  " @return {QWidget}
  """
  def __CreateScene(self) -> QWidget:
    layout = QVBoxLayout()
    layout.addWidget(self.__CreateTextResult())
    layout.addWidget(self.__CreateStartButton())

    widget = QWidget()
    widget.setLayout(layout)

    return widget


results = Results()