import cv2
import os

# Folder containing the images
image_folder = '/root/Pictures/'
output_video = 'output_video.mp4'

# Get list of image files
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
if not images:
    print("No images found in the specified folder")
else:
    # Read the first image to get dimensions
    first_image_path = os.path.join(image_folder, images[0])
    frame = cv2.imread(first_image_path)
    
    if frame is None:
        print(f"Unable to read the image {first_image_path}")
    else:
        height, width, layers = frame.shape

        # Initialize the video writer
        video = cv2.VideoWriter(output_video, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))

        # Write each image to the video
        for image in images:
            image_path = os.path.join(image_folder, image)
            frame = cv2.imread(image_path)
            
            if frame is None:
                print(f"Warning: Unable to read the image {image_path}, skipping.")
                continue

            video.write(frame)

        # Release the video writer
        video.release()
        print(f"Video saved as {output_video}")

