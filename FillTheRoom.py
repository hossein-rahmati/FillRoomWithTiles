def compare(width, length):
    if width > length:
        width, length = length, width
    return width, length


def getRoomSize():
    width = int(input("enter width of room: "))
    length = int(input("enter length of room: "))
    width, length = compare(width, length)
    return width, length


def printResult(tiles):
    tiles.sort()
    for i in range(len(tiles)):
        tile = 2**i
        if tiles.count(tile) != 0:
            print(f"{tiles.count(tile)}  {tile}*{tile} tiles")


def calcTiles(tempWidth, tempLength, tiles):
    while tempLength > 0:
        isWidthChanged = False
        setWidth = 0
        for i in range(tempWidth // 2, -1, -1):
            tileSize = 2**i
            if tempWidth >= tileSize and tempLength >= tileSize:
                square = 2**i
                widthOutOfPartition = tempWidth // square
                lengthOutOfPartition = tempLength // square

                outPartition = widthOutOfPartition * lengthOutOfPartition

                for i in range(outPartition):
                    tiles.append(square)

                if isWidthChanged == False:
                    tempWidth = square
                    setWidth = square
                    isWidthChanged = True

                if tempLength >= outPartition * square:
                    tempLength -= outPartition * square
                else:
                    tempLength -= square
    return tempWidth, tempLength, setWidth


def main():
    width, length = getRoomSize()

    tiles = []
    tempWidth = width
    lastRowLength = length
    tempLength = length

    while width > 1:
        tempWidth, tempLength, setWidth = calcTiles(tempWidth, tempLength, tiles)
        tempLength = length
        width -= setWidth
        tempWidth = width

    if width != 0:
        for i in range(lastRowLength):
            tiles.append(1)

    printResult(tiles)


main()
