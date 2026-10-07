# Data

The original training dataset is not included in this repository.

The notebook expects YOLO-format image/label directories:

```text
train/
  images/
  labels/
valid/
  images/
  labels/
```

The project uses a single class:

```yaml
nc: 1
names:
  - pothole
```

Do not commit private, restricted, or redistributable datasets without confirming their license.
