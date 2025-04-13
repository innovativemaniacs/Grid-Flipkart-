import cv2
import easyocr

def run_easyocr():

    # Initialize the EasyOCR Reader (you can specify more languages if needed)- English
    reader = easyocr.Reader(['en'])

    # Open the default camera
    cap = cv2.VideoCapture(0)  # '0' is the default camera

    if not cap.isOpened():
        print("Error: Could not open video stream.")
        exit()

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture video.")
            break

        # Resize the frame for better OCR performance (optional)
        resized_frame = cv2.resize(frame, None, fx=0.75, fy=0.75)

        # Perform OCR on the frame
        result = reader.readtext(resized_frame)

        # Draw bounding boxes and text on the frame
        for (bbox, text, prob) in result:
            # Get the coordinates of the bounding box
            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = tuple([int(val) for val in top_left])
            bottom_right = tuple([int(val) for val in bottom_right])

            # Draw the bounding box around the detected text
            cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

            # Display the detected text on the frame
            cv2.putText(frame, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

        # Display the frame with OCR results
        cv2.imshow('OCR - Press Q to Quit', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()
