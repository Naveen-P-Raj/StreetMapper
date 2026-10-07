# Architecture

```text
                ┌──────────────────┐
                │    Road Video    │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │     YOLO11s      │
                │ Object Detector  │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Pothole Boxes +  │
                │ Confidence Score │
                └────────┬─────────┘
                         ↓
                ┌──────────────────┐
                │ Confidence Filter│
                └────────┬─────────┘
                         ↓
              ┌──────────────────────┐
              │ GPS / Location Data  │
              │ (simulated in MVP)   │
              └──────────┬───────────┘
                         ↓
                ┌──────────────────┐
                │   CSV Detection  │
                │      Log         │
                └────────┬─────────┘
                         ↓
                Mapping / Dashboard
                   (future layer)
```

## Training

The notebook creates a one-class YAML configuration:

- `nc: 1`
- `names: [pothole]`

YOLO11s is trained for 80 epochs at 640px image size with batch size 16.

## Inference

Video frames are processed using streaming inference. Detections above the configured confidence threshold are recorded.

## Geolocation

The notebook demonstrates geolocation by assigning coordinates to detections. These are explicitly simulated coordinates in the current MVP. A production implementation should synchronize each detection with actual GPS readings.

## Output

CSV fields:

- Timestamp
- Latitude
- Longitude
- Issue_Type
- Confidence
