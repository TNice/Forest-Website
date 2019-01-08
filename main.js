/*Submenu Ids:
Species = 0
Disturbance = 1
*/

function OpenSubMenu(id) {
    var tagId = "sub-menu-" + id;
    console.log(tagId);
    document.getElementById(tagId).style.width = "10vw";
}

function CloseSubMenu(id) {
    var tagId = "sub-menu-" + id;
    console.log(tagId);
    document.getElementById(tagId).style.width = "0";
}