import gtk

def newWin():
    window = gtk.Window()
    window.set_title("title")
    window.set_default_size(150,100)
    window.set_position(gtk.WIN_POS_CENTER)
    window.set_type_hint(gtk.gdk.WINDOW_TYPE_HINT_DIALOG)
    window.set_resizable(False)
    window.set_border_width(8)

    args=[]
#    args.insert(0,stock.CLOSE)
    window.connect('delete-event',close_cb,window,None,*args)
    window.show()

def close_cb(widget, event, window, response_cb, *args):
    '''default close callback, call response_cb with args if it's not
    None'''
    print "close_cb"
    if response_cb:
        response_cb(*args)

    window.hide()

newWin()


