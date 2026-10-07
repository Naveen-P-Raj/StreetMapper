# Model Card

## Model

YOLO11s fine-tuned for pothole detection.

## Intended use

Portfolio/research prototype for detecting potholes in road video.

## Classes

- pothole

## Training configuration

- Epochs: 80
- Image size: 640
- Batch size: 16
- Ultralytics YOLO workflow

## Reported validation performance

- Precision: 80.3%
- Recall: 72.0%
- mAP@50: 80.6%
- mAP@50–95: 54.4%

## Limitations

Performance may vary with road type, weather, camera angle, lighting, motion blur, and pothole appearance. GPS integration in the supplied notebook is simulated. The model should be evaluated on representative deployment data before real-world use.
