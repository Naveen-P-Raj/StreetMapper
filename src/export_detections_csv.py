import argparse
import csv
import datetime
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", default="pothole_detections.csv")
    parser.add_argument("--conf", type=float, default=0.5)
    parser.add_argument("--base-lat", type=float, default=19.0760)
    parser.add_argument("--base-lon", type=float, default=72.8777)
    args = parser.parse_args()

    model = YOLO(args.model)

    with open(args.output, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Latitude", "Longitude", "Issue_Type", "Confidence"])

        for i, result in enumerate(
            model.predict(source=args.source, conf=args.conf, stream=True)
        ):
            for box in result.boxes:
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = model.names[cls]

                # Mirrors the supplied notebook's simulated GPS logic.
                lat = args.base_lat + i * 0.00001
                lon = args.base_lon + i * 0.00001
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                writer.writerow([timestamp, lat, lon, label, f"{conf:.2f}"])

    print(f"Saved detections to {args.output}")

if __name__ == "__main__":
    main()
