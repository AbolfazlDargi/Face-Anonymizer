# Real-Time Face Anonymizer (Privacy Blur) 🕵️‍♂️

A Python application that detects faces in real-time video streams and applies a Gaussian Blur to anonymize them. Built using OpenCV.

## 🌟 Features
- **Real-Time Detection:** Instantly detects faces from the webcam feed.
- **Privacy Protection:** Automatically blurs detected faces to hide identity.
- **No External Weights:** Uses OpenCV's built-in Haar Cascade classifiers (lightweight and fast).

## 🛠️ How It Works
1. **Detection:** The program converts the video frame to grayscale and uses the `Haar Cascade` algorithm to find face coordinates (x, y, w, h).
2. **ROI Extraction:** It crops the detected face area (Region of Interest) from the original frame.
3. **Processing:** A heavy `Gaussian Blur` filter is applied to the cropped area.
4. **Merging:** The blurred face is placed back into the original frame seamlessly.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/face-anonymizer.git](https://github.com/YOUR-USERNAME/face-anonymizer.git)
