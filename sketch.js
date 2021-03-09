
var canvas;
var generate = true;
var render = false;

var shelfx = 5
var shelfy = 2;
var shelfz = 10;

var Rows = 4;
var Cols = 6

var Width = window.innerWidth;
var Height = window.innerHeight;
var roomWidth = 0.9*Width;
var roomHeight = 0.9*Height;

var section1 = [shelfx, shelfy, shelfz, Cols, Rows];


function setup(){
	canvas = createCanvas(windowWidth, windowHeight);
	canvas.style("display", "block");
    canvas.parent('output');
}


function draw(){
    
    if (generate){
        render = true;
    }
    
    if (render){
        background('black');
        var horizontalLength = 0;
        for (var i = 0; i < section1[3]; i++){
            for (var j = 0; j < section1[0]; j++){
                horizontalLength += 0.5;
            }
            horizontalLength += 1;
        }
        horizontalLength += 1;
        
        var verticalLength = 0;
        for (var m = 0; m < section1[4]; m++){
            for (var n = 0; n < section1[1]; n++){
                verticalLength += 0.5;
            }
            verticalLength += 1;
        }
        verticalLength += 5;
        
        console.log(horizontalLength, verticalLength);
        
        var unit = roomHeight/horizontalLength;
        
        var posx = (canvas.width - (horizontalLength*unit))/2;
        var posy = (canvas.height - ((verticalLength-2)*unit))/2;
        
        // outline of floorplan
        noFill();
        stroke('white');
        rect(posx, posy, horizontalLength*unit, (verticalLength-2)*unit);
        
        // shelves
        for (var p = 0; p < section1[3]; p++) {
            for (var q = 0; q < section1[4]; q++){
                stroke('lightgreen');
                rect ((posx+unit) + p*((0.5*unit*section1[0]) + unit), (posy+(2*unit)) + q*((0.5*unit*section1[1]) + unit), unit*0.5*section1[0], unit*0.5*section1[1]);
            }
        }
        
        //calculating number of loading and unloading bays
        
        bayW = 6;
        bayH = 1;
        
        
        var numBays = 0;
        
        for (var b = 0; b < horizontalLength-2; b+= 4){
            numBays += 1;
        }
        
        var bayPosX = (canvas.width - (numBays*3.5*unit))/2
        
        for (var c = 0; c < numBays; c++){
            stroke('red');
            rect(bayPosX+(3.5*unit*c), posy, bayW*unit*0.5, bayH*unit*0.5);
            stroke('yellow');
            rect(bayPosX+(3.5*unit*c), posy + ((verticalLength-2.5)*unit), bayW*unit*0.5, bayH*unit*0.5);
        }
    }
    
    
    
    
    
    

}






