var selected = "";

function ShowSpeciesNav() {
    document.getElementById("speciesNav").style.width = "6vw";
}

function CloseLogin() {
    document.getElementById("login").style.visibility = "hidden"
}

function ShowLogin() {
    document.getElementById("login").style.visibility = "visible"
}

//Used to hide species when scrolling through 
function HideSpeciesNavMain(elem) {
    var overSpeciesMenu = false;
    var sideLeft = closestEdge(elem);

    if (selected != "species" && sideLeft != "right") {
        document.getElementById("speciesNav").style.width = "0";
    }
}

//Used to hide species when you leave the sub menu
function HideSpeciesNavSub() {
    var overSpeciesMenu = false;

    if (selected != "species") {
        document.getElementById("speciesNav").style.width = "0";
    }
}

function ShowDisturbanceNav() {
    document.getElementById("disturbanceNav").style.width = "6vw";
    document.getElementById('search').style.borderBottomRightRadius = '0';
}

//Used to hide disturbances when scrolling through 
function HideDisturbanceNavMain(elem) {
    var overSpeciesMenu = false;
    var sideLeft = closestEdge(elem);

    if (selected != "disturbance" && sideLeft != "right") {
        document.getElementById("disturbanceNav").style.width = "0";
        document.getElementById('search').style.borderBottomRightRadius = '';
    }
}

//Used to hide disturbances when you leave the sub menu
function HideDisturbanceNavSub() {
    var overSpeciesMenu = false;

    if (selected != "disturbance") {
        document.getElementById("disturbanceNav").style.width = "0";
        document.getElementById('search').style.borderBottomRightRadius = '';
    }
}


function ShowActivitiesNav() {
    document.getElementById("activitiesNav").style.width = "6vw";
    //document.getElementById("wind").style.borderTopRightRadius = "0";
    document.getElementById("human").style.borderBottomRightRadius = "0";
}

//Used to hide human activities when scrolling through 
function HideActivitiesNavMain(elem) {
    var overSpeciesMenu = false;
    var sideLeft = closestEdge(elem);

    if (selected != "activities" && sideLeft != "right") {
        document.getElementById("activitiesNav").style.width = "0";
        // document.getElementById("wind").style.borderTopRightRadius = "";
        document.getElementById("human").style.borderBottomRightRadius = "";

    }

}

//Used to hide human activities when you leave the sub menu
function HideActivitiesNavSub() {
    var overSpeciesMenu = false;

    if (selected != "activities") {
        setTimeout(ShouldHideDisturbace(), 100);
    }
}

function ShouldHideDisturbace() {
    var x = event.clientX;
    var y = event.clientY;

    var elements = document.elementsFromPoint(x, y);

    var shouldHide = true;
    for (i = 0; i < elements.length; i++) {
        console.log(elements[i].id);
        if (elements[i].id == "human") {
            shouldHide = false;
        }
    }

    console.log(shouldHide);
    if (shouldHide == true) {
        HideDisturbanceNavSub();
        document.getElementById("activitiesNav").style.transition = "0.0s";
        document.getElementById("activitiesNav").style.width = "0";
    } else {
        document.getElementById("activitiesNav").style.transition = "0.1s";
        document.getElementById("activitiesNav").style.width = "0";
    }
}

function HideSsNavSub() {
    var overSpeciesMenu = false;

    if (selected != "species") {
        document.getElementById("speciesNav").style.width = "0";
    }
}

function activateStatButton() {
    var element = document.getElementById("statButton");
    element.classList.add("active")
    document.getElementById("deepButton").classList.remove("active");
    document.getElementById("statDiv").style.height = "";
    document.getElementById("deepDiv").style.height = "0";
}

function activateDeepButton() {
    var element = document.getElementById("deepButton");
    element.classList.add("active");
    document.getElementById("statButton").classList.remove("active");
    document.getElementById("statDiv").style.height = "0";
    document.getElementById("deepDiv").style.height = "15vh";
}


function closestEdge(elem) {
    var elemBounding = elem.getBoundingClientRect();

    var elementLeftEdge = elemBounding.left;
    var elementTopEdge = elemBounding.top;
    var elementRightEdge = elemBounding.right;
    var elementBottomEdge = elemBounding.bottom;

    var mouseX = event.clientX;
    var mouseY = event.clientY;

    var topEdgeDist = Math.abs(elementTopEdge - mouseY);
    var bottomEdgeDist = Math.abs(elementBottomEdge - mouseY);
    var leftEdgeDist = Math.abs(elementLeftEdge - mouseX);
    var rightEdgeDist = Math.abs(elementRightEdge - mouseX);

    var min = Math.min(topEdgeDist, bottomEdgeDist, leftEdgeDist, rightEdgeDist);

    switch (min) {
        case leftEdgeDist:
            return "left";
        case rightEdgeDist:
            return "right";
        case topEdgeDist:
            return "top";
        case bottomEdgeDist:
            return "bottom";
    }
}