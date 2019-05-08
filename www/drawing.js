console.log("button clicked");
if (myMap == null) {
    myMap = mapsPlaceholder.pop()
}

let polygonDrawer = new L.Draw.Polyline(map);

// Assumming you have a Leaflet map accessible
myMap.on('draw:created', function (e) {
    var type = e.layerType,
        layer = e.layer;

    // Do whatever you want with the layer.
    // e.type will be the type of layer that has been draw (polyline, marker, polygon, rectangle, circle)
    // E.g. add it to the map
    layer.addTo(myMap);
});

// Click handler for you button to start drawing polygons
$('#draw_poly').click(function () {
    polygonDrawer.enable();
});