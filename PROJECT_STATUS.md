# Project Status

## Current status: MVP / portfolio-ready

The supplied Google Colab notebook demonstrates the core StreetMapper workflow:

- YOLO11s training for one pothole class
- 80-epoch training run
- Video inference
- Confidence-based detection
- Location alert demonstration
- CSV logging of detections
- TFLite export attempt with INT8 quantization

### Verified notebook results

The final validation output in the notebook reports:

- Precision: 0.803
- Recall: 0.720
- mAP@50: 0.806
- mAP@50–95: 0.544

The validation output reports 395 images and 1,394 instances.

### Important implementation notes

The notebook uses simulated coordinates for the GPS component. It is therefore more accurate to describe the project as **GPS-ready / location-logging MVP** rather than a fully integrated live GPS mapping application.

The notebook also shows an INT8 TFLite export. Its output warns that no calibration `data` argument was provided and default COCO8 calibration data was used. This should be improved before claiming production-ready quantized deployment.
