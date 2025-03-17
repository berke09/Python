import cv2
import datetime
import time


def open_photo(filename):
    path = f"C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{filename}"
    photo = cv2.imread(path)
    cv2.imshow("Window", photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def convert_to_gray(filename):
    path = f"C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{filename}"
    photo = cv2.imread(path)
    gray = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Window", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def live_video():
    cam = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\video_output.avi", fourcc, 30.0, (640, 480))

    while cam.isOpened():
        ret, frame = cam.read()
        cv2.putText(frame, str(datetime.datetime.now()), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        out.write(frame)
        cv2.imshow("Window", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()


def photo_properties(filename):
    path = f"C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{filename}"
    photo = cv2.imread(path)
    height, width, channels = photo.shape
    print(f"Photo Width: {width}\nPhoto Height: {height}\nColor Channels: {channels}")
    print(f"Photo Type: {photo.dtype}")


def video_properties(filename):
    choice = int(input("1 - Live video\n2 - Existing video\nYour choice: "))
    path = f"C:\\Users\\Abra v15.8\\Desktop\\oc.resimler\\{filename}"

    if choice == 1:
        cam = cv2.VideoCapture(0)
        print(cam.get(3))  # Width
        print(cam.get(4))  # Height
        while cam.isOpened():
            ret, frame = cam.read()
            cv2.imshow("Window", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()
    else:
        cam = cv2.VideoCapture(path)
        print(cam.get(3))  # Width
        print(cam.get(4))  # Height
        while True:
            ret, frame = cam.read()
            cv2.imshow("Window", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        cam.release()
        cv2.destroyAllWindows()


def take_photo():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        take = int(input("Press 1 to take a photo: "))
        if take == 1:
            ret, frame = cam.read()
            cv2.imshow("Window", frame)
            print("Photo captured successfully!")
            cv2.waitKey(0)
            cam.release()
            cv2.destroyAllWindows()
            break


def main():
    try:
        while True:
            print("********** WELCOME TO OUR APPLICATION **********\n")
            choice = int(input(
                "1 - View a photo\n2 - Convert a photo to grayscale\n3 - Record a video\n4 - Get photo properties\n5 - Get video properties\n6 - Take a photo\n7 - Exit\nYour choice: "))

            if choice == 1:
                filename = input("Enter the filename with extension: ")
                open_photo(filename)
            elif choice == 2:
                filename = input("Enter the filename with extension: ")
                convert_to_gray(filename)
            elif choice == 3:
                live_video()
            elif choice == 4:
                filename = input("Enter the filename with extension: ")
                photo_properties(filename)
            elif choice == 5:
                filename = input("Enter the filename with extension (or leave empty for live video): ")
                video_properties(filename)
            elif choice == 6:
                take_photo()
            elif choice == 7:
                print("Thank you! Exiting...")
                break
            else:
                print("Invalid choice! Try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Try restarting the program.")


if __name__ == "__main__":
    main()