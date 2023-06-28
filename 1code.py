import os
import cv2
import imghdr
import numpy as np
from sklearn.ensemble import IsolationForest
from stegano import lsb
from jinja2 import Environment, FileSystemLoader

def analyze_image(image_path):
    # File signature analysis
    signature = imghdr.what(image_path)
    if signature is None:
        print("Not a valid image file.")
        return

    # Load the image
    image = cv2.imread(image_path)

    # Steganography analysis
    secret_data = lsb.reveal(image)
    if secret_data:
        print("Steganographic content found:")
        print(secret_data)

    # Anomaly detection
    flattened_image = image.reshape(-1, 3)
    model = IsolationForest(contamination=0.05)
    model.fit(flattened_image)
    predictions = model.predict(flattened_image)
    anomaly_pixels = flattened_image[predictions == -1]

    # Create an anomaly image
    anomaly_image = np.zeros_like(image)
    anomaly_image[predictions.reshape(image.shape[:-1]) == -1] = [0, 0, 255]

    # Show the anomaly image
    cv2.imshow("Anomaly Image", anomaly_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Extraction functionality
    if secret_data:
        save_hidden_file(secret_data)

    # Generate report
    generate_report(image_path, signature, secret_data, anomaly_image)

def save_hidden_file(secret_data):
    # Save the hidden file to a specified location
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "hidden_file.txt")
    with open(output_path, "w") as f:
        f.write(secret_data)
    print("Hidden file extracted and saved to: " + output_path)

def generate_report(image_path, signature, secret_data, anomaly_image):
    # Gather relevant information
    file_name = os.path.basename(image_path)
    file_type = imghdr.what(image_path)
    file_size = os.path.getsize(image_path)
    hidden_file_indicator = "Yes" if secret_data else "No"

    # Prepare report data
    data = {
        "file_name": file_name,
        "file_type": file_type,
        "file_size": file_size,
        "hidden_file_indicator": hidden_file_indicator,
        "signature": signature,
        "anomaly_image_path": "anomaly_image.jpg",
        "hidden_file_content": secret_data
    }

    # Render the HTML report template
    template_env = Environment(loader=FileSystemLoader("."))
    template = template_env.get_template("report_template.html")
    report_html = template.render(data)

    # Save the report as an HTML file
    report_path = "report.html"
    with open(report_path, "w") as f:
        f.write(report_html)
    print("Report generated and saved to: " + report_path)

# Usage example
image_path = "path_to_your_image_file.jpg"
analyze_image(image_path)

