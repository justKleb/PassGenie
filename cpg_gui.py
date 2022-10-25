import gi
from time import time, perf_counter
import requests
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

ver = "0.4"
ver_response = requests.get("https://api.github.com/repos/v2ray/v2ray-core/releases/latest")
ver_response = ver_response.json()["name"]

count = 0
ct = time()


class Display(gtk.Window):
    def __init__(self):
        super().__init__()
        self.builder = gtk.Builder()
        self.builder.add_from_file("ui/main.glade")
        self.builder.connect_signals(self)

        win = self.builder.get_object("win")
        win.set_title("PassGin")
        win.connect("delete-event", gtk.main_quit)
        win.show()

        ver_label = self.builder.get_object("ver")
        if ver_response == ver:
            ver_label.set_label("Version: %s" % ver)
        else:
            ver_label.set_label("Current version: %s, Update %s available" % (ver, ver_response))


if __name__ == '__main__':
    m = Display()
    #m.set_title("PassGin")
    gtk.main()
