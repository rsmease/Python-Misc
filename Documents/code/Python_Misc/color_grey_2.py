# An array of size N x M represents pixels of an image. Each cell of this array contains an array of size 3 with the pixel's color information: [R,G,B]

# Convert the color image, into an average greyscale image.

# The [R,G,B] array contains integers between 0 and 255 for each color.

# To transform a color pixel into a greyscale pixel, average the values of that pixel:

# p = [R,G,B] => [(R+G+B)/3, (R+G+B)/3, (R+G+B)/3]
# Note: the values for the pixel must be integers, therefore you should round floats to the nearest integer.

# Example

# Here's an example of a 2x2 image:

test1 = [
 [ [123, 231, 12], [56, 43, 124] ],
 [ [78, 152, 76], [64, 132, 200] ]
]
# Here's the expected image after transformation:

# [
#  [ [122, 122, 122], [74, 74, 74] ],
#  [ [102, 102, 102], [132, 132, 132] ]
# ]
# 
# PYTHON
# 
# FAILED; NOT SURE WHY, MY PYTHON IS RUSTY

def color_2_grey(colors):
    # your code here
    gray_scale = []
    for row in range(len(colors)):
    	new_row = []
    	for col in range(len(colors[0])):
    		color_average = sum(colors[row][col])/3
    		new_row.append([color_average, color_average, color_average])
		gray_scale.append(new_row)

	return gray_scale

print color_2_grey(test1)
