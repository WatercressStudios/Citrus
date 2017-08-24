print('Please enter the file to be parsed. Include the file path.')
inputFilePath = input()

inputFileName = inputFilePath.rsplit('\\', 1)[1]
filePath = inputFilePath.rsplit('\\', 1)[0]

outputFileName = '\\parsed_' + inputFileName
outputFilePath = filePath + outputFileName

print('Please enter the scene\'s route tag.')
routeTag = input()

print('Please enter the scene number.')
sceneNumber = input()

lineCount = 1

with open(inputFilePath, 'r') as infile, open(outputFilePath, 'w') as outfile:
    for line in infile:
        if 'clm' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Clementine\n')
            outfile.write(line)
            lineCount += 1
        elif 'lem' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Lemon\n')
            outfile.write(line)
            lineCount += 1
        elif 'lim' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Lime\n')
            outfile.write(line)
            lineCount += 1
        elif 'rby' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Ruby\n')
            outfile.write(line)
            lineCount += 1
        elif 'cap' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Track Captain\n')
            outfile.write(line)
            lineCount += 1
        elif 'bkr' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Baker\n')
            outfile.write(line)
            lineCount += 1
        elif 'tch' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" Teacher\n')
            outfile.write(line)
            lineCount += 1
        elif 'bnd' in line[:3]:
            outfile.write('voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Lime\'s Band Member\n')
            outfile.write(line)
            lineCount += 1
        else:
            outfile.write(line)

print('Scene has been successfully parsed! Output location: ')
print(outputFilePath)
