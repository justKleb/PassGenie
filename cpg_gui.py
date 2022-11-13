import gi; gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk
from gi.repository import Gdk as gdk
from utils.cpg_utils import passwordGen as pg
from utils.cpg_utils import to_log
import subprocess as sp
import re

xclip = False
try:
    op = sp.run(["xclip", '-h'], capture_output=True, text=True)
    xclip = True; import pyclip
except FileNotFoundError:
    to_log("xclip installation not found, falling back to GTK clipboard", 2)
    xclip = False

cmds = ['rn', 'rl', 'rs', 'm', 'rw']

count = 0

class Display(gtk.Window):

    def passgen(self, widjet):
        to_log("Password generation initiated via GUI")
        global count
        self.passdone.hide()
        self.pbar.set_fraction(0)
        toGen = self.usrinp.get_text()
        if len(toGen) != 0: partPerc = (100 / len(toGen)) / 100
        else: partPerc = 1
        cmd_regex = "%([a-zA-Z]{1,2}) *?([0-9]*?) ?%"

        def check(check, args, pos: tuple):
            pbarVal = self.pbar.get_fraction()
            self.pbar.set_fraction(pbarVal + partPerc)
            if check in cmds:
                if check == cmds[0]:
                    return pg.gen_random_nums(int(args))
                elif check == cmds[1]:
                    return pg.gen_random_letters(int(args))
                elif check == cmds[2]:
                    return pg.gen_random_syms(int(args))
                elif check == cmds[3]:
                    return pg.mirror(toGen[:pos[0]])
                elif check == cmds[4]:
                    return pg.gen_random_words(int(args))

        if toGen != '' or None:
            x = re.findall(cmd_regex, toGen)
            for j, k in x:
                z = re.search(cmd_regex, toGen); z1, z2 = z.span()
                to_write = check(j, k, (z1, z2))
                convs = list(toGen)
                convs[z1:z2] = [to_write]
                toGen = ''.join(str(i) for i in convs)
        else:
            toGen = pg.gen_random_words(2) + pg.gen_random_syms(10)

        self.pbar.set_fraction(1)
        to_log("Password generation complete")
        self.password.set_text(toGen)

        def copy(s):
            to_log("Copy to clipboard option was chosen")
            if xclip:
                pyclip.copy(toGen)
            else:
                self.clipboard.set_text(toGen, -1)
        def write(s):
            to_log("Write to file option was chosen [WIP]")
            pass

        def cancel(s):
            to_log("Clear option was chosen")
            global check
            check = None
            self.pbar.set_fraction(0)
            self.usrinp.set_text('')
            self.password.set_text('')
            self.passdone.hide()

        if count != 1:
            self.cancel.connect('clicked', cancel)
            self.copy.connect("clicked", copy)
            self.writeout.connect("clicked", write)
        self.passdone.show()

        count = 1




    def __init__(self):
        super().__init__()
        self.builder = gtk.Builder()
        self.builder.add_from_file("ui/main.glade")
        self.builder.connect_signals(self)
        self.clipboard = gtk.Clipboard.get(gdk.SELECTION_CLIPBOARD)

        win = self.builder.get_object("win")
        win.set_title("PassGenie")
        win.set_icon_from_file('./passgenieblur.svg')
        win.connect("delete-event", gtk.main_quit)
        self.pbar = self.builder.get_object("pbar")
        self.genpass = self.builder.get_object("genpass")
        self.writeout = self.builder.get_object("writeout")
        self.cancel = self.builder.get_object("cancel")
        self.copy = self.builder.get_object("copy")
        self.usrinp = self.builder.get_object("usrinp")
        self.passdone = self.builder.get_object("passdone")
        self.password = self.builder.get_object("password")

        self.genpass.connect("clicked", self.passgen)

        self.passdone.hide()
        win.show()


m = Display()
gtk.main()
