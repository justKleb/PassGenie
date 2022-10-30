import gi; gi.require_version("Gtk", "3.0")
import pyclip
from gi.repository import Gtk as gtk
from utils.cpg_utils import passwordGen as pg

cmds = ['%rn', '%rl', '%rs', '%m', '%mp']

count = 0

class Display(gtk.Window):

    def passgen(self, widjet):
        global count
        self.passdone.hide()
        self.pbar.set_fraction(0)
        toGen = self.usrinp.get_text()
        inp = toGen.split(' ')
        partPerc = (100 / len(inp)) / 100
        for i in range(len(inp)):
            pbarVal = self.pbar.get_fraction()
            self.pbar.set_fraction(pbarVal + partPerc)
            if inp[i]:
                if inp[i] == cmds[0]:
                    inp[i] = pg.genRandomNums(int(inp[i + 1]))
                    del inp[i + 1]
                elif inp[i] == cmds[1]:
                    inp[i] = pg.genRandomLetters(int(inp[i + 1]))
                    del inp[i + 1]
                elif inp[i] == cmds[2]:
                    inp[i] = pg.genRandomSyms(int(inp[i + 1]))
                    del inp[i + 1]
                elif inp[i] == cmds[3]:
                    inp[i] = pg.mirror(inp[i - 1])

        def copy(s):
            pyclip.copy(''.join(inp))

        def write(s):
            pass

        def cancel(s):
            global inp
            inp = None
            self.pbar.set_fraction(0)
            self.usrinp.set_text('')
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

        self.genpass.connect("clicked", self.passgen)

        self.passdone.hide()
        win.show()

        #ver_label = self.builder.get_object("ver")


if __name__ == '__main__':
    m = Display()
    #m.set_title("PassGin")
    gtk.main()
