"""
This module is used as utilities functions that relate to image detection
"""


def detect_objects(image_path):
    """
    Currently placeholder
    In the future it will activate ultralytics object detection
    and return a json of the detection
    :param image_path:
    :return: Json of detected objects
    """
    return [
        {"label": "person", "confidence": 0.98, "bbox": [100, 100, 200, 200]},
        {"label": "car", "confidence": 0.89, "bbox": [300, 150, 450, 300]},
    ]
