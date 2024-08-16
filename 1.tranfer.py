from ultralytics.data.converter import convert_dota_to_yolo_obb
from ultralytics.data.split_dota import split_test, split_trainval
import PIL.Image

# for large images
PIL.Image.MAX_IMAGE_PIXELS = None

# ship ID = 1

def main():
    # convert dota to yolo format
    # convert_dota_to_yolo_obb("./")

    # split train and val set, with labels.
    split_trainval(
        data_root="C:/baidunetdiskdownload/DOTA-Merge/",
        save_dir="C:/baidunetdiskdownload/DOTA-Merge-Split/",
        rates=[0.5, 1.0, 1.5],  # multiscale
        gap=500,
    )

    # split test set, without labels.
    # split_test(
    #     data_root="path/to/DOTAv1.0/",
    #     save_dir="path/to/DOTAv1.0-split/",
    #     rates=[0.5, 1.0, 1.5],  # multiscale
    #     gap=500,
    # )



if __name__ == "__main__":
    main()