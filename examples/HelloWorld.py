# encoding: utf-8

from yast import *
class HelloWorldClient:
    def main(self):
      UI.OpenDialog(
        VBox(Label("Hello, World!"), PushButton(Opt("default"), "&OK"))
      )
      UI.UserInput()
      UI.CloseDialog()


HelloWorldClient().main()

