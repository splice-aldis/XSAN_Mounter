import os
import sys
from subprocess import call
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# xsan_volumes = {"LAMBERT","WILLIAMS", "PRATT"}
xsan_volumes = []

class XSANMounterApp(App):
    cache_file = open('cachefile', 'r')

    for line in cache_file:
        volume_name = line.split(" - ")[0]
        volume_mounted = line.split(" - ")[1].replace('\n', '')

        if volume_mounted == "not mounted":
            # print volume_name + " is " + volume_mounted
            xsan_volumes.append([volume_name, volume_mounted])
        else:
            # print volume_name + " is mounted"
            xsan_volumes.append([volume_name, "mounted"])
    cache_file.close()
    # this is the button maker to toggle whether volumes are mounted or not.

    def build(self):

        app_stage = BoxLayout(orientation="vertical")

        message_box = TextInput(text='You have three volumes to mount:', font_size=30)

        for vol in xsan_volumes:
            app_stage.add_widget(self.bm(vol))

        app_stage.add_widget(message_box)

        return app_stage

    def btn_mnt_state(self, vol):

        if vol[1] == "not mounted":
            return "normal"
        else:
            return "down"

    def btn_unmnt_state(self, vol):

        if vol[1] == "not mounted":
            return "down"
        else:
            return "normal"

    def mount_volume(self, test):

        f = open("cachefile", "w")
        try:
            call(["ls", "-l"])  # , stdout=f
            f.close()

        except (OSError, SyntaxError):
            print "this failed OS"
            f.close()
        cache_file = open('cachefile2', 'r')
        for line in cache_file:
            volume_name = line.split(" - ")[0]
            volume_mounted = line.split(" - ")[1].replace('\n', '')
            mount_button_name = 'mount_btn_' + volume_name
            unmount_button_name = 'unmount_btn_' + volume_name

            if volume_mounted == "not mounted":
                unmount_button_name.state = "down"
                mount_button_name.state = "normal"
            else:
                mount_button_name.state = "down"
                unmount_button_name.state = "normal"

    def bm(self, vol):

        xsan_layout = BoxLayout(orientation="horizontal")
        mount_button_name = 'mount_btn_' + vol[0]
        unmount_button_name = 'unmount_btn_' + vol[0]

        mount_button_name = ToggleButton(text='MOUNT', group=vol[0], state=self.btn_mnt_state(vol), allow_no_selection=False, font_size=30, id=self.btn_unmnt_state(vol))

        mount_button_name.bind(on_press=self.mount_volume)

        unmount_button_name = ToggleButton(text='UNMOUNT', group=vol[0], state=self.btn_unmnt_state(vol),allow_no_selection=False, font_size=30, id=self.btn_unmnt_state(vol))

        unmount_button_name.bind(on_press=self.mount_volume)

        volume_name = Label(text=vol[0], font_size=40, size_hint_x=2)

        xsan_layout.add_widget(volume_name)
        xsan_layout.add_widget(mount_button_name)
        xsan_layout.add_widget(unmount_button_name)
        return xsan_layout



if __name__ == "__main__":
    XSANMounterApp().run()