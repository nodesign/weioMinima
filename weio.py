from weioLib import weioControl
from weioLib import weioUserApi
import main

weioUserApi.attach.process(main.main)
w = weioControl.WeioControl()
w.start()
