# General
- This is the code we used to participate track 5 (Detecting Violation of Helmet Rule for Motorcyclists) of [AI CITY CHALLANGE 2023](https://www.aicitychallenge.org/).
- We used a YOLOv8 for detector and strongsort for tracker. 
- For details about dataset, you should go to the link above.
# Requirement 
- For visualizing-web: ```pip install -r visualizing-web/requirements.txt```
- For yolov8, refer this repo: https://github.com/ultralytics/ultralytics
- For strongsort, refer this repo: https://github.com/kadirnar/strongsort-pip
# Visualizing data
- If you want to visualize video, move videos to 'visualizing-web/static/data/bbox-video'
- Then, run the following command:
```python visualizing-web/app.py```
# Training
- To train yolov8, refer this repo: https://github.com/ultralytics/ultralytics
- To train feature extractor of strongsort, refer this repo: https://github.com/kadirnar/strongsort-pip
# Inference
- cd to yolov8 folder: 
```cd yolov8```
- We provide the checkpoint file of YOLOv8 on this dataset: https://drive.google.com/file/d/1P-VjBKllb4KcqoNTYQsXhTYOMwmkmu9X/view?usp=sharing
- Change the path folder of videos and path to checkpoint file of YOLOv8 in inferece.py if necessary, then: 
```python inference.py```
- However, there will be some bounding boxes predicted which extend outside the image. We need to modify the output with the following command:
```python post-preprocessing.py```