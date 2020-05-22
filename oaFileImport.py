import pandas as pd




class oaFileClass:
    def __init__(self):
        self.rowIndex = 0
        self.testIndex = 0
        self.rowTotal = 0

        self.oaTemplate = pd.read_csv("template/OATemplate.csv", header=0)

    def _writeHeader(self, _claim, _diagCodeList):
        self.oaTemplate.at[self.rowIndex, "InsurancePlanName"] = _claim[0]["INSURANCE_PLAN_NAME"]
        self.oaTemplate.at[self.rowIndex, "InsurancePayerID"] = " "
        self.oaTemplate.at[self.rowIndex, "InsuranceStreetAddr"] = _claim[0]["INSURANCE_STREET_ADDR"]
        self.oaTemplate.at[self.rowIndex, "InsuranceCity"] = _claim[0]["INSURANCE_CITY"]
        self.oaTemplate.at[self.rowIndex, "InsuranceState"] = _claim[0]["INSURANCE_STATE"]
        self.oaTemplate.at[self.rowIndex, "InsuranceZip"] = _claim[0]["INSURANCE_ZIP"]
        self.oaTemplate.at[self.rowIndex, "InsuranceCityStateZip"] = str(_claim[0]["INSURANCE_CITY"]) + " " + str(_claim[0]["INSURANCE_STATE"]) + " " + str(_claim[0]["INSURANCE_ZIP"])
        self.oaTemplate.at[self.rowIndex, "PlanGroupHealthPlan"] = "1"
        self.oaTemplate.at[self.rowIndex, "PatientID"] = _claim[0]["PATIENT_ID"]
        self.oaTemplate.at[self.rowIndex, "PatientLast"] = _claim[0]["PATIENT_LAST"]
        self.oaTemplate.at[self.rowIndex, "InsuredLast"] = _claim[0]["PATIENT_LAST"]
        self.oaTemplate.at[self.rowIndex, "PatientFirst"] = _claim[0]["PATIENT_FIRST"]
        self.oaTemplate.at[self.rowIndex, "InsuredFirst"] = _claim[0]["PATIENT_FIRST"]
        self.oaTemplate.at[self.rowIndex, "PatientMidInit"] = _claim[0]["PATIENT_MID_INIT"]
        self.oaTemplate.at[self.rowIndex, "InsuredMidInit"] = _claim[0]["PATIENT_MID_INIT"]
        self.oaTemplate.at[self.rowIndex, "PatientDOB"] = _claim[0]["PATIENT_DOB"]
        self.oaTemplate.at[self.rowIndex, "PatientStreetAddress"] = _claim[0]["PATIENT_STREET_ADDR"]
        self.oaTemplate.at[self.rowIndex, "PatientCity"] = _claim[0]["PATIENT_CITY"]
        self.oaTemplate.at[self.rowIndex, "PatientState"] = _claim[0]["PATIENT_STATE"]
        self.oaTemplate.at[self.rowIndex, "PatientZip"] = _claim[0]["PATIENT_ZIP"]
        self.oaTemplate.at[self.rowIndex, "PatientPhone"] = _claim[0]["PATIENT_ZIP"]
        self.oaTemplate.at[self.rowIndex, "PatientRelationSELF"] = 1
        self.oaTemplate.at[self.rowIndex, "PatientSignature"] = "Signature on file"
        self.oaTemplate.at[self.rowIndex, "PatientSignatureDate"] = _claim[0]["TO_DATE_SERVICE"]
        self.oaTemplate.at[self.rowIndex, "InsuredSignature"] = "Signature on File "
        try:
            self.oaTemplate.at[self.rowIndex, "ReferringPhysician"] = _claim[0]["REFER_PHY_FIRST"] + " " + _claim[0]["REFER_PHY_LAST"]
        except:
            print("Error in Phy Names")
        self.oaTemplate.at[self.rowIndex, "ReferPhysQualifier"] = _claim[0]["REFER_PHY_QUAL"]
        self.oaTemplate.at[self.rowIndex, "Refer_Phys_NPI"] = _claim[0]["REFER_PHY_NPI"]
        self.oaTemplate.at[self.rowIndex, "PhysicianSignature"] = "Signature on File"
        self.oaTemplate.at[self.rowIndex, "PhysicianSignatureDate"] = _claim[0]["TO_DATE_SERVICE"]
        self.oaTemplate.at[self.rowIndex, "PhysicianLast"] = "Prime Clinical"
        self.oaTemplate.at[self.rowIndex, "PhysicianFirst"] = "Lab"
        self.oaTemplate.at[self.rowIndex, "FacilityName"] = "Prime Clinical Lab"
        self.oaTemplate.at[self.rowIndex, "FacilityStreetAddr"] = "27825 Fremont Ct"
        self.oaTemplate.at[self.rowIndex, "FacilityCity"] = "Velencia"
        self.oaTemplate.at[self.rowIndex, "FacilityState"] = "CA"
        self.oaTemplate.at[self.rowIndex, "FacilityZip"] = "91355"
        self.oaTemplate.at[self.rowIndex, "FacilityCityStateZip"] = "Valencia CA 91355"
        self.oaTemplate.at[self.rowIndex, "FacilityNPI"] = "1871038778"
        self.oaTemplate.at[self.rowIndex, "SupplierName"] = "Prime Clinical Lab"
        self.oaTemplate.at[self.rowIndex, "SupplierStreetAddr"] = "27825 Fremont Ct"
        self.oaTemplate.at[self.rowIndex, "SupplierCity"] = "Velencia"
        self.oaTemplate.at[self.rowIndex, "SupplierState"] = "CA"
        self.oaTemplate.at[self.rowIndex, "SupplierZip"] = "91355"
        self.oaTemplate.at[self.rowIndex, "SupplierCityStateZip"] = "Valencia CA 91355"
        self.oaTemplate.at[self.rowIndex, "SupplierNPI"] = "1871038778"
        self.oaTemplate.at[self.rowIndex, "SupplierPhone"] = "(661) 253-1173"
        self.oaTemplate.at[self.rowIndex, "AcceptAssignYes"] = "1"
        self.oaTemplate.at[self.rowIndex, "TaxID"] = "81-3301345"
        #self.oaTemplate.at[self.rowIndex, "Session"] = _claim[0]["ACCESSION_NUMBER"]



        for i in range(len(_diagCodeList)):
            self.oaTemplate.at[self.rowIndex, "DiagCode" + str(i + 1)] = _diagCodeList[i]

        self.setGender(_claim)

    def setGender(self, _claim):
        if _claim[0]["PATIENT_GENDER"] == "F":
            self.oaTemplate.at[self.rowIndex, "PatientFemale"] = 1
            self.oaTemplate.at[self.rowIndex, "PatientMale"] = ""

        else:
            self.oaTemplate.at[self.rowIndex, "PatientFemale"] = ""
            self.oaTemplate.at[self.rowIndex, "PatientMale"] = 1


    def writeTestBlock(self, _claim, _diagCodeList):
        self._writeHeader(_claim, _diagCodeList)

        self.rowTotal = 0
        self.testIndex = 0
        self.totalRowsProcessed = 0
        for i in range(len(_claim)):


            self.testIndex += 1
            self.oaTemplate.at[self.rowIndex, "CPT" + str(self.testIndex)] = _claim[i]["CPT"]
            self.oaTemplate.at[self.rowIndex, "EMG" + str(self.testIndex)] = _claim[i]["EMG"]
            self.oaTemplate.at[self.rowIndex, "Charges" + str(self.testIndex)] = _claim[i]["PRICE"]
            self.oaTemplate.at[self.rowIndex, "Units" + str(self.testIndex)] = "1"
            self.oaTemplate.at[self.rowIndex, "ToDateOfService" + str(self.testIndex)] = _claim[i]["TO_DATE_SERVICE"]
            self.oaTemplate.at[self.rowIndex, "FromDateOfService" + str(self.testIndex)] = _claim[i]["FROM_DATE_SERVICE"]
            self.oaTemplate.at[self.rowIndex, "PlaceOfService" + str(self.testIndex)] = "11"
            self.oaTemplate.at[self.rowIndex, "RenderingPhysQualifier" + str(self.testIndex)] = "MD"
            self.oaTemplate.at[self.rowIndex, "RenderingPhysID" + str(self.testIndex)] = _claim[i]["REFER_PHY_ID"]
            self.oaTemplate.at[self.rowIndex, "RenderingPhysNPI" + str(self.testIndex)] = _claim[i]["REFER_PHY_NPI"]
            self.oaTemplate.at[self.rowIndex, "DiagCodePointer" + str(self.testIndex)] = _claim[i]["DIAG_POINTER"]

            self.rowTotal = self.rowTotal + int(_claim[i]["PRICE"])
            print(_claim[i]["PRICE"])
            self.totalRowsProcessed += 1

            if self.testIndex == 6 and self.totalRowsProcessed != len(_claim):
                self.oaTemplate.at[self.rowIndex, "TotalCharges"] = self.rowTotal
                self.oaTemplate.at[self.rowIndex, "BalanceDue"] = self.rowTotal
                self.rowIndex += 1
                self._writeHeader(_claim, _diagCodeList)
                self.rowTotal = 0
                self.testIndex = 0

            if self.totalRowsProcessed == len(_claim):
                break




        self.oaTemplate.at[self.rowIndex, "TotalCharges"] = self.rowTotal
        self.oaTemplate.at[self.rowIndex, "BalanceDue"] = self.rowTotal
        self.rowTotal = 0
        self.rowIndex += 1



    def closeOAFile(self):
        self.oaTemplate.to_csv("scratch/oaClaims.csv", header=False, index=False)

        with open('scratch/oaClaims.csv', 'r') as tabFile:
            tabFiledata = tabFile.read()

            tabFiledata = tabFiledata.replace(',', '\t')

        with open('output/tabClaims.txt', 'w') as tabFile:
            tabFile.write(tabFiledata)



