document.getElementsByName("taille").item(0).addEventListener('change', updateValue);
document.getElementsByName("poids").item(0).addEventListener('change', updateValue);
function updateValue() {
    let pesages = document.getElementsByClassName("poids"); // Cette boucle est nécessaire pour remettre tout les textes en noir
    for(var i=0, len=pesages.length; i<len; i++)
    {
        pesages[i].style["color"] = "black";
    }
    let taille = document.getElementsByName("taille").item(0).value; // On Calcule ici l'IMC
    let poids = document.getElementsByName("poids").item(0).value;
    let IMC = parseInt(poids)/Math.pow(parseInt(taille)/100, 2);
    if (IMC <= 18.5) { // On colore ensuite la bonne phrase
        document.getElementById("18,5").style.color = "blue";
    }
    else if (IMC <= 25) {
        document.getElementById("25").style.color = "blue";
    }
    else if (IMC <= 30) {
        document.getElementById("30").style.color = "blue";
    }
    else if (IMC <= 35) {
        document.getElementById("35").style.color = "blue";
    }
    else if (IMC <= 40) {
        document.getElementById("40").style.color = "blue";
    }
    else if (IMC > 40) {
        document.getElementById("40+").style.color = "blue";
    }
    document.getElementById("IMC").innerHTML = "Votre IMC: "+String(IMC); // Puis on affiche le texte
}
updateValue(); //Ici c'est surtout pour quand vous changez la valeur puis rechargez la page sans vider le cache