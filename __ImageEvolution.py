from ImageHandler import *
from GUIMainWindow import *
from DrawHandler import *
from ShapesGenerator import *
from GlobalDefintions import *
from OptimizationScheme import *
from NeighborColorsScheme import *


# -------------------------------------------------------------------------------------------------
# Main BEG
# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    Log.debug('Program Start: ' + Progress.get_time_str())

    #reference image init
    # file = open_file_chose()
    ref_image = ImageWrapper(TO_OPEN_FILE_NAME)
    dims = ref_image.get_image_dims()
    height, width, no_channels = dims

    #circle factory init
    #limit radius up to % of width of the reference image
    randomizer = Randomizer(height, width, MAX_CIRCLE_RADIUS_PERCENT, ref_image.get_colors())
    circle_factory = CircleFactory(randomizer)

    #drawer init
    drawer = PILDrawerCircle(dims, circle_factory)

    #GUI init
    GUI = MainGUIController(ref_image, drawer)

    #optimization scheme init
    scheme = NeighborColorsScheme(ref_image, drawer)
    scheme_ctx = OptimizationSchemeContext(scheme)


    while GUI.is_alive():
        try:
            scheme_ctx.run()
            GUI.refresh()
        except Exception as e:
            Log.exception(str(e))


    Log.debug('Program End: ' + Progress.get_time_str())

# -------------------------------------------------------------------------------------------------
# Main END
# -------------------------------------------------------------------------------------------------

