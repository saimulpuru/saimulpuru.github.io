import random
shelfUnit = 1
openTagGeometrybox = '<a-box '
openTagGeometryPlane = '<a-plane '
widthTag = ' width = "' # x axis
depthTag = ' depth = "' # y axis
heightTag = ' height = "' # z axis
endProperty = '"'
positionTag = ' position = "'
rotationTag = ' rotation = "'
colorTag = ' color = "'
materialTag =  ' material="side: double"'
endBrac = '>'
endBoxTag = '</a-box>'
endPlaneTag = '</a-plane>'
shelfSpace = 3

def rectangle(x, z, y, width, depth):
    outputString = '<a-entity geometry = "primitive: box; width: ' +  str((width*shelfUnit)) + '; depth: ' + str((depth*shelfUnit)) + '; height: 0.025" position = "' + str(x) + ' ' + str(y) + ' ' + str(z) + '"></a-entity>'
    return outputString

def shelf(PosX, PosZ, PosY, width, depth, height):
    outputstring = ''
    outputstring += openTagGeometryPlane 
    outputstring += positionTag + str(PosX) + ' ' + str(PosZ+(height/2)) + ' ' + str(PosY) + endProperty
    outputstring += widthTag + str(width) + endProperty + heightTag + str(height) + endProperty
    outputstring += colorTag + "#00FFFF" + endProperty
    outputstring += materialTag
    outputstring += endBrac
    
    outputstring += openTagGeometryPlane 
    outputstring += positionTag + str(0) + ' ' + str(0) + ' ' + str(depth) + endProperty
    outputstring += widthTag + str(width) + endProperty + heightTag + str(height) + endProperty
    outputstring += materialTag
    outputstring += colorTag + "#778899" + endProperty
    outputstring += endBrac
    outputstring += endPlaneTag
    
    
    for i in range(int(height/-2)+1, int(height/2)+1, 1):
        outputstring += openTagGeometryPlane 
        outputstring += positionTag + str(0) + ' ' + str(i) + ' ' + str(4) + endProperty
        outputstring += widthTag + str(width) + endProperty + heightTag + str(depth) + endProperty
        outputstring += materialTag
        outputstring += colorTag + "#778899" + endProperty
        outputstring += rotationTag + "-90 0 0" + endProperty
        outputstring += endBrac
        outputstring += endPlaneTag
        
    outputstring += endPlaneTag    
    return outputstring



def warehouse(rows, colums, shelfX, shelfZ, shelfY):
    outputString = ""
    totalX = rows*shelfX + shelfSpace*rows + shelfSpace
    totalY = colums*shelfY + shelfSpace*colums + shelfSpace
    
    for m in range (int(totalX/-2), int(totalX/2), shelfX+shelfSpace):
        for n in range (int(totalY/-2), int(totalY/2), shelfY+(shelfSpace*2)):
            outputString += shelf(m, 0, n, shelfX, shelfZ, shelfY )
    print(totalX, totalY)        
    return outputString

a = warehouse(4, 4, 2, 8, 6)

f = open("myfile.txt", "w")
f.write(a)
f.close()
    
    



    
    
    

