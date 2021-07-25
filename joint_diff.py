import csv

list = [1, 8, 13, 17]

dates = ["2021-07-23-15-03-49", "2021-07-23-15-04-08", "2021-07-23-15-04-27", "2021-07-23-15-04-58"]

for date in dates:
    fname = date + "_people_"

    for i in list:
        file = open("./" + fname + str(i) + "_normal.csv", "r")
        rf = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        wf = open("./" + fname + str(i) + "_j_diff.csv", "w")
        wf.write("HEAD_x,HEAD_y,NECK_x,NECK_y,RIGHT_SHOULDER_x,RIGHT_SHOULDER_y,RIGHT_ELBOW_x,RIGHT_ELBOW_y,RIGHT_WRIST_x,RIGHT_WRIST_y,LEFT_SHOULDER_x,LEFT_SHOULDER_y,LEFT_ELBOW_x,LEFT_ELBOW_y,LEFT_WRIST_x,LEFT_WRIST_y,RIGHT_HIP_x,RIGHT_HIP_y,RIGHT_KNEE_x,RIGHT_KNEE_y,RIGHT_ANKLE_x,RIGHT_ANKLE_y,LEFT_HIP_x,LEFT_HIP_y,LEFT_KNEE_x,LEFT_KNEE_y,LEFT_ANKLE_x,LEFT_ANKLE_y,CHEST_x,CHEST_y\n")
        header = next(rf)
        
        for row in rf:
            for i in range(len(row)):
                if(int(i%3) == 0):
                    continue
                elif(int(i/3) != 4 and int(i/3) != 7 and int(i/3) != 10 and int(i/3) != 13 and i < 43):
                    wf.write(str(float(row[i])-float(row[i+3])) + ",")
                # if i != len(row)-2:
                
                # else:
                #     wf.write("\n")

            wf.write(str(float(row[4])-float(row[16])) + ",")
            wf.write(str(float(row[5])-float(row[17])) + ",")
            wf.write(str(float(row[4])-float(row[43])) + ",")
            wf.write(str(float(row[5])-float(row[44])) + ",")
            wf.write(str(float(row[43])-float(row[25])) + ",")
            wf.write(str(float(row[44])-float(row[26])) + ",")
            wf.write(str(float(row[43])-float(row[34])) + ",")
            wf.write(str(float(row[44])-float(row[35])) + "\n")
        
        wf.close()