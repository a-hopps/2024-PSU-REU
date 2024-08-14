import cv2

from ultralytics import YOLO, solutions


def count_objects_in_region(region_points, video_path, output_video_path, model_path):
    """Count objects in a specific region within a video."""
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))
    counter = solutions.ObjectCounter(
        view_img=True, reg_pts=region_points, names=model.names, draw_tracks=True, line_thickness=2
    )

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or video processing has been successfully completed.")
            break
        tracks = model.track(im0, persist=True, show=False)
        im0 = counter.start_counting(im0, tracks)
        video_writer.write(im0)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()

crosswalk1 = [(20, 400), (1080, 404), (1080, 360), (20, 360)]
crosswalk2 = [(), (), (), ()]
crosswalk3 = [(), (), (), ()]
crosswalk4 = [(), (), (), ()]

count1 = count_objects_in_region(crosswalk1, "path/to/video.mp4", "output_video.avi", "model.pt")
count2 = count_objects_in_region(crosswalk2, "path/to/video.mp4", "output_video.avi", "model.pt")
count3 = count_objects_in_region(crosswalk3, "path/to/video.mp4", "output_video.avi", "model.pt")
count4 = count_objects_in_region(crosswalk4, "path/to/video.mp4", "output_video.avi", "model.pt")