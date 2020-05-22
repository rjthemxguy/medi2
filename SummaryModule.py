import DBModule as db

class summaryClass:




    def __init__(self):

        from fpdf import FPDF
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(False)
        self.currentRow = 0
        self.claimCount = 1
        self.database = db.database_class()


    def writeClaim(self, claim, diagCodes):


        self.database.insertAccession(claim.rowList[0]["ACCESSION_NUMBER"])

        self.pdf.set_font('Arial', '', 8)
        self.pdf.set_xy(5, self.currentRow)
        self.pdf.line(5, self.currentRow, 280, self.currentRow)
        self.currentRow += 2
        self.pdf.set_xy(5, self.currentRow)
        self.pdf.cell(5, 4, "[" + str(self.claimCount) + "]")
        self.pdf.set_xy(12, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["ACCESSION_NUMBER"]))
        self.pdf.set_xy(38, self.currentRow)
        #self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_PAYER_ID"]))
        self.pdf.set_xy(70, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_LAST"]))
        self.pdf.set_xy(88, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_FIRST"]))
        self.pdf.set_xy(110, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_DOB"]))
        self.pdf.set_xy(132, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_GENDER"]))
        self.pdf.set_xy(145, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["REFER_PHY_FIRST"]))
        self.pdf.set_xy(160, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["REFER_PHY_LAST"]))
        self.pdf.set_xy(190, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["REFER_PHY_NPI"]))
        self.pdf.set_xy(220, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_PLAN_NAME"]))

        self.currentRow += 5
        self.pdf.set_xy(70, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_STREET_ADDR"]))
        self.pdf.set_xy(220, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_STREET_ADDR"]))
        self.currentRow += 5
        self.pdf.set_xy(70, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_CITY"]))
        self.pdf.set_xy(105, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_STATE"]))
        self.pdf.set_xy(110, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["PATIENT_ZIP"]))
        self.pdf.set_xy(220, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_CITY"]))
        self.pdf.set_xy(250, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_STATE"]))
        self.pdf.set_xy(258, self.currentRow)
        self.pdf.cell(5, 4, str(claim.rowList[0]["INSURANCE_ZIP"]))




        self.currentRow += 5
        self.pdf.line(5,self.currentRow, 280, self.currentRow)
        self.currentRow += 2

        self.pdf.set_xy(15, self.currentRow)
        self.pdf.cell(5, 4, "Diagnosis Codes:")


        xPos = 40
        for i in range(len(diagCodes)):
            self.pdf.set_xy(xPos, self.currentRow)
            self.pdf.cell(5, 4, diagCodes[i])
            xPos += 15

        self.currentRow += 5
        self.pdf.set_xy(15, self.currentRow)
        self.pdf.cell(5, 4, "CPT Code")

        self.pdf.set_xy(35, self.currentRow)
        self.pdf.cell(5, 4, "EMG Code")

        self.pdf.set_xy(55, self.currentRow)
        self.pdf.cell(5, 4, "Price")


        self.currentRow += 5
        self.pdf.line(5, self.currentRow, 280, self.currentRow)
        self.currentRow += 3


        for row in claim.rowList:
            self.pdf.set_xy(15, self.currentRow)
            self.pdf.cell(5, 4, str(row["CPT"]))
            self.pdf.set_xy(35, self.currentRow)
            self.pdf.cell(5, 4, str(row["EMG"]))
            self.pdf.set_xy(55, self.currentRow)
            self.pdf.cell(5, 4, str(row["PRICE"]))

            self.currentRow += 5

            if self.pdf.get_y() > 155:

                self.pdf.add_page("L")
                self.pdf.set_xy(5, 10)
                self.currentRow = 5



        self.currentRow += 10
        self.claimCount += 1





    def writeMast(self):

        self.pdf.add_page("L")
        self.pdf.set_font('Arial', 'B', 10)
        self.pdf.set_xy(5,0)
        self.pdf.cell(5, 10, 'Claim Summary - ')
        self.pdf.set_xy(12, self.currentRow + 10)
        self.pdf.set_font('Arial', '', 8)
        self.pdf.cell(5, 4, "Accession #")
        self.pdf.set_xy(38, self.currentRow + 10)
        self.pdf.cell(5, 4, "Sub ID")
        self.pdf.set_xy(70, self.currentRow + 10)
        self.pdf.cell(5, 4, "Pat. Last")
        self.pdf.set_xy(88, self.currentRow + 10)
        self.pdf.cell(5, 4, "Pat. First")
        self.pdf.set_xy(110, self.currentRow + 10)
        self.pdf.cell(5, 4, "DOB")
        self.pdf.set_xy(132, self.currentRow + 10)
        self.pdf.cell(5, 4, "Gender")
        self.pdf.set_xy(145, self.currentRow + 10)
        self.pdf.cell(5, 4, "Ref Phy")
        self.pdf.set_xy(190, self.currentRow + 10)
        self.pdf.cell(5, 4, "Ref Phy NPI")
        self.pdf.set_xy(220, self.currentRow + 10)
        self.pdf.cell(5, 4, "Insurance")
        self.currentRow = 20
        self.pdf.set_font('Arial', '', 10)


    def writePDF(self):
        self.pdf.output('claimSummary.pdf', 'F')