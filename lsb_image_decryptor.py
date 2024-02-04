from PIL import Image

def extract(carrier, outfile):
    """Extracts a hidden image from a carrier image using least significant bit (LSB) steganography.

    Args:
        carrier (str): Path to the carrier image file.
        outfile (str): Path to the output file for the extracted image.
    """

    try:
        # Open the carrier image
        c_image = Image.open(carrier)

        # Create a new grayscale image with the same dimensions as the carrier
        out = Image.new('L', c_image.size)

        # Get the width and height of the carrier image
        width, height = c_image.size

        # Create an empty list to store the extracted pixel values
        new_array = []

        # Iterate through each pixel in the carrier image
        for h in range(height):
            for w in range(width):
                # Get the RGB pixel value at the current position
                ip = c_image.getpixel((w, h))

                # Extract the least significant bit from the red channel
                new_red = ip[0] & 1

                # Append the extracted bit (0 or 255) to the new image array
                new_array.append(new_red)

        # Set the pixel data of the output image using the extracted bits
        out.putdata(new_array)

        # Save the extracted image with maximum quality
        out.save(outfile, quality=100)

        print("Message extracted \n")

    except (IOError, OSError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Prompt the user for the carrier and output file names
    carrier_file = input("Enter the carrier image file: ")
    output_file = input("Enter the output file name for the extracted image: ")

    # Call the extract function to perform the extraction
    extract(carrier_file, output_file)
