from ShapesGenerator import *
from GlobalDefintions import *
import PIL.Image, PIL.ImageTk, PIL.ImageDraw
import abc


# -------------------------------------------------------------------------------------------------
# AbstractDrawer BEG
# -------------------------------------------------------------------------------------------------
class AbstractDrawer(abc.ABC):

    @abc.abstractmethod
    def get_draw(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
# -------------------------------------------------------------------------------------------------
# AbstractDrawer END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# PILDrawer BEG
# -------------------------------------------------------------------------------------------------
class PILDrawer(AbstractDrawer):
    __image = None
    __draw = None
    __dims = None

    def __init__(self, dims, shape_factory):
        try:
            Log.debug('CTR>PILDrawer')
            # Save dimensions
            self.__dims = dims
            height, width, no_channels = dims
            # Create a blank image
            self.__image = PIL.Image.new('RGBA', (width, height), "white")
            # Create a draw object
            self.__draw = PIL.ImageDraw.Draw(self.__image)

            self.shape_factory = shape_factory

        except Exception as e:
            Log.exception(str(e))

    def get_image(self):
         return self.__image

    def get_draw(self):
         return self.__draw

    def set_draw(self, draw):
         Log.debug('set_draw')
         self.__draw = draw

    def set_image(self, image):
        Log.debug('set_draw')
        self.__image = image


    def draw(self):
        Log.debug('draw')
        Log.info('not implemented')
        pass

    def get_dims(self):
         return self.__dims

    def convert_to_ImageTkd(self):
        Log.debug('convert_to_ImageTkd')
        return PIL.ImageTk.PhotoImage(self.get_image())

# -------------------------------------------------------------------------------------------------
# PILDrawer END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# PILDrawerCircle BEG
# -------------------------------------------------------------------------------------------------
class PILDrawerCircle(PILDrawer):

    def __init__(self, dims, shape_factory):
        try:
            Log.debug('CTR>PILDrawerCircle')
            super().__init__(dims, shape_factory)

        except Exception as e:
            Log.exception(str(e))

    def draw(self):
        Log.debug('draw_circle')
        self.draw_circle(self.get_random_circle())

    def get_random_circle(self):
        Log.debug('get_circle')
        return self.shape_factory.create_shape()

    def draw_circle(self, circle):
        Log.debug('draw_circle')
        self.get_draw().ellipse(circle.xy, circle.color)
# -------------------------------------------------------------------------------------------------
# PILDrawerCircle BEG
# -------------------------------------------------------------------------------------------------