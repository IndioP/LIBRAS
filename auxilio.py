from os import listdir

import csv

files = listdir('DATASET')
csv_file = open('fullConvertedDataset.csv',"w")
csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csv_writer.writerow(["left_or_right","WRIST.x","WRIST.y","WRIST.z","THUMB_CMC.x","THUMB_CMC.y","THUMB_CMC.z","THUMB_MCP.x","THUMB_MCP.y","THUMB_MCP.z","THUMB_IP.x","THUMB_IP.y","THUMB_IP.z","THUMB_TIP.x","THUMB_TIP.y","THUMB_TIP.z","INDEX_FINGER_MCP.x","INDEX_FINGER_MCP.y","INDEX_FINGER_MCP.z","INDEX_FINGER_PIP.x","INDEX_FINGER_PIP.y","INDEX_FINGER_PIP.z","INDEX_FINGER_DIP.x","INDEX_FINGER_DIP.y","INDEX_FINGER_DIP.z","INDEX_FINGER_TIP.x","INDEX_FINGER_TIP.y","INDEX_FINGER_TIP.z","MIDDLE_FINGER_MCP.x","MIDDLE_FINGER_MCP.y","MIDDLE_FINGER_MCP.z","MIDDLE_FINGER_PIP.x","MIDDLE_FINGER_PIP.y","MIDDLE_FINGER_PIP.z","MIDDLE_FINGER_DIP.x","MIDDLE_FINGER_DIP.y","MIDDLE_FINGER_DIP.z","MIDDLE_FINGER_TIP.x","MIDDLE_FINGER_TIP.y","MIDDLE_FINGER_TIP.z","RING_FINGER_MCP.x","RING_FINGER_MCP.y","RING_FINGER_MCP.z","RING_FINGER_PIP.x","RING_FINGER_PIP.y","RING_FINGER_PIP.z","RING_FINGER_DIP.x","RING_FINGER_DIP.y","RING_FINGER_DIP.z","RING_FINGER_TIP.x","RING_FINGER_TIP.y","RING_FINGER_TIP.z","PINKY_MCP.x","PINKY_MCP.y","PINKY_MCP.z","PINKY_PIP.x","PINKY_PIP.y","PINKY_PIP.z","PINKY_DIP.x","PINKY_DIP.y","PINKY_DIP.z","PINKY_TIPPINKY_TIP.x","PINKY_TIPPINKY_TIP.y","PINKY_TIPPINKY_TIP.z","label"])

for f in files:
    with open('DATASET/'+f) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count+=1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                row.append(f[0])
                csv_writer.writerow(row)
                print(row)
                
        