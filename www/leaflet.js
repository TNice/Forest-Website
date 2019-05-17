// Before map is being initialized.
var mapsPlaceholder = [];
var myMap = null;
window.shape = null;
var polygonDrawer = null;

L.Map.addInitHook(function () {
    mapsPlaceholder.push(this); // Use whatever global scope variable you like.
});