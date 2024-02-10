from picamera import PiCamera
import os

# Picture Paths 
pgallery_directory = "/home/michaelberkman/Desktop/ChaelCam/pgallery/"
pgalnamer_file = "pgalnamer.txt"
pgalnamer_path = "/home/michaelberkman/Desktop/ChaelCam/"

# Video Paths 
vgallery_directory = "/home/michaelberkman/Desktop/ChaelCam/vgallery/"
vgalnamer_file = "vgalnamer.txt"
vgalnamer_path = "/home/michaelberkman/Desktop/ChaelCam/"

# Variables
photoname = 0
camera = PiCamera()

while True:  # Infinite loop
    camera.start_preview()
    user_input = input("Press 'ENTER' to snap a picture, 'r' to record or 'e' to exit: ")

    if user_input == "":
        photoname_str = str(photoname)
        # Read the pgalnamer.txt file to check if the filename exists
        with open(os.path.join(pgalnamer_path, pgalnamer_file), "r") as file:
            contents = file.read()

        # If photoname_str is in file, increment it until we find a unique name
        while photoname_str + ".jpg" in contents:
            photoname += 1
            photoname_str = str(photoname)

        # Create the full path for the image file with the unique photoname_str
        filename = os.path.join(pgallery_directory, photoname_str.zfill(3) + ".jpg")
        # Capture and save the image with the specified filename
        camera.capture(filename)

        # Write the unique image filename to the pgalnamer.txt file
        with open(os.path.join(pgalnamer_path, pgalnamer_file), "a") as file:
            file.write(photoname_str + ".jpg" + '\n')

    elif user_input == "r":
        videoname_str = str(photoname)

        with open(os.path.join(vgalnamer_path, vgalnamer_file), "r") as file:
            contents = file.read()

        # Check for a unique video name
        while videoname_str + ".h264" in contents:
            photoname += 1
            videoname_str = str(photoname)

        filename = os.path.join(vgallery_directory, videoname_str.zfill(3) + ".h264")

        camera.start_recording(filename)
        print("Recording... Press 'r' again to stop recording")
        while True:
            user_input = input()
            if user_input == "r":
                camera.stop_recording()
                break
            else:
                print("Invalid input. Press 'r' to stop recording")

        with open(os.path.join(vgalnamer_path, vgalnamer_file), "a") as file:
            file.write(videoname_str + ".h264" + '\n')

    elif user_input == "e":
        print("Exiting...")
        camera.stop_preview()
        break  # Exit the loop

    else:
        print("Invalid input")
from picamera import PiCamera
import os

# Paths
pgallery_directory = "/home/michaelberkman/Desktop/ChaelCam/pgallery/"
pgalnamer_file = "pgalnamer.txt"
pgalnamer_path = "/home/michaelberkman/Desktop/ChaelCam/"

# Variables
photoname = 0
camera = PiCamera()

while True:  # Infinite loop
    camera.start_preview()
    user_input = input("Press 'ENTER' to snap a picture or 'e' to exit: ")

    if user_input == "":
        photoname_str = str(photoname)
        # Read the pgalnamer.txt file to check if the filename exists
        with open(os.path.join(pgalnamer_path, pgalnamer_file), "r") as file:
            contents = file.read()

        # If photoname_str is in file, increment it until we find a unique name
        while photoname_str + ".jpg" in contents:
            photoname += 1
            photoname_str = str(photoname)

        # Create the full path for the image file with the unique photoname_str
        filename = os.path.join(pgallery_directory, photoname_str.zfill(3) + ".jpg")
        # Capture and save the image with the specified filename
        camera.capture(filename)

        # Write the unique image filename to the pgalnamer.txt file
        with open(os.path.join(pgalnamer_path, pgalnamer_file), "a") as file:
            file.write(photoname_str + ".jpg" + '\n')

    elif user_input == "e":
        print("Exiting...")
        break  # Exit the loop

    else:
        print("Invalid input")

camera.stop_preview()
