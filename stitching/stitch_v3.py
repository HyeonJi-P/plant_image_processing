from panorama import Stitcher
#import argparse
import imutils
import cv2
# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument(“-f”, “ — first”, required=True, help=”path to the first image”)
#ap.add_argument(“-s”, “ — second”, required=True, help=”path to the second image”)
#args = vars(ap.parse_args())
# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageB = cv2.imread('./stitch_2/230208_082324_L1_V2_P07_D0250.png')
imageA = cv2.imread('./stitch_2/230208_082354_L1_V2_P08_D0290.png')
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)
# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
# show the images
#cv2.imshow(“Image A”, imageA)
#cv2.imshow(“Image B”, imageB)
cv2.imwrite('./Keypoint_Matches.png', vis)
cv2.imwrite('./Result_v3.png', result)
