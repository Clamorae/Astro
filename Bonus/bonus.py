from PIL import Image

def convert_image(path):

    with open(path,"rb") as f:
        content = f.readlines()

    img_array = []
    max_size = 0
    for line in content:
        line = line.hex()
        hex_line = [line[i:i+2] for i in range(0, len(line), 2)]
        img_array.append(hex_line)

        if len(hex_line)>max_size:
            max_size = len(hex_line)
    return(img_array,max_size)

def convert_image(image_path):
    img = Image.open(image_path)
    pixel_matrix = list(img.getdata())
    width, height = img.size
    pixel_matrix = [pixel_matrix[i * width:(i + 1) * width] for i in range(height)]

    return pixel_matrix


def create_header(image):

    header_line = []
    header_line.append("SIMPLE ="+" "*8+"T / file does conform to FITS Standard")
    header_line.append("BITPIX ="+" "*8+"8 / number of bits per data pixel")
    header_line.append("NAXIS  ="+" "*8+"3 / number of data axes")
    header_line.append("NAXIS1 ="+" "*(9-(len(str(len(image)))))+f"{len(image)} / length of data axis 1")
    header_line.append("NAXIS2 ="+" "*(9-(len(str(len(image[0])))))+f"{len(image[0])} / length of data axis 2")
    header_line.append("NAXIS3 ="+" "*8+"3 / length of data axis 3")

    return header_line

def table_to_str(table):
    string = ""
    for filter in table:
        for row in filter:
            for pixel in row:
                string = string + pixel.upper() + " "
            string = string + "\n"
    return string

def create_data_units(img):
    naxis1 = []
    naxis2 = []
    naxis3 = []

    for row in img:
        naxis1_line = []
        naxis2_line = []
        naxis3_line = []
        for pixel in row:
            naxis1_line.append(hex(pixel[0])[-2:])
            naxis2_line.append(hex(pixel[1])[-2:])
            naxis3_line.append(hex(pixel[2])[-2:])
        naxis1.append(naxis1_line)
        naxis2.append(naxis2_line)
        naxis3.append(naxis3_line)
    
    return table_to_str([naxis1,naxis2,naxis3])

img = convert_image("./Bonus/test.jpg")

header = create_header(img)
for line in header:
    print(line)

data_units = create_data_units(img)
print(data_units)