# Image Similarity using SIFT
This project aims to compare images and determine their similarity using Scale-Invariant Feature Transform (SIFT) algorithm. 

This project includes two files:
main.py : The main script that performs the comparison between images.
Utilities.py : Contains all the utility functions used in the main script.

## Requirements
- Python 3.x
- OpenCV
- Numpy
- Matplotlib

## Usage
Place all the images that need to be compared in the 'images' folder.
Run the main script main.py.
The script will compare each pair of images in the folder and display the result.

## Functions in Utilities.py
- sift_matches(imgA,imgB) : Performs SIFT on the two images and returns their keypoints, descriptors, and matches.
- get_inliers_ratio(desc1,desc2,ratio) : Filters the matches using the ratio test.
- get_inliers_crossCheck(desc1,desc2) : Filters the matches using the cross-checking method.
- Draw_matches(imgA,imgB,kpsA,kpsB,matches,similarity,bool) : Draws the matches between the two images and displays their similarity.
- getSimilarity(inliers, kpsA,kpsB) : Calculates the similarity between the two images.
- if_similar(similarity,threshold) : Determines whether the two images are similar or not based on the calculated similarity.
- find_homography(inliers, kpsA, kpsB, reprojThresh) : Finds the homography matrix between the two images using the inliers.
- Draw_matches_RANSAC(imgA,imgB,kpsA,kpsB,matches,status,similarity,bool) : Draws the matches between the two images using the RANSAC algorithm and displays their similarity.

## Note
The main.py script will compare each pair of images in the folder. Hence, it may take some time to complete depending on the number of images in the folder.
The Draw_matches_RANSAC function in Utilities.py is a bonus function and is not used in the main script. It is included in case you want to experiment with the homography matrix.

## Example Output

