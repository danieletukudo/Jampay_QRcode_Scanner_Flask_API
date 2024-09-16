
# Real Time QR code Detector and Text Extractor Web App

![Barcode Detection Example](image.png)
This project is a real-time QR code detection and text extraction web application built using Flask, OpenCV and pyzbar. It captures video from a webcam, detects barcodes, decodes the text embedded in the barcodes, and displays the decoded text on the video stream. The application is optimized for real-time performance, making it suitable for various interactive applications.

## Features

- Real-time video capture and processing using OpenCV.
- Barcode detection and text extraction using `pyzbar`.
- Dynamic video streaming in a web application using Flask.
- Overlay of decoded text on the video feed.
- Easily extendable for various types of barcode and text extraction requirements.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Dependencies

The project requires the following Python packages:

- Flask: For creating the web application.
- OpenCV: For video capture and frame processing.
- NumPy: For numerical operations.
- Pyzbar: For barcode detection and decoding.

You can install these dependencies using the following command:

```bash
pip install flask opencv-python numpy pyzbar
```

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/danieletukudo/Real-Time-QRcode-Detector-and-Text-Extractor-Web-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Real-Time-QRcode-Detector-and-Text-Extractor-Web-App
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Open your web browser and navigate to `http://localhost:5000` to see the barcode detection in action.

## Usage

- Launch the application using the instructions above.
- Once the webcam feed is visible, the application will automatically detect barcodes in the video stream.
- The decoded text will be displayed on the video feed.
- Use this setup for testing barcode detection or as a starting point for more complex barcode-related projects.

## Project Structure

- `app.py`: The main application file containing the Flask app and barcode detection logic.
- `templates/`: Directory containing the HTML template for the web application.
    - `index.html`: The main HTML file rendered by Flask.
- `static/`: Directory for static files (CSS, JavaScript), if any.
- `README.md`: Project documentation and setup instructions.

## Class Overview

### `QrcodeDetector`

- **Purpose**: Captures video from the webcam, detects QRcodes, decodes their content, and annotates the video feed with the decoded text.
- **Methods**:
  - `__init__()`: Initializes the video capture and sets the camera resolution.
  - `gen_frames()`: Captures frames, detects QRcodes, decodes and annotates the frames, and yields them for streaming.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or create an Issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/): Lightweight WSGI web application framework.
- [OpenCV](https://opencv.org/): Open-source computer vision library.
- [Pyzbar](https://pypi.org/project/pyzbar/): Python wrapper for zbar library.

## Contact

If you have any questions or suggestions, feel free to contact me at danielsamueletukudo@gmail.com and on linkedin@ https://www.linkedin.com/in/daniel-etukudo
