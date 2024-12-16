# Real-Time Hand Tracking using OpenCV and Mediapipe

This project demonstrates real-time hand tracking using Python, OpenCV, and Mediapipe. The application uses a webcam to detect and visualize hand landmarks and connections in a live video feed.

## Features
- Real-time hand detection and tracking.
- Visualization of hand landmarks and connections.
- Supports up to two hands simultaneously.
- Easy-to-understand implementation using Mediapipe's Hand module.

## Requirements
Make sure you have the following installed:
- Python 3.7 or later
- OpenCV (`cv2`)
- Mediapipe

You can install the required libraries using pip:
```bash
pip install opencv-python mediapipe
```

## How It Works
1. **Video Capture**: The script uses OpenCV to capture video from the default webcam.
2. **Hand Detection**: Mediapipe's Hand module detects and tracks hand landmarks in the video feed.
3. **Landmark Visualization**: Detected landmarks and hand connections are drawn on the video feed in real-time.
4. **Quit Option**: Press the `q` key to exit the application.
