from PyPDF2 import PdfReader
import PySimpleGUI as sg

reader = PdfReader("hamlet 2.pdf")

length = (len(reader.pages)) 

pageArray = []
pageLineArray = []
lineArray = []

i = 0

characters = ["CLAUDIUS","HAMLET","POLONIUS","HORATIO"]
characterDict = {
    "CLAUDIUS": 0,
    "HAMLET": 0,
    "POLONIUS": 0,
    "HORATIO": 0,
    "BERNARDO": 0,
    "FRANCISCO": 0,


}
startPage = 3
endPage = 5


while (i < length):

    pageArray.append(reader.pages[i].extract_text())
    i += 1

for page in pageArray:
    pageLine = page.split("\n")
    pageLineArray.append(pageLine)

for pageLine in pageLineArray:
    for index, line in enumerate(pageLine):
        if line in characterDict:
            splitLine = line.split(" ")
            lineLength = len(splitLine)
            print(pageLine[index+1])
            characterDict[line] += lineLength

print (characterDict)
