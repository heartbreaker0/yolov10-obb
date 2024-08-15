from ultralytics import YOLO


def main():
    model = YOLO("yolov10n-obb.yaml")

    result = model.train(data="DOTAv1.yaml", epochs=1000, imgsz=1024, batch=8, device=0)


if __name__ == "__main__":
    main()
