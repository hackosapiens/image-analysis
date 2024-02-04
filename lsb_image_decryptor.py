from PIL import Image

def extract(carrier, outfile):
    """Extracts a hidden image from a carrier image."""

    try:
        c_image = Image.open(carrier)
        out = Image.new('L', c_image.size)
        width, height = c_image.size
        new_array = []

        for h in range(height):
            for w in range(width):
                ip = c_image.getpixel((w, h))
                if ip[0] & 1 == 0:
                    new_array.append(0)
                else:
                    new_array.append(255)

        out.putdata(new_array)
        out.save(outfile, quality=100)
        print("Message extracted \n")

    except (IOError, OSError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    carrier_file = input("Enter the carrier image file: ")
    output_file = input("Enter the output file name for the extracted image: ")
    extract(carrier_file, output_file)
