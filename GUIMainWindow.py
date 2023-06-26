from Logger import *
from GlobalDefintions import *
import abc
import threading
from tkinter import *
from tkinter.filedialog import askopenfilename


# -------------------------------------------------------------------------------------------------
# Display BEG
# Encapsulates display
# -------------------------------------------------------------------------------------------------
class AbstractView(abc.ABC):

    @abc.abstractmethod
    def get_window(self):
        pass

    @abc.abstractmethod
    def init_window(self, dims, title):
        pass

    @abc.abstractmethod
    def update(self):
        pass
# -------------------------------------------------------------------------------------------------
# Display END
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
# GUIWindow BEG
# GUI thread for the window to run async
# -------------------------------------------------------------------------------------------------
class GUIThread(threading.Thread):
    __display = None

    def __init__(self, display):
        try:
            Log.debug('CTR>MainGUI')
            self.__display = display
            threading.Thread.__init__(self)
            self.start()

        except Exception as e:
            Log.exception(str(e))

    def run(self):
        Log.debug('run')
# -------------------------------------------------------------------------------------------------
# GUIWindow END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# MainGUIController BEG
# Encapsulates GUI thread to show display
# -------------------------------------------------------------------------------------------------
class MainGUIController(object):
    __view = None
    __model = None
    __gui_thread = None
    def __init__(self, image, draw):
        Log.debug('CTR>MainGUIController')

        self.__view = MainGUIView(MAIN_WIN_TITLE, image, draw)
        self.__model = MainGUIModel(image, draw)
        self.__gui_thread = GUIThread(self)

    def get_model(self):
        return self.__model

    def is_alive(self):
        return self.__view.get_is_alive()

    def refresh(self):
        Log.debug('refresh')
        Log.debug(Progress.get_all_stats())
        self.__view.update(self.get_model().get_draw())

    def loop(self):
        self.__view.loop()

# -------------------------------------------------------------------------------------------------
# MainGUIController END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# MainGUIModel BEG
# Encapsulates GUI thread to show display
# -------------------------------------------------------------------------------------------------
class MainGUIModel(object):
    __image = None
    __draw = None
    def __init__(self, image, draw):
        Log.debug('CTR>MainGUIModel')

        self.__image = image
        self.__draw = draw

    def get_draw(self):
        return self.__draw

# -------------------------------------------------------------------------------------------------
# MainGUIModel END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# MainGUIView BEG
# GUI view
# -------------------------------------------------------------------------------------------------
class MainGUIView(AbstractView):
    draw_panel = None
    __is_alive = False

    def __init__(self, window_title='', image=None, draw=None):
        Log.debug('CTR>MainGUIView')
        try:
            self.init_window(window_title)
            self.add_image(image)
            self.add_draw(draw)

        except Exception as e:
            Log.exception(str(e))

    def get_window(self):
        return self.window

    def init_window(self, title):
        Log.debug('init_window')
        try:
            # Create root window
            self.window = Tk()
            self.window.title(title)

            # Create PanedWindow
            self.pnd_window = PanedWindow(self.window, orient=HORIZONTAL)
            self.pnd_window.pack(fill=BOTH, expand=1)

            # Create image panel
            self.image_panel = Label(self.pnd_window, text="Real Image")
            self.image_panel.pack(side="left", padx=10, pady=10)
            self.pnd_window.add(self.image_panel)

            # Create draw panel
            self.draw_panel = Label(self.pnd_window, text="Synthetic Image")
            self.draw_panel.pack(side="right", padx=10, pady=10)
            self.pnd_window.add(self.draw_panel)

            # Create buttons
            self.quit_button = Button(self.window, text='Quit', command=self.on_close)
            self.quit_button.pack()

            # Create text statistics
            self.stats_str = StringVar()
            self.stats_lbl = Label(self.window, textvariable=self.stats_str)
            self.stats_lbl.place(relx=0.0, rely=1.0, anchor='sw')
            self.stats_lbl.pack()

            # Closing stuff
            self.window.protocol("WM_DELETE_WINDOW", self.on_close)
            self.__is_alive = True



        except Exception as e:
            Log.exception(str(e))

    # Add image to image pane
    def add_image(self, image):
        Log.debug('add_image')
        try:
            tk_im = image.convert_to_ImageTk()
            self.image_panel.image = tk_im
            self.image_panel.configure(image=tk_im)

        except Exception as e:
            Log.exception(str(e))

    # Add draw to draw pane
    def add_draw(self, draw):
        Log.debug('add_draw')
        try:
            tk_draw = draw.convert_to_ImageTkd()
            self.draw_panel.image = tk_draw
            height, width, no_channels = draw.get_dims()
            self.draw_panel.configure(image=tk_draw)


        except Exception as e:
            Log.exception(str(e))

    def get_is_alive(self):
        return self.__is_alive

    def on_close(self):
        Log.debug('on_close')
        try:
            self.__is_alive = False
            self.window.destroy()
        except Exception as e:
            Log.exception(str(e))


    def update_stats(self):
        Log.debug('update_stats')
        stats = Progress.get_stats_4GUI()
        self.stats_str.set(stats)

    def update(self, draw):
        Log.debug('update')
        self.add_draw(draw)
        self.update_stats()
        self.window.update()

    def loop(self):
        Log.debug('loop')
        self.window.mainloop()


def open_file_chose():
    root = Tk()
    path_name = askopenfilename(initialdir=ROOT_DIR, title=CHOOSE_DIALOG_MSG)
    return path_name
# -------------------------------------------------------------------------------------------------
# MainGUIView END
# -------------------------------------------------------------------------------------------------