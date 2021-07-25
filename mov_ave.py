import csv

list = [8, 13, 17]

dates = ["2021-07-23-15-03-49", "2021-07-23-15-04-08", "2021-07-23-15-04-27", "2021-07-23-15-04-58"]

for date in dates:
    fname = date + "_people_"

    for i in list:
        file = open("./" + fname + str(i) + "_diff.csv", "r")
        rf = csv.reader(file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        rf = [row for row in rf]
        wf = open("./" + fname + str(i) + "_diff_m_ave.csv", "w")
        wf.write("HEAD_x,HEAD_y,NECK_x,NECK_y,RIGHT_SHOULDER_x,RIGHT_SHOULDER_y,RIGHT_ELBOW_x,RIGHT_ELBOW_y,RIGHT_WRIST_x,RIGHT_WRIST_y,LEFT_SHOULDER_x,LEFT_SHOULDER_y,LEFT_ELBOW_x,LEFT_ELBOW_y,LEFT_WRIST_x,LEFT_WRIST_y,RIGHT_HIP_x,RIGHT_HIP_y,RIGHT_KNEE_x,RIGHT_KNEE_y,RIGHT_ANKLE_x,RIGHT_ANKLE_y,LEFT_HIP_x,LEFT_HIP_y,LEFT_KNEE_x,LEFT_KNEE_y,LEFT_ANKLE_x,LEFT_ANKLE_y,CHEST_x,CHEST_y\n")
        for itr in range(len(rf)-5):
            if itr == 0:
                continue
            for n_row in range(30):
                sum = 0.0
                for i in range(5):
                    sum += float(rf[itr+i][n_row])
                wf.write(str(sum/5.0))
                if n_row != 29:
                    wf.write(",")
                else:
                    wf.write("\n")
        wf.close()