from Logger import *
from OptimizationScheme import *
from GlobalDefintions import *



# -------------------------------------------------------------------------------------------------
# NeighborColorsScheme BEG
# Implements an Optimization Scheme in the most basic way:
#  - Each cycle a random shape is generated
#  - The shape is compared to the reference image loaded by the user
#  - It is compared based on pixel colors in the shape coordinates and the ref image
#  - If the generation is good enough it is drawn
#  - 'Good enough' is defined by: for each color average difference (r,g,b) test whether it less then pre defined MAX_ALLOWED_ERROR_PERCENT
# -------------------------------------------------------------------------------------------------
class NeighborColorsScheme(OptimizationSchemeStrategy):

    def __init__(self, image, drawer):
        Log.debug('CTR>NeighborColorsScheme')

        self.drawer = drawer
        self.ref_image = image


    # entry point in the algorithm
    def find_solution(self):
        self.generate()


    def generate(self):
        Log.debug('generate')
        circle = self.drawer.get_random_circle()
        fit = self.fitness(circle.xy, circle.color)
        Progress.inc_im_generated()

        if fit is True:
            Log.debug('drawing')
            self.drawer.draw_circle(circle)
            Progress.inc_im_drawn()
        else:
            Log.debug('ignored')
            Progress.inc_im_ignored()


    # calculates if the current generated sh
    def fitness(self, xy, color):
        Log.debug('fitness')
        fit = self.test_for_thershold(self.pixel_error(xy, color), MAX_ALLOWED_ERROR_PERCENT)
        return fit


    def pixel_error(self, xy, gen_color):
        ref_r, ref_g, ref_b = self.ref_image.calc_average_color_mask_circle(xy)
        gen_r, gen_g, gen_b, gen_alpha = gen_color

        dist_r = abs(gen_r - ref_r)
        dist_g = abs(gen_g - ref_g)
        dist_b = abs(gen_b - ref_b)

        return dist_r, dist_g, dist_b

    def test_for_thershold(self, rgb, thr):
        r, g, b = rgb

        p_r = r / 255.0 * 100
        p_g = g / 255.0 * 100
        p_b = b / 255.0 * 100

        return (p_r <= thr) and (p_g <= thr) and (p_b <= thr)
# -------------------------------------------------------------------------------------------------
# NeighborColorsScheme END
# -------------------------------------------------------------------------------------------------





