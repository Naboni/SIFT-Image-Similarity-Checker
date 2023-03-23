import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from Utilities import *
images = os.listdir('images')
path= 'images/'
for im1 in images :
    img_path1=os.path.join(path,im1)
    image1=cv2.imread(img_path1,0)
    for im2 in images:
        if(im1==im2):
            continue;
        elif(im1[5]==im2[5]):
            img_path2 = os.path.join(path, im2)
            image2 = cv2.imread(img_path2, 0)
            #sift and get matches
            allMatches,kps1,desc1,kps2,desc2=sift_matches(image1,image2)

            # first way for filtering



            ratio_match=get_inliers_ratio(desc1,desc2,ratio=0.7)

            #second way for filtering

            crossCheck_match= get_inliers_crossCheck(desc1,desc2)
            match=[]
            for match1 in ratio_match:
                for match2 in crossCheck_match:
                    if match1.queryIdx == match2.queryIdx and match1.trainIdx==match2.trainIdx:
                        match.append(match1)
            #calculate similaritiy
            similarity=getSimilarity(match,kps1,kps2)
            bool =if_similar(similarity,0.01)

            # Draw matches after compressing matches
            Draw_matches(image1, image2, kps1, kps2, match,similarity,bool)

            #in Case Work with homography(Bonus)
            # (H, status)= find_homography(match,kps1,kps2,reprojThresh=4.0)
            # Draw_matches_RANSAC(image1,image2,kps1,kps2,match,status,similarity,bool)


