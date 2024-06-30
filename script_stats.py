from PyPDF2 import PdfReader
import PySimpleGUI as sg

reader = PdfReader("hamlet.pdf")

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

print(pageLineArray)

for pageLine in pageLineArray:
    for index, line in enumerate(pageLine):
        if line in characterDict:
            nextLine = (pageLine[index+1])
            splitLine = nextLine.split(" ")
            lineLength = len(splitLine)
            characterDict[line] += lineLength

print(characterDict)
