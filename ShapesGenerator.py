from Logger import *
from GlobalDefintions import *
import abc
import random

# -------------------------------------------------------------------------------------------------
# AbstractShape BEG
# -------------------------------------------------------------------------------------------------
class AbstractShape(abc.ABC):

    @abc.abstractmethod
    def get_xy(self):
        pass

    @abc.abstractmethod
    def get_color(self):
        pass

# -------------------------------------------------------------------------------------------------
# AbstractShape END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# Cirlce BEG
# -------------------------------------------------------------------------------------------------
class Cirlce(AbstractShape):
    def __init__(self, xy = (0, 0, 0, 0), color="white"):
        Log.debug('CTR>Cirlce')
        self.xy = xy
        self.color = color

    def get_xy(self):
        return self.xy

    def get_color(self):
        return self.fill
# -------------------------------------------------------------------------------------------------
# Cirlce END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# AbstractShapeFactory BEG
# -------------------------------------------------------------------------------------------------
class AbstractShapeFactory(abc.ABC):

    __randomizer = None
    def __init__(self, randomizer=None):
        Log.debug('CTR>AbstractShapeFactory')
        self.__randomizer=randomizer

    @abc.abstractmethod
    def create_shape(self):
        pass

    def get_random_cordinates(self):
        if self.__randomizer is not None:
            return self.__randomizer.get_random_cordinates()

    def get_random_color(self):
        if self.__randomizer is not None:
            return self.__randomizer.get_random_color()

# -------------------------------------------------------------------------------------------------
# AbstractShapeFactory END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# CircleFactory BEG
# -------------------------------------------------------------------------------------------------
class CircleFactory(AbstractShapeFactory):

    def __init__(self, randomizer=None):
        Log.debug('CTR>CircleFactory')
        super().__init__(randomizer)

    def create_shape(self):
        return self.create_random_circle()

    def create_circle(self, xy, color):
        Log.debug('create_circle')
        circle = Cirlce(xy, color)
        return circle

    def create_random_circle(self):
        Log.debug('create_random_circle')
        return self.create_circle(self.get_random_cordinates(), self.get_random_color())
# -------------------------------------------------------------------------------------------------
# CircleFactory END
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# Randomizer BEG
# -------------------------------------------------------------------------------------------------
class Randomizer(object):

    #if radius = 0, it will be ignored
    def __init__(self, max_h=1000, max_w=1000, radius_prcnt_w=0, color_set=None, r=255, g=255, b=255, a=255):
        Log.debug('CTR>Randomizer')

        self.max_height = max_h
        self.max_width = max_w

        self.max_r = r
        self.max_g = g
        self.max_b = b
        self.max_a = a

        self.color_set = color_set

        self.max_radius = (radius_prcnt_w/100)*max_w


    def get_random_radius(self):
        Log.debug('get_random_radius')
        return random.uniform(1, self.max_radius)

    def get_random_cordinates(self):
        Log.debug('get_random_cordinates')

        try:
            if self.max_radius > 0:
                rnd_radius = self.get_random_radius()
                rnd_x = random.uniform(1, self.max_width)
                rnd_y = random.uniform(1, self.max_height)

                rnd_x1 = rnd_x - rnd_radius
                rnd_y1 = rnd_y - rnd_radius
                rnd_x2 = rnd_x + rnd_radius
                rnd_y2 = rnd_y + rnd_radius

            else:
                rnd_x1 = random.uniform(1, self.max_width)
                rnd_x2 = random.uniform(1, self.max_width)
                rnd_y1 = random.uniform(1, self.max_height)
                rnd_y2 = random.uniform(1, self.max_height)

            xy = [rnd_x1, rnd_y1, rnd_x2, rnd_y2]

        except Exception as e:
            Log.exception(str(e))

        finally:
            return xy

    def get_random_color(self):
        Log.debug('get_random_color')

        if(self.color_set is not None):
            indx = random.randint(0, len(self.color_set) - 1)
            rnd_r = self.color_set[indx][1][0]
            rnd_g = self.color_set[indx][1][1]
            rnd_b = self.color_set[indx][1][2]
            rnd_a = random.randint(0, self.max_a)

        else:
            rnd_r = random.randint(0, self.max_r)
            rnd_g = random.randint(0, self.max_g)
            rnd_b = random.randint(0, self.max_b)
            rnd_a = random.randint(0, self.max_a)
        return (rnd_r, rnd_g, rnd_b, rnd_a)


# -------------------------------------------------------------------------------------------------
# Randomizer END
# -------------------------------------------------------------------------------------------------