var rt1 = document.querySelector("#rformtop1");
var rt2 = document.querySelector("#rformtop2");
var rt3 = document.querySelector("#rformtop3");

var st1 = document.querySelector("#sformtop1");
var st2 = document.querySelector("#sformtop2");
var st3 = document.querySelector("#sformtop3");

var alert1 = document.querySelector("#ralert");
var alert2 = document.querySelector("#salert");

var subToppings = document.querySelector("#subtoppingform");

rt1.style.display = "none";
rt2.style.display = "none";
rt3.style.display = "none";

st1.style.display = "none";
st2.style.display = "none";
st3.style.display = "none";

alert1.style.display = "none";
alert2.style.display = "none";

subToppings.style.display = "none";


function toggleRegularToppings(){
    let type = document.querySelector("#rtype").value;
    if(type == "Cheese"){
        rt1.style.display = "none";
        rt2.style.display = "none";
        rt3.style.display = "none";
        alert1.style.display = "none";
    }
    else if(type == "1topping"){
        rt1.style.display = "block";
        rt2.style.display = "none";
        rt3.style.display = "none";
        alert1.style.display = "none";
    }
    else if(type == "2toppings"){
        rt1.style.display = "block";
        rt2.style.display = "block";
        rt3.style.display = "none";
        alert1.style.display = "none";
    }
    else if(type == "3toppings"){
        rt1.style.display = "block";
        rt2.style.display = "block";
        rt3.style.display = "block";
        alert1.style.display = "none";
    }
    else if(type == "Special"){
        rt1.style.display = "none";
        rt2.style.display = "none";
        rt3.style.display = "none";
        alert1.style.display = "block";
    }
}

function toggleSicilianToppings(){
    let type = document.querySelector("#stype").value;
    if(type == "Cheese"){

        st1.style.display = "none";
        st2.style.display = "none";
        st3.style.display = "none";
        alert2.style.display = "none";
    }
    else if(type == "1item"){

        st1.style.display = "block";
        st2.style.display = "none";
        st3.style.display = "none";
        alert2.style.display = "none";
    }
    else if(type == "2items"){

        st1.style.display = "block";
        st2.style.display = "block";
        st3.style.display = "none";
        alert2.style.display = "none";
    }
    else if(type == "3items"){
        st1.style.display = "block";
        st2.style.display = "block";
        st3.style.display = "block";
        alert2.style.display = "none";
    }
    else if(type == "Special"){
        st1.style.display = "none";
        st2.style.display = "none";
        st3.style.display = "none";
        alert2.style.display = "block";
    }
}

function toggleSubToppings(){
    let type = document.querySelector("#subtype").value;
    if(type == "Steak+Cheese"){
        subToppings.style.display = "block";
    }
}


