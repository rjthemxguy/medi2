import constants as con
import math
from os import system
from colorama import init
from colorama import Fore, Back, Style
import globals as g

import DBModule as db
import pandas as pd

init()


class claimClass:
    def __init__(self):
        self.rowList = []
        self.diagCodeList = []
        self.accession_number = 0
        self.assignedDiagCodes = []
        self.EMGList = []
        self.diagEntryList = []

    def doSummaryFile(self):

        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 12)
        pdf.set_x(0)
        pdf.set_y(g.pageRow)
        pdf.cell(5, 40, 'Claim Summary')
        pdf.output('tuto1.pdf', 'F')

    def loadPrices(self):
        database = db.database_class()

        for row in self.rowList:
            price = database.getPrice(str(row["CPT"]))

            try:
                row["PRICE"] = price
            except:
                pass

    def setMedicare(self):
        g.mode = "M"

    def getInsInfo(self, numofClaims, claimsProcessed):

        system("clear")
        print("Claim " + str(claimsProcessed) + " of " + str(numofClaims))
        print()
        print(Fore.GREEN + "Please select the correct Payer info for each claim\n")
        print(Fore.MAGENTA + "ACCESSION #: " + str(self.accession_number) + "\n")
        print(Fore.GREEN + "Patient: " + self.rowList[0]["PATIENT_FIRST"] + " " + self.rowList[0]["PATIENT_LAST"] + "\n")
        print(Fore.YELLOW + self.rowList[0]["INSURANCE_PLAN_NAME"])
        print()

        while True:
            print("Enter Payer ID below:")
            payerID = input()

            while True:
                print("Is this the correct payer ID: " + str(payerID))
                x = str(input())
                if x == "y":
                    break
                if x == "n":
                    break
            if x == "n":
                continue

            if x == "y":
                break

        for row in self.rowList:
            row["INSURANCE_PAYER_ID"] = payerID



    def setDaigCodes(self, numofClaims, claimsProcessed):

        EMGCount = 0
        pointerList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
        while True:

            for i in range(len(self.diagCodeList)):
                self.diagEntryList.append(i + 1)

            print(self.diagEntryList)

            for row in self.rowList:
                system("clear")
                print("Claim " + str(claimsProcessed) + " of " + str(numofClaims))
                print()
                print(Fore.GREEN + "Please select the correct Diagnostic Code for each EMG Code\n")
                print(Fore.MAGENTA + "ACCESSION #: " + str(self.accession_number) + "\n")
                print(Fore.GREEN + "Patient: " + row["PATIENT_FIRST"] + " " + row["PATIENT_LAST"] + "\n")
                print(Fore.YELLOW + "EMG Code: " + Fore.WHITE + str(row["EMG"]).ljust(8, " ") + "  " + Fore.BLUE + str(
                    EMGCount + 1) + " of " + str(len(self.rowList)) + "\n")

                for i in range(len(self.diagCodeList)):
                    print(Fore.BLUE + "[" + str(i + 1) + "] " + self.diagCodeList[i])

                while True:

                    try:
                        x = int(input())

                    except:
                        print("Please select a number in the list")
                        continue

                    if x in self.diagEntryList:
                        self.assignedDiagCodes.append(self.diagCodeList[x - 1])
                        self.EMGList.append(row["EMG"])
                        row["DIAG_POINTER"] = pointerList[x - 1]
                        break

                    else:
                        print("Select a number in the list")

                EMGCount += 1

                if EMGCount == len(self.rowList):
                    system("clear")
                    print(Fore.RED + "Please ensure the diagnosis codes matches the EMG codes for this claim \n")
                    print(Fore.MAGENTA + "ACCESSION #: " + str(self.accession_number) + "\n")
                    print(Fore.GREEN + "Patient: " + row["PATIENT_FIRST"] + " " + row["PATIENT_LAST"] + "\n")

                    for i in range(len(self.EMGList)):
                        print(Fore.BLUE + self.EMGList[i].ljust(10, " ") + " - " + self.assignedDiagCodes[i])

                    print("\n" + Fore.GREEN + "Press [Y] to accept or [R] to re-code")

            allowedKeys = ["Y", "y", "R", "r"]

            while True:
                x = input()
                if x in allowedKeys:
                    break
                else:
                    print("Please select [Y] or [R]")
                    continue

            if x == "y":
                break

            if x == "r":
                EMGCount = 0
                self.assignedDiagCodes = []
                self.EMGList = []
                self.diagEntryList = []
                continue

    def addRow(self, claimRow):

        rowDict = {
            "INSURANCE_PLAN_NAME": claimRow[con.INSURANCE_PLAN_NAME],
            "INSURANCE_STREET_ADDR": claimRow[con.INSURANCE_STREET_ADDR],
            "INSURANCE_CITY": claimRow[con.INSURANCE_CITY],
            "INSURANCE_STATE": claimRow[con.INSURANCE_STATE],
            "INSURANCE_ZIP": claimRow[con.INSURANCE_ZIP],
            "PLAN_GROUP_HEALTH_PLAN": claimRow[con.PLAN_GROUP_HEALTH_PLAN],
            "PATIENT_ID": claimRow[con.PATIENT_ID],
            "PATIENT_LAST": claimRow[con.PATIENT_LAST],
            "PATIENT_FIRST": claimRow[con.PATIENT_FIRST],
            "PATIENT_MID_INIT": claimRow[con.PATIENT_MID_INIT],
            "PATIENT_DOB": claimRow[con.PATIENT_DOB],
            "PATIENT_GENDER": claimRow[con.PATIENT_GENDER],
            "PATIENT_STREET_ADDR": claimRow[con.PATIENT_STREET_ADDR],
            "PATIENT_CITY": claimRow[con.PATIENT_CITY],
            "PATIENT_STATE": claimRow[con.PATIENT_STATE],
            "PATIENT_ZIP": claimRow[con.PATIENT_ZIP],
            "PATIENT_PHONE": claimRow[con.PATIENT_PHONE],
            "PATIENT_SIG_DATE": claimRow[con.PATIENT_SIG_DATE],
            "REFER_PHY_FIRST": claimRow[con.REFER_PHY_FIRST],
            "REFER_PHY_LAST": claimRow[con.REFER_PHY_LAST],
            "REFER_PHY_QUAL": claimRow[con.REFER_PHY_QUAL],
            "REFER_PHY_NPI": claimRow[con.REFER_PHY_NPI],
            "DIAG_1": claimRow[con.DIAG_1],
            "DIAG_2": claimRow[con.DIAG_2],
            "DIAG_3": claimRow[con.DIAG_3],
            "DIAG_4": claimRow[con.DIAG_4],
            "DIAG_5": claimRow[con.DIAG_5],
            "DIAG_6": claimRow[con.DIAG_6],
            "DIAG_7": claimRow[con.DIAG_7],
            "DIAG_8": claimRow[con.DIAG_8],
            "DIAG_9": claimRow[con.DIAG_9],
            "DIAG_10": claimRow[con.DIAG_10],
            "DIAG_11": claimRow[con.DIAG_11],
            "DIAG_12": claimRow[con.DIAG_12],
            "FROM_DATE_SERVICE": claimRow[con.FROM_DATE_SERVICE],
            "TO_DATE_SERVICE": claimRow[con.TO_DATE_SERVICE],
            "CPT": claimRow[con.CPT],
            "EMG": claimRow[con.EMG],
            "PRICE": "",
            "REFER_PHY_ID": claimRow[con.REFER_PHY_ID],
            "ACCESSION_NUMBER": claimRow[con.ACCESSION_NUMBER],
            "DIAG_POINTER": ""
        }


        self.rowList.append(rowDict)

        self.accession_number = claimRow[con.ACCESSION_NUMBER]

    def getPrices(self):
        pass

    def rowCount(self):
        return len(self.rowList)

    def getDiagCodes(self):
        if type(self.rowList[0]["DIAG_1"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_1"])
        if type(self.rowList[0]["DIAG_2"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_2"])
        if type(self.rowList[0]["DIAG_3"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_3"])
        if type(self.rowList[0]["DIAG_4"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_4"])
        if type(self.rowList[0]["DIAG_5"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_5"])
        if type(self.rowList[0]["DIAG_6"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_6"])
        if type(self.rowList[0]["DIAG_7"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_7"])
        if type(self.rowList[0]["DIAG_8"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_8"])
        if type(self.rowList[0]["DIAG_9"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_9"])
        if type(self.rowList[0]["DIAG_10"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_10"])
        if type(self.rowList[0]["DIAG_11"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_11"])
        if type(self.rowList[0]["DIAG_12"]) == str:
            self.diagCodeList.append(self.rowList[0]["DIAG_12"])

    def checkForLab(self, labCode):

        if labCode == "LP2":

            emgCount = 0

            for lp2_claim in self.rowList:

                if "LP" in lp2_claim.values():
                    emgCount += 1
                    LP = lp2_claim

                if "LDLD" in lp2_claim.values():
                    emgCount += 1
                    LDLD = lp2_claim

                if emgCount == 2:
                    lp2_claim.remove(LP)
                    LDLD["EMG"] = "LP2"
                    break

        if labCode == "LP":

            emgCount = 0
            listCount = 0

            for claim in self.rowList:

                # check for 3 tests that make up panel
                if "HDL" in claim.values():
                    emgCount += 1
                    HDL = claim

                if "CHOL" in claim.values():
                    emgCount += 1
                    CHOL = claim

                if "TRIG2" in claim.values():
                    emgCount += 1
                    TRIGclaim = claim

                if emgCount == 3:
                    TRIGclaim["EMG"] = "LP"
                    TRIGclaim["CPT"] = "80061"
                    self.rowList.remove(HDL)
                    self.rowList.remove(CHOL)
                    break

                listCount += 1
