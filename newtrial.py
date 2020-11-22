import os, arcpy
import json

# home = r"C:\EsriTraining\county change\County Change.gdb"
home = r"C:\Users\Safal Acharya\Documents\ArcGIS\Projects\New Trial\New Trial.gdb"

arcpy.env.workspace = home



def create_timestamps(counter):
    minTime =0
    maxTime = 1800
    skipTime = maxTime/counter
    # print(r'"timestamps" : [ ')
    printText = '"timestamps" : [ '
    while minTime < maxTime+1:
        # print(minTime)
        printText = printText + str(minTime)
        if (maxTime-minTime) < 0.0025:
            printText += ']'
        else:
            printText += ', '
        minTime += skipTime
    # print(printText)
    return printText
#

initbrac = False
with arcpy.da.SearchCursor("Change_Map_Project", ['NAME', 'SHAPE@', 'START_DATE', 'END_DATE']) as cursor:
    print(cursor.fields)
    for row in cursor:
        totalcheck = 0
        print(row[0] + row[2].strftime("%Y") + row[3].strftime("%Y"))
        hello = row[0] + row[2].strftime("%Y") + row[3].strftime("%Y") + ".txt"
        world = "Trial Json" + ".json"
        directory = "C:/EsriTraining/county change/Text/" + hello
        directory1 = "C:/EsriTraining/county change/Text/" + world
        file1 = open(directory, "a")
        file2 = open(directory1, "a")
        if initbrac == False:
            file2.write('[')
            initbrac = True

        # print(" File {} created". format(directory))
        if row[0]:
            num = 0
            for part in row[1]:
                # Print the part number
                # print("Part {}:".format(num))
                # file1.write("Part {}:".format(num))
                # Step through each vertex in the feature
                counter = 0
                # file2.write('{ "vendor":0, "path": [')
                boolvalue = True
                print (row[3])
                for pnt in part:
                    print(pnt)
                    if pnt:

                        # Print x,y coordinates of current point
                        print("{}, {}".format(pnt.X, pnt.Y))

                        file1.write("[{}, {}],".format(pnt.X, pnt.Y))
                        file1.write("\n")
                        file2.write("[{}, {}],".format(pnt.X, pnt.Y))
                        file2.write("\n")
                        counter += 1
                    else:
                        # If pnt is None, this represents an interior ring
                        # print("Interior Ring:")
                        pass
                num += 1
            print(directory + " : "+str(counter))
            file2.write('')
            buffer = create_timestamps(counter)
            file1.write(buffer)
            file2.write(buffer)
            totalcheck += 1

            print("Total numbers : {}". format(num))







