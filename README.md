================================================================================
                  Image Analysis and Reporting Module Documentation
================================================================================

Welcome to the Image Analysis and Reporting Module documentation! This Python module
helps you analyze image files using different techniques, such as steganography
analysis, file signature analysis, and anomaly detection. It provides a way to preview
hidden file content, extract hidden files, and generate comprehensive reports.

How to Use:
1. Prerequisites:
    - Make sure you have Python 3.x installed on your system.
    - Install the required libraries:
        - OpenCV (cv2): You can install it using `pip install opencv-python`.
        - NumPy: You can install it using `pip install numpy`.
        - scikit-learn: You can install it using `pip install scikit-learn`.
        - Stegano: You can install it using `pip install stegano`.
        - Jinja2: You can install it using `pip install Jinja2`.

2. Import the Module:
    - In your Python script, import the `image_analysis_reporting_module` module.

3. Analyze an Image:
    - Call the `analyze_image()` function from the module and provide the path to the
      image file you want to analyze as an argument. For example:
      ```
      import image_analysis_reporting_module

      image_path = "path_to_your_image_file.jpg"
      image_analysis_reporting_module.analyze_image(image_path)
      ```

4. Preview and Extract Hidden Files:
    - If the module detects steganographic content in the image, it will display the
      hidden information in the console. You can view the hidden file content there.
    - If you want to save the hidden file to a specific location, the module provides
      extraction functionality that saves the hidden file as "hidden_file.txt" in an
      "output" folder. You can find the extracted file in the "output" folder.

5. Generate a Report:
    - The module generates a comprehensive report in HTML format, which contains
      relevant information about the analyzed image.
    - The report includes details such as file name, file type, file size, the presence
      of hidden files, file signature, a preview of the anomaly image, and the content
      of any hidden files.
    - The report is saved as "report.html" in the current working directory.
    - You can open the report in a web browser to view the information.

Code Flow and Working Explanation:
1. Importing the Required Libraries:
    - The necessary libraries, such as `os`, `cv2`, `imghdr`, `numpy`, `IsolationForest`
      from `sklearn.ensemble`, `lsb` from `stegano`, and `Environment`, `FileSystemLoader`
      from `jinja2`, are imported.

2. Defining the `analyze_image()` Function:
    - The `analyze_image()` function is defined, which takes the `image_path` as an
      argument.

3. File Signature Analysis:
    - The `imghdr.what()` function is used to determine the file signature of the
      provided image file. If the file signature is not recognized, an error message
      is displayed, indicating that it is not a valid image file.

4. Image Loading:
    - The `cv2.imread()` function is used to load the image from the specified `image_path`.
      The loaded image is stored in the `image` variable.

5. Steganography Analysis:
    - The `lsb.reveal()` function from the `stegano` library is used to check if the image
      contains any hidden steganographic content.
    - If any hidden data is detected, it is stored in the `secret_data` variable, which
      represents the hidden file content.

6. Anomaly Detection:
    - The `image` is reshaped into a 1D array using the `reshape()` method from `numpy`.
      The reshaped image is stored in the `flattened_image` variable.
    - An instance of the `IsolationForest` class from `sklearn.ensemble` is created
      with a contamination of 0.05, indicating the expected proportion of anomalies.
    - The `fit()` method is called on the model with `flattened_image` as the argument to
      train the model on the image data.
    - The `predict()` method is used to obtain the anomaly predictions for `flattened_image`.
      The predictions are stored in the `predictions` variable.
    - Anomalies are identified by filtering the `flattened_image` based on the negative
      predictions (`predictions == -1`). The anomaly pixels are stored in the
      `anomaly_pixels` variable.

7. Creating Anomaly Image:
    - An empty image, `anomaly_image`, with the same dimensions as the original image
      is created using the `np.zeros_like()` function. This will be used to highlight
      the anomaly pixels in the image.
    - The pixels corresponding to anomalies are marked in red (`[0, 0, 255]`) on
      `anomaly_image` using boolean indexing.

8. Previewing the Anomaly Image:
    - The `cv2.imshow()` function is used to display the `anomaly_image` with the
      anomalies highlighted in red.
    - The `cv2.waitKey(0)` function waits for a key press, and the `cv2.destroyAllWindows()`
      function closes the image window when a key is pressed.

9. Extracting Hidden Files:
    - If any hidden data is detected (`secret_data` is not empty), the `save_hidden_file()`
      function is called to save the hidden file.

10. Saving the Hidden File:
    - The `save_hidden_file()` function takes the `secret_data` as input and saves it as
      "hidden_file.txt" in the "output" folder. The "output" folder is created if it
      doesn't exist.

11. Generating a Report:
    - The `generate_report()` function is called to create a comprehensive report
      containing relevant information about the analyzed image.

12. Gathering Relevant Information:
    - The function gathers relevant information such as `file_name`, `file_type`,
      `file_size`, and `hidden_file_indicator`.

13. Preparing Report Data:
    - A `data` dictionary is created, containing the gathered information, as well as
      `signature` (file signature), `anomaly_image_path` (path to the anomaly image),
      and `hidden_file_content` (content of the hidden file).

14. Rendering the HTML Report Template:
    - The `Environment` class from the `jinja2` library is used to load the HTML report
      template. The template is rendered with the `data` dictionary to fill in the
      placeholders with the gathered information.

