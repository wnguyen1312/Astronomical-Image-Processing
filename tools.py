import numpy as np
import scipy.ndimage as snd

def mask_circle(mask, center, radius):
    '''
    Function to create a circular mask with a fixed radius at a center (x0, y0)
    '''
    x0, y0 = center
    yy, xx = np.ogrid[:mask.shape[0], :mask.shape[1]]
    circle_mask = (xx - x0)**2 + (yy - y0)**2 <= radius**2
    mask[circle_mask] = False
    return mask
