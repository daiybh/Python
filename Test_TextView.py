import gobject
import gtk
import pango

class HtmlTextView(gtk.TextView):
    __gtype_name__="HtmlTextView"
    __gsignals__ = {
        'url-clicked': (gobject.SIGNAL_RUN_LAST, None, (str, str)), # href, type
    }
    def __init__(self,buff=None):
         gtk.TextView.__init__(self,buff)
         self.textbuf = self.get_buffer()
         #color = colormap.alloc_color(0, 0, 0xffff)
         tag = self.textbuf.create_tag("big",
                                       weight=pango.WEIGHT_BOLD)
         tag = self.textbuf.create_tag("italic",
                                       style=pango.STYLE_ITALIC)
         tag = self.textbuf.create_tag("arisal",
                                       family="微软雅黑")
         tag = self.textbuf.create_tag("Red",
                                       foreground="red")
         #tag = self.textbuf.create_tag("h_9f",
          #                      background_gdk=color,
          #                      size_points=10.0)
         #tag.set_property("family","Arial")
         #tag.set_property("weight",pango.WEIGHT_BOLD)
         eob = self.textbuf.get_end_iter()
         #self.textbuf.insert_with_tags_by_name(eob,"hello","family","weight")
         #self.textbuf.insert_with_tags(eob,"hello",tag)
         self.textbuf.insert_with_tags_by_name(eob,"kf看",
                                               "big","italic")
         self.textbuf.insert_with_tags_by_name(eob,'wo的中国',
                                               "arisal","Red","big")

    def display_html(self,htmlu):
        return
        buffer = self.get_buffer()
        eob = buffer.get_end_iter()
        buffer.insert(eob,htmlu)
        if not eob.starts_line():
            buffer.insert(eob,"\n")


def main():
	sw = gtk.ScrolledWindow()
	sw.show()
	htmlview = HtmlTextView()
	htmlview.display_html("<span>")
	htmlview.display_html('<span><span style="font-size: 10pt;">    [10:22:49] <span style="color: #000000;">&#173;&#36824;&#26159;&#23601;&#26159;</span><br/></span></span>')
	htmlview.show()
	sw.add(htmlview)

	label = gtk.Label("myLabel")
	label.modify_font(pango.FontDescription("sans 48"))

	frame = gtk.Frame()
	frame.set_shadow_type(gtk.SHADOW_IN)
	#frame.add(htmlview)
	frame.add(sw)
	frame.show()
	#frame.add( sw )
	w = gtk.Window()
	w.add(frame)

	w.set_default_size(400, 300)
	w.show_all()
	w.connect("destroy", lambda w: gtk.main_quit())
	gtk.main()

if __name__ =='__main__':
	main()