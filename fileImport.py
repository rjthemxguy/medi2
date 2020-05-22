import csv
import globals as g
import pandas as pd
import DBModule as db



if g.mode == "I":
    import constants as con

else:
    import constantsMed as con

import os


class fileClass:
    def __init__(self):

        self.filePath = "input/"
        self.inputFileName = ""


    def __numIn(self, s):
        return any(i.isdigit() for i in s)

    def setPath(self, path):
        self.filePath = path

    def openInput(self, inputFileName):
        with open(self.filePath + inputFileName, 'r') as file:
            fileData = file.read()

            fileData = fileData.replace('"', '')

            with open('scratch/cleaned.csv', 'w') as file:
                file.write(fileData)

                file.close()

    def parseForMed(self, issue, fileName):
        with open('scratch/' + fileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed1.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if "PALMETTO" not in row[1]:
                        writer.writerow(row)

                result.close()

    def parseForBlankIns(self, issue, fileName):
        with open('scratch/parsed1.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed2.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if len(row[1]) == 0:
                        row[1] = "Insurance Info Missing"
                    writer.writerow(row)

                result.close()

    def parseForBadSubID(self, issue, fileName):
        with open('scratch/parsed2.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed3.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if self.__numIn(row[9]) == True:  # 15 for ins
                        writer.writerow(row)

                result.close()

    def parseForBadAddress(self, issue, fileName):
        with open('scratch/parsed3.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/parsed4.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    if "SUITE" in row[con.SUITE_FIX_1]:
                        row[con.SUITE_FIX_1 - 1] = row[con.SUITE_FIX_1 - 1] + row[con.SUITE_FIX_1]
                        del row[con.SUITE_FIX_1]

                    writer.writerow(row)
                result.close()

    def parseForRan(self, _accession):
        database = db.database_class()

        with open('scratch/parsed4.csv', 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/addressFixed.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:
                    #if database.didRun(row[con.ACCESSION_NUMBER])  == False:
                    writer.writerow(row)
                   # else:
                   #     print("Accession " + row[con.ACCESSION_NUMBER] + " Ran")




    def fixAddress(self, fileName):

        with open('scratch/' + fileName, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            with open('scratch/addressFixed.csv', "w", newline='') as result:
                writer = csv.writer(result)

                for row in csvreader:

                    if self.__numIn(row[con.NUM_FIX_1]) == True:
                        row[con.NUM_FIX_1 - 1] = row[con.NUM_FIX_1 - 1] + row[con.NUM_FIX_1]
                        del row[con.NUM_FIX_1]

                    if self.__numIn(row[con.NUM_FIX_2]) == True:
                        row[con.NUM_FIX_2 - 1] = row[con.NUM_FIX_2 - 1] + row[con.NUM_FIX_2]
                        del row[con.NUM_FIX_2]

                    if self.__numIn(row[con.NUM_FIX_3]) == True:
                        row[con.NUM_FIX_3 - 1] = row[con.NUM_FIX_3 - 1] + row[con.NUM_FIX_3]
                        del row[con.NUM_FIX_3]

                    if "SUITE" in row[con.SUITE_FIX_1]:  #335 for ins
                        row[con.SUITE_FIX_1 - 1] = row[con.SUITE_FIX_1 - 1] + row[con.SUITE_FIX_1]
                        del row[con.SUITE_FIX_1]

                    if "SUITE" in row[con.SUITE_FIX_2]:
                        row[con.SUITE_FIX_2 - 1] = row[con.SUITE_FIX_2 - 1] + row[con.SUITE_FIX_2]
                        del row[con.SUITE_FIX_2]

                    if "MD" in row[con.MD_FIX]:
                        del row[con.MD_FIX]

                    if "MD" in row[con.MD_FIX2]:
                        del row[con.MD_FIX2]

                    writer.writerow(row)

                result.close()

    def get(self):

        try:
            self.dataset = pd.read_csv("scratch/addressFixed.csv", header=None)
            return (self.dataset)

        except:
            print("There is no Accessions number to run")
            exit(10)


