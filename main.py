#!/usr/bin/env python2

import sys
sys.path.append('./kivymd')


from kivy.app import App
from kivy.lang import Builder

# from kivy.metrics import dp
# from kivy.properties import ObjectProperty
# from kivy.uix.image import Image

# from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
# from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
# from plyer.facades import Orientation
# from kivymd.time_picker import MDTimePicker
import subprocess
import tomWrap


class SimpleApp(App):
    theme_cls = ThemeManager()
    theme_cls.theme_style = 'Light'
    theme_cls.primary_palette = 'Indigo'

    def build(self, ):
        main_widget = Builder.load_file('./mdkvfile.kv')
        return main_widget

    def connect(self):
        pass

    def getTom(self, maxcycle, asmcode):
        # print(blah)
        try:
            return tomWrap.tomCall((maxcycle, asmcode))
        except:
            return 'Correct your code'

    def getTomMax(self, asmcode):
        # print(blah)
        try:
            return tomWrap.tomMax((asmcode))
        except:
            return -1


if __name__ == '__main__':
    SimpleApp().run()