15. Saving the Report:
    - The generated report is saved as "report.html" in the current working directory.

16. Usage Example:
    - An example usage of the module is provided, where the `image_path` is set to the
      path of the image file you want to analyze.


Module Functions:
-----------------

1. `analyze_image(image_path: str) -> None`:
    This function analyzes the provided image file using various techniques, such as
    steganography analysis, file signature analysis, and anomaly detection. It displays
    the analysis results, including any hidden file content, previews of anomalies, and
    generates a comprehensive report.

    Parameters:
        - image_path (str): The path to the image file to be analyzed.

    Return Value:
        None

2. `save_hidden_file(secret_data: str) -> None`:
    This function saves the hidden file content to a specified location. The hidden file
    is saved as "hidden_file.txt" in an "output" folder.

    Parameters:
        - secret_data (str): The content of the hidden file to be saved.

    Return Value:
        None

3. `generate_report(image_path: str, file_name: str, file_type: str, file_size: str,
                    signature: str, anomaly_image_path: str, hidden_file_content: str) -> None`:
    This function generates a comprehensive HTML report with relevant information about
    the analyzed image, including file details, anomaly information, and hidden file
    content.

    Parameters:
        - image_path (str): The path to the analyzed image file.
        - file_name (str): The name of the analyzed image file.
        - file_type (str): The type (format) of the analyzed image file.
        - file_size (str): The size of the analyzed image file.
        - signature (str): The file signature of the analyzed image file.
        - anomaly_image_path (str): The path to the anomaly image file.
        - hidden_file_content (str): The content of the hidden file, if present.

    Return Value:
        None

4. `gather_information(image_path: str, has_hidden_file: bool) -> dict`:
    This function gathers relevant information about the analyzed image, such as file
    name, type, size, presence of a hidden file, and file signature.

    Parameters:
        - image_path (str): The path to the analyzed image file.
        - has_hidden_file (bool): Indicates whether a hidden file is detected.

    Return Value:
        A dictionary containing the gathered information.

5. `create_anomaly_image(image: np.ndarray, anomaly_pixels: np.ndarray) -> np.ndarray`:
    This function creates an image with highlighted anomaly pixels.

    Parameters:
        - image (np.ndarray): The original image.
        - anomaly_pixels (np.ndarray): An array of anomaly pixel coordinates.

    Return Value:
        The image with highlighted anomaly pixels.

6. `display_image(image: np.ndarray, window_name: str = "Image") -> None`:
    This function displays an image in a window.

    Parameters:
        - image (np.ndarray): The image to be displayed.
        - window_name (str): The name of the window (default: "Image").

    Return Value:
        None

7. `preprocess_image(image: np.ndarray) -> np.ndarray`:
    This function performs preprocessing on the image for anomaly detection. It reshapes
    the image into a 1D array.

    Parameters:
        - image (np.ndarray): The image to be preprocessed.

    Return Value:
        The preprocessed image (reshaped as a 1D array).

8. `detect_anomalies(image: np.ndarray) -> np.ndarray`:
    This function detects anomalies in the provided image using an Isolation Forest
    algorithm.

    Parameters:
        - image (np.ndarray): The image to be analyzed.

    Return Value:
        An array of anomaly predictions (-1 for anomalies, 1 for normal pixels).

9. `extract_hidden_data_from_image(image_path: str) -> str`:
    This function extracts hidden data from the image using steganography techniques.

    Parameters:
        - image_path (str): The path to the image file.

    Return Value:
        The extracted hidden data as a string, if present; otherwise, an empty string.

10. `get_file_signature(image_path: str) -> str`:
    This function retrieves the file signature of the provided image file.

    Parameters:
        - image_path (str): The path to the image file.

    Return Value:
        The file signature as a string.

11. `is_valid_image(image_path: str) -> bool`:
    This function checks if the provided file is a valid image file based on its file
    signature.

    Parameters:
        - image_path (str): The path to the image file.

    Return Value:
        True if the file is a valid image file; False otherwise.


Code Flow:
----------

The code implementation follows the following flow:

1. The necessary libraries, such as `os`, `cv2`, `imghdr`, `numpy`, `sklearn`, `stegano`,
   and `jinja2`, are imported.

2. The `analyze_image()` function is defined, which takes the `image_path` as an argument.

3. The `image_path` is checked for a valid image file using the `is_valid_image()`
   function.

4. The image is loaded using the `cv2.imread()` function.

5. The `extract_hidden_data_from_image()` function is called to check for hidden data in
   the image.

6. Anomaly detection is performed on the image using the `detect_anomalies()` function.

7. The anomaly pixels are identified.

8. The anomaly image is created using the `create_anomaly_image()` function.

9. The anomaly image is displayed using the `display_image()` function.

10. If hidden data is detected, it is saved using the `save_hidden_file()` function.

11. Relevant information about the analyzed image is gathered using the `gather_information()`
    function.

12. The report is generated using the `generate_report()` function.

Please note that the code is designed to be modular and reusable, with each function
serving a specific purpose. You can use these functions individually or combine them to
create your own image analysis workflows.

That concludes the documentation for the Image Analysis and Reporting Module. You can
refer to this documentation to understand the purpose and usage of each function in the
module.

Happy analyzing!
