import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--conf", type=float, default=0.5)
    args = parser.parse_args()

    model = YOLO(args.model)

    for result in model.predict(source=args.source, conf=args.conf, stream=True):
        if len(result.boxes):
            confidence = float(result.boxes.conf[0])
            print(f"Damage detected | confidence={confidence:.2f}")

if __name__ == "__main__":
    main()
