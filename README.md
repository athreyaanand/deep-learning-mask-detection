# Mask and You Shall Receive: A Survey of Deep Learning in Face Mask Detection

## Open Source Packages

* [pytorch](https://pytorch.org) - a famous framework for machine learning including numerous lines of code exist in the package

* [numpy](https://numpy.org/) - a famous numerical computing tool including numerous lines of code exist in the package

* [opencv](https://pypi.org/project/opencv-python/) - a famous computer vision tool including numerous lines of code exist in the package

* [pillow](https://python-pillow.org) - PIL is the Python Imaging Library used for general image processing through code

* [facenet-pytorch](https://github.com/timesler/facenet-pytorch) - an efficient pytorch implementation of MTCNN for face detection prior to inference

## Datasets

* [Kaggle Face Mask Detection Dataset](https://www.kaggle.com/andrewmvd/face-mask-detection)
  * images belonging to 3 classes: With_mask, mask_weared_incorrect, without_mask
  * Total Size: 853 images
* [MaskedFace-Net Dataset](https://github.com/cabani/MaskedFace-Net)
  * 60,000 images of correctly worn masks and over 60,000 images of incorrectly worn masks over chin or mouth. All images were computer generated.
  * Total Size: 134,093 images

To run the model from scratch please go to the links, download the files and put the images and annotations in the empty "images" and "annotations" folders.

## Structure of the Code

We implemented 3 models (Faster-RCNN, SSD, YOLO) as well as a real time webcam detection module to test out the models. Both Faster-RCNN and SSD can be found in the home directory in their respective jupyter notebooks. The code for YOLO is contained within the YOLO folder. Similarly, to run the webcam detector please navigate to the respective folder and simply run the `webcam.py` script.

For the jupyter notebooks, there is no real need to rerun the notebooks since outputs of our latest runs are saved as checkpoints. However, if desired, you can feel free to run it yourself! Just make sure you download the data beforehand like mentioned before.

Similarly, for more understanding, our slide decks and presentations can also be found within the project.

## Performance

We used Google Colab to run the notebooks for better performance due to its free GPU. For performance, we used Accuracy, Recall, Precision, and Average Prediction Time to measure each models' ability. A table of our results can be seen here:

|             | FASTER RCNN | SSD         | YOLO        |
|    :---     |    :----:   |    :----:   |    :----:   |
| ACCURACY    | 58.33%      | 56.2%       | 66.85%      |
| RECALL      | 60%         | 58.5%       | 68.74%      |
| PRECISION   | 85.71%      | 80.6%       | 49.9%       |
| PRED TIME   | 15.24ms     | 13.39ms     | 13.08ms     |

There is no hosting URLs of our project; thus, you can run it locally or check the results run by us in the notebooks of each model.
