from ultralytics import YOLO

def main():
    # Load a model
    # model = YOLO("YOLOv10-OBB/pretrained/yolov10n-obb.pt")  # load an official model
    # model = YOLO("yolov8n-obb.pt")
    model = YOLO("./runs/obb/train7/weights/best.pt")  # load a custom model

    # Validate the model
    metrics = model.val(data="DOTAv1.yaml")
    # metrics = model.val(data="DOTAv1.5.yaml")  # no arguments needed, dataset and settings remembered
    # metrics = model.val(data="dota8.yaml")
    metrics.box.map  # map50-95(B)
    metrics.box.map50  # map50(B)
    metrics.box.map75  # map75(B)
    metrics.box.maps  # a list contains map50-95(B) of each category


if __name__ == "__main__":
    main()