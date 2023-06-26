from PIL import Image
from GlobalDefintions import *
from Logger import Log
import math
import cv2
import PIL.ImageTk


# -------------------------------------------------------------------------------------------------
# ImageWrapper BEG
# Encapsulates image file handling
# -------------------------------------------------------------------------------------------------
class ImageWrapper(object):
    __image = None
    __pil_image = None
    __image_name = None

    def __init__(self, file_name):

        Log.debug('CTR>ImageFile file name =  ' + file_name)
        self.__image_name = file_name
        self.open_image(file_name)

    def get_image(self):
        return self.__image

    def get_pil_image(self):
        return self.__pil_image

    def open_image(self, file_path=None):
        try:
            Log.debug('Attempt to read ' + file_path)
            file_path = IMAGES_PATH + file_path
            self.__image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
            self.__pil_image = Image.open(file_path)

            if self.__image is None:
                Log.error('Image file = ' + file_path + ' did not load OK')
                raise ValueError("Unable to open image", file_path)
            else:
                Log.debug('Image file = ' + file_path + ' loaded OK')
                self.print_image_properties()


        except Exception as e:
            Log.exception(str(e))

    def close_image(self):
        try:
            if self.__image is not None:
                self.__image.close()
                Log.debug('Image file closed OK')

        except Exception as e:
            Log.exception(str(e))

    def save_image(self, file_name):
        try:
            self.__image.save(file_name, 'JPEG')
            Log.debug('Image file saved OK')

        except Exception as e:
            Log.exception(str(e))

    def display_image(self):
        try:
            if self.__image is not None:
                Log.debug('Image displayed')

                cv2.startWindowThread()
                cv2.namedWindow(self.__image_name)
                cv2.imshow(self.__image_name, self.__image)
                cv2.waitKey()
                cv2.destroyAllWindows()
        except Exception as e:
            Log.exception(str(e))

    def print_image_properties(self):
        try:
            if self.__image is None:
                Log.error('Image is NoneType')
            else:
                dimensions = self.get_image_dims()
                height = dimensions[0]
                width = dimensions[1]
                channels = dimensions[2]
                colors = self.get_colors()

                print('Image Metadata')
                print('\tFile Name\t= ', self.__image_name)
                print('\tImage Dimension\t= ', dimensions)
                print('\tImage Height\t= ', height)
                print('\tImage Width\t = ', width)
                print('\tDifferent Colors\t= ', colors)
                print('\tNumber of Channels\t= ', channels)

        except Exception as e:
            Log.exception(str(e))


    def get_image_dims(self):
            return self.__image.shape

    def get_size(self):
        height, width, no_channels = self.get_image_dims()
        return (height, width)

    def get_histogram(self):
        return self.__image.histogram()

    def get_colors(self):
        im = self.__pil_image.convert('P', palette=Image.ADAPTIVE).convert("RGB")
        colors = im.getcolors()
        return colors

    def convert_to_PIL(self):
        return Image.fromarray(self.__image)

    def convert_to_ImageTk(self):
        pil = self.convert_to_PIL()
        return PIL.ImageTk.PhotoImage(pil)

    # Get the pixel colors from the given image
    def get_pixel(self, i, j):
        # Inside image bounds?
        width, height = self.__pil_image.size
        if i >= width or j >= height:
            return (0, 0, 0)

        # Get Pixel
        try:
            pixel = self.__pil_image.getpixel((i, j))
            return pixel
        except Exception as e:
            Log.exception(str(e))
            return (0, 0, 0)

    # tests whether coordinate is inside a hypothetical circle
    def inside_circle(self, x, y, x_cen, y_cen, radius):
        square_dist = (x_cen - x) ** 2 + (y_cen - y) ** 2
        return square_dist <= radius ** 2

    # calculates the average color
    # inside the circle area inside the given coordinate bounds
    # seperate for r g b
    def calc_average_color_mask_circle(self, xy):
        # Returns a 3-tuple containing the RGB value of the average color of the
        # given square bounded by xy
        x1, y1, x2, y2 = xy
        x1 = int(round(x1))
        x2 = int(round(x2))
        y1 = int(round(y1))
        y2 = int(round(y2))

        dx = x2 - x1
        dy = x2 - x1
        x_cen = x1 + dx/2
        y_cen = y1 + dy/2
        diag = abs(dx)*math.sqrt(2)
        radius = diag/2

        try:
            r, g, b = 0, 0, 0
            out_r, out_g, out_b = 0, 0, 0
            count = 0
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if self.inside_circle(i, j, x_cen, y_cen, radius) is True:
                        pixlr, pixlg, pixlb = self.get_pixel(i, j)
                        r += pixlr
                        g += pixlg
                        b += pixlb
                        count += 1
                    else:
                        Log.debug('outside circle')


            if count is not 0:
                out_r = r / count
                out_g = g / count
                out_b = b / count

        except Exception as e:
            Log.exception(str(e))

        finally:
            return (out_r, out_g, out_b)



# -------------------------------------------------------------------------------------------------
# ImageWrapper END
# -------------------------------------------------------------------------------------------------

