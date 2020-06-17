
var cardSpan = document.querySelectorAll(".card-toppings span");
var cardSubtitle = document.querySelectorAll(".card-toppings");

for(i=0; i<cardSpan.length; i++){
    console.log(cardSpan[i].textContent);
    if(cardSpan[i].textContent == "None"){
        cardSubtitle[i].style.display = "none";
    }
}

