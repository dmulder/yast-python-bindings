# encoding: utf-8

from yast import *
class RadioButton1Client:
    def main(self):
      UI.OpenDialog(
        RadioButtonGroup(
          Id("rb"),
          VBox(
            Label("How do you want to crash?"),
            Left(RadioButton(Id('0'), "No&w")),
            Left(RadioButton(Id('1'), "&Every now and then")),
            Left(RadioButton(Id('2'), "Every &five minutes", True)),
            Left(RadioButton(Id('3'), Opt("boldFont"), "Ne&ver", True)),
            HBox(PushButton(Id("next"), "&Next"), PushButton("&OK"))
          )
        )
      )

      while True:
        ret = UI.UserInput()
        if ret == "next":
          current = int(UI.QueryWidget(Id("rb"), "CurrentButton"))
          current = ((current + 1) % 4)
          #UI.ChangeWidget(Id("rb"), "CurrentButton", Id(str(current)))
          # The variant above also doesn't work
          UI.ChangeWidget(Id("rb"), "CurrentButton", str(current))
        else:
          break

      UI.CloseDialog()


RadioButton1Client().main()
