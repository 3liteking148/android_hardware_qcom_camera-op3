#!/bin/python3

with open('../QCamera2/stack/common/cam_intf.h', 'r') as f:
    data = f.read()
f.closed

start = data.find('    INCLUDE(CAM_INTF_META_HISTOGRAM')
end = data.find('} metadata_data_t;')
data = data[start:end]
metadata = data.split("\n")

metalist = list()

for line in metadata:
    if (line.startswith('    INCLUDE')):
        foo = line.split(',')
        foo[0] = foo[0].replace('INCLUDE', 'PRINT')

        # Compilation errors
        if foo[0].find("CAM_INTF_META_LENS_FOCUS_STATE") == -1 and foo[0].find("CAM_INTF_META_ASD_SCENE_CAPTURE_TYPE") == -1:
            metalist.append(foo[0] + ",    pMetadata);")

with open('list.txt', 'w') as f:
    for item in metalist:
        f.write("%s\n" % item)
f.closed
