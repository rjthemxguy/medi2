import os
from os import system
from colorama import Fore, Back, Style

class inputClass:
    def __init__(self):
        self.inputList = []

    def getInput(self):
        inputDirList = os.listdir('input')

        system("clear")
        print(Fore.YELLOW + "Please select the file wish to process")
        print()

        allowableKeys = []
        inputCount = 0
        for i in range(len(inputDirList)):
            if "csv" in inputDirList[i]:
                inputCount += 1
                allowableKeys.append(str(inputCount))
                self.inputList.append(inputDirList[i])
                print(Fore.WHITE + "[" + str(inputCount) + "] " + "- " + inputDirList[i])

        while True:
            x = int(input())
            if str(x) in allowableKeys:
                return self.inputList[x-1]

    def getCheck(self):
        inputDirList = os.listdir('scratch')

        system("clear")
        print(Fore.YELLOW + "Please select the file wish to process")
        print()

        allowableKeys = []
        inputCount = 0
        for i in range(len(inputDirList)):
            if "csv" in inputDirList[i]:
                inputCount += 1
                allowableKeys.append(str(inputCount))
                self.inputList.append(inputDirList[i])
                print(Fore.WHITE + "[" + str(inputCount) + "] " + "- " + inputDirList[i])

        while True:
            x = int(input())
            if str(x) in allowableKeys:
                return self.inputList[x - 1]

    def getFileType(self):
        system("clear")
        print(Fore.YELLOW + "Do you want to process an [E]xtract file or [C]heck file?")

        allowableKeys = ["e", "c"]
        while True:
            x = input()
            if x in allowableKeys:
                if x == "e":
                    return "Extract"
                if x == 'c':
                    return "Check"

