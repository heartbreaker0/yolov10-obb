from ultralytics import YOLO


def main():
    model = YOLO("yolov8n-obb.yaml")

    result = model.train(data="/openbayes/home/yolov10-obb/DOTA-SHIP.yaml", epochs=1000, imgsz=1024, batch=8, device=0, pretrained=False, plots=True)


if __name__ == "__main__":
    main()
