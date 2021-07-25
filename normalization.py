import csv

list = [1, 8, 13, 17]

dates = ["2021-07-23-15-03-49", "2021-07-23-15-04-08", "2021-07-23-15-04-27", "2021-07-23-15-04-58"]

for date in dates:
    fname = date + "_people_"

    for i in list:
        file = open("./" + fname + str(i) + ".csv", "r")
        rf = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        wf = open("./" + fname + str(i) + "_normal.csv", "w")
        wf.write("time,HEAD_x,HEAD_y,HEAD_z,NECK_x,NECK_y,NECK_z,RIGHT_SHOULDER_x,RIGHT_SHOULDER_y,RIGHT_SHOULDER_z,RIGHT_ELBOW_x,RIGHT_ELBOW_y,RIGHT_ELBOW_z,RIGHT_WRIST_x,RIGHT_WRIST_y,RIGHT_WRIST_z,LEFT_SHOULDER_x,LEFT_SHOULDER_y,LEFT_SHOULDER_z,LEFT_ELBOW_x,LEFT_ELBOW_y,LEFT_ELBOW_z,LEFT_WRIST_x,LEFT_WRIST_y,LEFT_WRIST_z,RIGHT_HIP_x,RIGHT_HIP_y,RIGHT_HIP_z,RIGHT_KNEE_x,RIGHT_KNEE_y,RIGHT_KNEE_z,RIGHT_ANKLE_x,RIGHT_ANKLE_y,RIGHT_ANKLE_z,LEFT_HIP_x,LEFT_HIP_y,LEFT_HIP_z,LEFT_KNEE_x,LEFT_KNEE_y,LEFT_KNEE_z,LEFT_ANKLE_x,LEFT_ANKLE_y,LEFT_ANKLE_z,CHEST_x,CHEST_y,CHEST_z\n")
        header = next(rf)
        
        for row in rf:
            for i in range(len(row)):
                if(i == 0):
                    wf.write(row[i])
                    wf.write(",")
                elif(int(i%3 == 1)):
                    wf.write(str(float(row[i])-float(row[43])))
                    wf.write(",")
                elif(int(i%3 == 2)):
                    wf.write(str(float(row[i])-float(row[44])))
                    wf.write(",")
                else:
                    wf.write(str(float(row[i])-float(row[45])))
                    if i != len(row)-1:
                        wf.write(",")
                    else:
                        wf.write("\n")
        wf.close()