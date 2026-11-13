import gi

gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk


class App(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.mkamelll.calcboi")

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="calcboi")
        window.set_default_size(600, 400)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        grid = Gtk.Grid(
            row_spacing=4,
            column_spacing=4,
            row_homogeneous=True,
            column_homogeneous=True,
        )
        max_col = 3
        numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
        for i, n in enumerate(numbers):
            button = Gtk.Button(label=n)
            button.connect("clicked", self.on_number_btn_clicked)
            row = i // max_col
            col = i % max_col
            grid.attach(button, col, row, 1, 1)

        grid.attach(Gtk.Button(label="0"), (i + 1) % max_col, (i + 1) // max_col, 2, 1)
        grid.attach(Gtk.Button(label="."), (i + 3) % max_col, (i + 2) // max_col, 1, 1)

        self.text_view = Gtk.TextView()
        self.text_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        self.text_view.set_hexpand(True)
        self.text_view.set_vexpand(True)
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_child(self.text_view)

        vbox.append(scrolled)
        vbox.append(grid)

        window.set_child(vbox)
        window.present()

    def on_number_btn_clicked(self, btn: Gtk.Button):
        buffer = self.text_view.get_buffer()
        label_text = btn.get_label()
        buffer.insert_at_cursor(label_text or "", len(label_text or ""))


if __name__ == "__main__":
    import sys

    app = App()
    app.run(sys.argv)
