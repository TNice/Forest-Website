 // don't forget to add gmaps-heatmap.js
 var myLatlng = new google.maps.LatLng(38.917724, -92.092734);
 // map options,
 var myOptions = {
  zoom: 5,
  maxZoom: 10,
  minZoom: 3,
  center: myLatlng,
  disableDefaultUI: true,
  mapTypeControl: false,
  streetViewControl: false,
  scaleControl: false,
  gestureHandling: 'greedy',
  zoomControl: false,
  zoomControlOptions: {
    style: google.maps.ZoomControlStyle.LARGE 
  },
  mapTypeId: google.maps.MapTypeId.ROADMAP
 };
 // standard map
 map = new google.maps.Map(document.getElementById("map"), myOptions);

 var drawingManager = new google.maps.drawing.DrawingManager({
  //drawingMode: google.maps.drawing.OverlayType.MARKER,
  drawingControl: true,
  drawingControlOptions: {
    position: google.maps.ControlPosition.TOP_CENTER,
    drawingModes: ['circle', 'rectangle']
  },
  circleOptions: {
    fillColor: '#555555',
    fillOpacity: 0.35,
    strokeWeight: 0,
    clickable: false,
    editable: false,
    zIndex: 1
  }
});
drawingManager.setMap(map);
 // heatmap layer
 heatmap = new HeatmapOverlay(map, {
   // radius should be small ONLY if scaleRadius is true (or small radius is intended)
   "radius": 5,
   "maxOpacity": 1,
   "minOpacity": .25,
   // scales the radius based on map zoom
   "scaleRadius": false,
   "useLocalExtrema": true,
   "gradient":{
     '.25': 'rgba(0,26,0,1)',
     '.5': 'rgba(0,128,0,1)',
     '.95': 'rgba(0,255,0,1)'
   },
   latField: 'lat',
   lngField: 'lng',
   valueField: 'gso'
 });
 

jQuery.getJSON("util/results/gsoData1.json", function(data){
  console.log(data);
  heatmap.setData(data);
});

google.maps.event.addListener(drawingManager, 'polygoncomplete', function (polygon) {
  var coordinates = polygon.getPath().getArray();
  console.log("Polygon Cords: " + coordinates);
});

google.maps.event.addListener(drawingManager, 'circlecomplete', function (circle) {
  var bounds = circle.getBounds();
  console.log(bounds);
});

google.maps.event.addListener(drawingManager, 'rectanglecomplete', function (rectangle) {
  var coords = rectangle.getBounds();
  console.log("Rectangle Cords: " + coords);
});

