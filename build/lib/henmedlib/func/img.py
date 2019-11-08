__author__ = "Henning Schmitz"

import cv2
import numpy as np

def image_difference(image1, image2):
    """
    Given two images of the same size, the function calculates the difference between them and in case of a difference
    returns an image showing that difference.

    :param image1: path of the first image (string)
    :param image2: path of the second image (string)
    :return: String indicating whether there is a difference or not. If there is a difference an additional image
    showing that difference.
    """

    a = cv2.imread(image1)
    b = cv2.imread(image2)
    difference = cv2.subtract(a, b)
    result = not np.any(difference)
    if result is True:
        print('Pictures are identical')
    else:
        cv2.imwrite('diff.jpg', difference)
        print('Pictures are not identical, the difference is stored as diff.jpg')