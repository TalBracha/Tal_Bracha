 let txt = "Open To Work" ;
 let i = 0;
 let speed = 4500;
 function OpenToWork() {
      if ( i < 12) {
      document.getElementById("open").innerHTML += txt.substring(i,i+4);
       i=i+4;
       setTimeout(OpenToWork, speed);
     }
   }
    console.log(txt);
