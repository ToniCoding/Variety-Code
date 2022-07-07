import os
from datetime import datetime, date
from pathlib import Path

Path('result.txt').touch()
running = True
uName = os.getlogin()
nowDate = date.today()
nowT = datetime.now()
nowTime = nowT.strftime('%H:%M:%S')
openFile = open(f"C:\\Users\\{uName}\\AppData\\Roaming\\.minecraft\\logs\\latest.log")
newLogFile = open('./result.txt', "r+")
readLine = openFile.readlines()
lineNumb = 0
timePlayedRange = range(0,5000)

def fileRead(lineNumb, nowDate, nowTime):
    alreadyRead = 1
    try:
        uFilter = input('Which dimension you want to filter (world, nether, end, exit(ends the program)): ').lower()
    except KeyboardInterrupt:
        print('Exception: Keyboard Interrupt')
    validAnswers = ('world', 'nether', 'end', 'exit')
    if uFilter not in validAnswers:
        return fileRead(lineNumb, nowDate, nowTime)
    if uFilter == 'world':
        uFilter = 'world:'
    if uFilter == 'nether':
        uFilter = 'world_nether:'
    if uFilter == 'end':
        uFilter = 'world_the_end:'
    if uFilter == 'exit':
        newLogFile.write('\n>>> User requested program exit.\n')
        exit()
    newLogFile.write(f'>>> Registry date: {nowDate}, {nowTime}\n\n')
    if alreadyRead == 1:
        newLogFile.write(f'Filtered by: "{uFilter}"\n')
        for lineRead in readLine:
            lineNumb += 1
            if '[Render thread/INFO]: [CHAT]  = ' in lineRead:
                print(f'End detected at line: {lineNumb}.')
                alreadyRead += 1
                print(alreadyRead)
                break
            for eachPtr in lineRead:
                storagePrts = lineRead
                croppedStr = storagePrts[40:]
                if croppedStr.startswith(uFilter):
                    newLogFile.write(f'{croppedStr.strip()}\n')
                break

while running == True:
    fileRead(lineNumb, nowDate, nowTime)