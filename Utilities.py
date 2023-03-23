import numpy as np
import cv2
import matplotlib.pyplot as plt

bf = cv2.BFMatcher()
def sift_matches(imgA,imgB):
    sift = cv2.SIFT_create()
    kps1,desc1= sift.detectAndCompute(imgA,None)
    kps2,desc2= sift.detectAndCompute(imgB,None)
    matches = bf.match(desc1,desc2)
    matches = sorted(matches,key= lambda x:x.distance)
    print(matches[0])
    return matches,kps1,desc1,kps2,desc2
def get_inliers_ratio(desc1,desc2,ratio):
    matches=bf.knnMatch(desc1,desc2,2)
    inliers=[]
    for m in matches:
        if((m[0].distance/m[1].distance)<ratio):
            inliers.append(m[0])
    return inliers

def get_inliers_crossCheck(desc1,desc2):
    match1= bf.match(desc1,desc2)
    match2=bf.match(desc2,desc1)
    inliers=[]
    for matc1 in match1:
        for matc2 in match2:
            if matc2.queryIdx == matc1.trainIdx and matc1.queryIdx==matc2.trainIdx:
                inliers.append(matc1)
    return inliers
def Draw_matches(imgA,imgB,kpsA,kpsB,matches,similarity,bool):
    img3 = cv2.drawMatches(imgA, kpsA,
                           imgB, kpsB,
                           matches,
                           flags=2,
                            outImg=None)
    plt.imshow(img3),plt.text(-25, -10, (bool , similarity), fontsize=15), plt.show()

def getSimilarity(inliers, kpsA,kpsB):
    similarity = len(inliers)/ min(len(kpsA),len(kpsB))
    return similarity
def if_similar(similarity,threshold):
    if similarity<threshold:
        return "the Two Images are not Similar"
    else:
        return "the Two Images are Similar"

#Bonus
def find_homography(inliers, kpsA, kpsB, reprojThresh):
    s = np.float32([kpsA[i.queryIdx].pt for i in inliers]).reshape(-1, 1, 2)
    d = np.float32([kpsB[i.trainIdx].pt for i in inliers]).reshape(-1, 1, 2)
    (H, status) = cv2.findHomography(s, d, cv2.RANSAC, reprojThresh)
    return (H, status)

def Draw_matches_RANSAC(imgA,imgB,kpsA,kpsB,matches,status,similarity,bool):
    status = status.ravel().tolist()
    img4 = cv2.drawMatches(imgA, kpsA, imgB, kpsB, matches, None,
                           matchColor=(0, 255, 0),  # draw matches in green color
                           matchesMask=status,  # draw only inliers
                           flags=2)
    plt.imshow(img4),plt.text(-25, -10, (bool , similarity), fontsize=15), plt.show()


