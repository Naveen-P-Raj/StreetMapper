# Project Description

## Problem

Road damage such as potholes can be difficult to monitor continuously using manual inspection.

## Objective

Develop a computer-vision MVP that detects potholes from road video and prepares structured location-tagged records that can support future road-condition mapping.

## Approach

1. Prepare a YOLO-format pothole dataset.
2. Train YOLO11s for 80 epochs.
3. Run the trained detector on road video.
4. Filter detections using a confidence threshold.
5. Associate detections with coordinates.
6. Save detections to CSV.
7. Explore TFLite export for edge/mobile deployment.

## Outcome

The supplied training run achieved 80.6% mAP@50 and 54.4% mAP@50–95 on the reported validation set, with 80.3% precision and 72.0% recall.
