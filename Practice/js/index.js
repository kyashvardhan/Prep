
var randomNumber1= Math.floor(Math.random()*6+1);
var randomNumber2=Math.floor(Math.random()*6+1);

var image1=document.querySelector(".img1");
var image2=document.querySelector(".img2");


image1.setAttribute("src","images/dice"+randomNumber1+".png");
image2.setAttribute("src","images/dice"+randomNumber2+".png");

p1=randomNumber1;
p2=randomNumber2;

if(p1>p2){
    document.querySelector("h1").innerText="Player One Won";
}
else{
    document.querySelector("h1").innerText="Player Two Won";
}

