#!/usr/bin/env python

from PIL import Image

def hide_message(carrier, message, outfile):
    """Hides a message image within a carrier image, converting JPG to PNG if needed."""

    try:
        # Check for JPG files and convert to PNG if necessary
        if carrier.lower().endswith(".jpg"):
            carrier = convert_jpg_to_png(carrier)
        if message.lower().endswith(".jpg"):
            message = convert_jpg_to_png(message)

        # Open the carrier and message images
        c_image = Image.open(carrier)
        hide = Image.open(message)

        # Ensure the message image is smaller than or equal to the carrier image
        if hide.size > c_image.size:
            raise ValueError("Message image cannot be larger than carrier image.")

        # Resize the message image to match the carrier image's dimensions
        hide = hide.resize(c_image.size)
        hide = hide.convert('1')  # Convert the message image to black and white

        # Create a new image to store the combined result
        out = Image.new('RGB', c_image.size)

        # Iterate through each pixel of the carrier and message images
        width, height = c_image.size
        new_array = []
        for h in range(height):
            for w in range(width):
                ip = c_image.getpixel((w, h))  # Get the pixel from the carrier image
                hp = hide.getpixel((w, h))     # Get the corresponding pixel from the message image

                # Modify the least significant bit of the red channel to hide the message
                if hp == 0:
                    newred = ip[0] & 254  # Preserve the LSB if the message pixel is black
                else:
                    newred = ip[0] | 1    # Set the LSB if the message pixel is white

                # Create a new pixel with the modified red channel and the original green and blue channels
                new_array.append((newred, ip[1], ip[2]))

        # Fill the output image with the modified pixels
        out.putdata(new_array)

        # Save the output image
        out.save(outfile)
        print(f"Secret Image saved to {outfile}")

    except (IOError, OSError) as e:
        print(f"Error: {e}")

def convert_jpg_to_png(filename):
    """Converts a JPG image to PNG and returns the new filename."""

    new_filename = filename.replace(".jpg", ".png")
    with Image.open(filename) as img:
        img.save(new_filename, format="PNG")
    return new_filename

if __name__ == "__main__":
    carrier_file = input("Enter the carrier image file: ")
    message_file = input("Enter the message image file: ")
    output_file = input("Enter the output file name: ")
    hide_message(carrier_file, message_file, output_file)
