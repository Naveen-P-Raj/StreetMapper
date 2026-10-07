import argparse
from ultralytics import YOLO

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--int8", action="store_true")
    args = parser.parse_args()

    model = YOLO(args.model)
    kwargs = {"format": "tflite"}
    if args.int8:
        kwargs["int8"] = True

    exported = model.export(**kwargs)
    print(f"Exported model: {exported}")

if __name__ == "__main__":
    main()
