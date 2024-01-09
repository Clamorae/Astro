def read_fits(path):
    with open(path,"r") as f:
        lines = f.readlines()
    
    for line in lines:
        print(line)


def create_header(image_path):

    header_line = []
    header_line.append("SIMPLE ="+" "*8+"T / file does conform to FITS Standard")
    header_line.append("BITPIX ="+" "*7+"16 / number of bits per data pixel")#TODO - depend on the image
    header_line.append("NAXIS  ="+" "*8+"2 / number of data axes")
    header_line.append("NAXIS1 ="+" "*6+"250 / length of data axis 1")#TODO - depend on the image
    header_line.append("NAXIS2 ="+" "*6+"300 / length of data axis 2")#TODO - depend on the image

    return header_line

def create_data_units():
    data_units_line = []
    return data_units_line

header = create_header("test")
for line in header:
    print(line)