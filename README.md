# StreetMapper 🚧

**AI-based road damage detection with YOLO11s, video inference, GPS-tagged detections, and mobile-oriented TFLite export.**

StreetMapper is a computer-vision MVP that detects **potholes** from road video and records detected issues with location information. The implementation uses **YOLO11s** and is designed to be developed and tested in Google Colab.

## Project Overview

Road-condition monitoring is often manual and expensive. StreetMapper explores an automated pipeline that can process road video, detect potholes, associate detections with geographic coordinates, and export the results for downstream mapping or dashboard applications.

### Current MVP pipeline

```text
Road Video
    ↓
YOLO11s Object Detection
    ↓
Pothole Detection
    ↓
Confidence Filtering
    ↓
GPS / Location Association
    ↓
CSV Detection Log
    ↓
Potential Mapping / Dashboard
```

## Current Scope

The supplied implementation is a **single-class pothole detector**:

- Class: `pothole`
- Model: YOLO11s
- Training: 80 epochs
- Image size: 640
- Batch size: 16
- Dataset configuration: YOLO-format train/validation folders
- Validation images reported by the training run: 395
- Validation instances reported by the training run: 1,394
- Training environment: Google Colab GPU workflow

## Reported Training Results

The original notebook's final validation output reports:

| Metric | Reported value |
|---|---:|
| Precision | **80.3%** |
| Recall | **72.0%** |
| mAP@50 | **80.6%** |
| mAP@50–95 | **54.4%** |

These numbers are preserved from the notebook output and should be described as results from that training run.

## Detection and GPS Logging

The notebook demonstrates two inference ideas:

1. Triggering a location alert when a pothole is detected.
2. Writing detections to a CSV file with:

```text
Timestamp, Latitude, Longitude, Issue_Type, Confidence
```

The current notebook uses **simulated GPS coordinates** for the MVP. A production system should replace this with actual GPS sensor data or a synchronized GPS log.

## TFLite Export

The notebook also demonstrates exporting the YOLO model to TensorFlow Lite with INT8 quantization for mobile-oriented deployment.

> Note: the notebook output indicates that INT8 export used the default COCO8 calibration data because a calibration `data` argument was not supplied. For a production quantized model, calibration should use representative data from the actual pothole dataset.

## Repository Structure

```text
StreetMapper/
├── README.md
├── PROJECT_STATUS.md
├── requirements.txt
├── LICENSE
├── .gitignore
│
├── notebooks/
│   └── Street_mapper_original.ipynb
│
├── src/
│   ├── train.py
│   ├── infer_video.py
│   ├── export_tflite.py
│   └── export_detections_csv.py
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── PROJECT_DESCRIPTION.md
│   └── MODEL_CARD.md
│
├── data/
│   └── README.md
│
├── models/
│   └── README.md
│
└── results/
    └── README.md
```

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare a YOLO-format dataset

The notebook expects:

```text
train/
├── images/
└── labels/

valid/
├── images/
└── labels/
```

with one class:

```yaml
nc: 1
names:
  - pothole
```

### 3. Train

```bash
python src/train.py \
  --data /path/to/pothole_config.yaml \
  --epochs 80 \
  --imgsz 640 \
  --batch 16
```

### 4. Run video inference

```bash
python src/infer_video.py \
  --model /path/to/best.pt \
  --source sample_video.mp4 \
  --conf 0.5
```

### 5. Export TFLite

```bash
python src/export_tflite.py \
  --model /path/to/best.pt
```

For proper INT8 calibration, supply representative project data when supported by the Ultralytics export configuration.

## Limitations

This repository intentionally documents the implementation as it actually exists.

- The current detector has one class: pothole.
- GPS association is simulated in the notebook.
- The dataset itself is not included.
- The trained `best.pt` weights are not included because they were not supplied with the notebook.
- The sample road video is not included.
- The notebook's TFLite export used default calibration data rather than a project-specific calibration dataset.
- A complete production mapping/dashboard/API layer is not implemented in the supplied notebook.

## Future Improvements

- Add multiple road-infrastructure classes.
- Replace simulated GPS with live GPS or synchronized GPS logs.
- Deduplicate repeated detections across consecutive frames.
- Build a map-based dashboard.
- Add severity classification.
- Use project-specific representative data for INT8 calibration.
- Add model tracking and deployment monitoring.
- Package inference as a mobile or edge application.

## Credits

Developed as an AI/Data Science project using Python, Ultralytics YOLO, OpenCV-compatible video workflows, and TensorFlow Lite export.
