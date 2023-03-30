#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if(isNaN(x)){
        console.log("missing size");
} else {
    for(let n = 0; n < x; n++){
            //for(let m = 0; m < n; m++)
            console.log("X".repeat(x));
             
             //console.log("\n");
        
    }
}
