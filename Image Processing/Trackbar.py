import cv2
import numpy as np

# Callback function for trackbar (does nothing)
def nothing(x):
    pass

# Create a window for trackbars
cv2.namedWindow("Trackbars")

# Initialize webcam
cam = cv2.VideoCapture(0)

# Create trackbars for HSV range adjustment
cv2.createTrackbar("H1", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S1", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V1", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("H2", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("S2", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V2", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Switch", "Trackbars", 0, 1, nothing)

# Define a kernel for morphological operations
kernel = np.ones((5, 5), dtype=np.uint8)

while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    # Convert frame to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions
    H1 = cv2.getTrackbarPos("H1", "Trackbars")
    S1 = cv2.getTrackbarPos("S1", "Trackbars")
    V1 = cv2.getTrackbarPos("V1", "Trackbars")
    H2 = cv2.getTrackbarPos("H2", "Trackbars")
    S2 = cv2.getTrackbarPos("S2", "Trackbars")
    V2 = cv2.getTrackbarPos("V2", "Trackbars")
    switch = cv2.getTrackbarPos("Switch", "Trackbars")

    # Define lower and upper HSV thresholds
    if switch == 1:
        lower = np.array([H1, S1, V1])
        upper = np.array([H2, S2, V2])
    else:
        lower = np.array([0, 0, 0])
        upper = np.array([0, 0, 0])

    # Apply morphological operations
    frame = cv2.erode(frame, kernel, iterations=1)
    frame = cv2.dilate(frame, kernel, iterations=1)

    # Create a mask and apply bitwise operation
    mask = cv2.inRange(hsv_frame, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display results
    cv2.imshow("Trackbars", hsv_frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
