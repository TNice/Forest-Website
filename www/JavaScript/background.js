 // don't forget to add gmaps-heatmap.js
 var myLatlng = new google.maps.LatLng(38.917724, -92.092734);
 // map options,
 var myOptions = {
   zoom: 5,
   maxZoom: 10,
   minZoom: 3,
   center: myLatlng,
   disableDefaultUI: true,
   disableDoubleClickZoom: true,
   mapTypeControl: false,
   streetViewControl: false,
   scaleControl: false,
   gestureHandling: 'greedy',
   zoomControl: true,
   mapTypeId: google.maps.MapTypeId.ROADMAP
 };

 //Controls Map Colors, Labels, ect.
 var styledMapType = new google.maps.StyledMapType(
   [{
       "elementType": "geometry",
       "stylers": [{
         "color": "#ebe3cd"
       }]
     },
     {
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#523735"
       }]
     },
     {
       "elementType": "labels.text.stroke",
       "stylers": [{
         "color": "#f5f1e6"
       }]
     },
     {
       "featureType": "administrative",
       "elementType": "geometry",
       "stylers": [{
         "visibility": "on"
       }]
     },
     {
       "featureType": "administrative",
       "elementType": "geometry.stroke",
       "stylers": [{
         "color": "#c9b2a6"
       }]
     },
     {
       "featureType": "administrative.land_parcel",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "administrative.land_parcel",
       "elementType": "geometry.stroke",
       "stylers": [{
         "color": "#dcd2be"
       }]
     },
     {
       "featureType": "administrative.land_parcel",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#ae9e90"
       }]
     },
     {
       "featureType": "administrative.neighborhood",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "landscape.natural",
       "elementType": "geometry",
       "stylers": [{
         "color": "#dfd2ae"
       }]
     },
     {
       "featureType": "poi",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "poi",
       "elementType": "geometry",
       "stylers": [{
         "color": "#dfd2ae"
       }]
     },
     {
       "featureType": "poi",
       "elementType": "labels.text",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "poi",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#93817c"
       }]
     },
     {
       "featureType": "poi.park",
       "elementType": "geometry.fill",
       "stylers": [{
         "color": "#a5b076"
       }]
     },
     {
       "featureType": "poi.park",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#447530"
       }]
     },
     {
       "featureType": "road",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "road",
       "elementType": "geometry",
       "stylers": [{
         "color": "#f5f1e6"
       }]
     },
     {
       "featureType": "road",
       "elementType": "labels",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "road",
       "elementType": "labels.icon",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "road.arterial",
       "elementType": "geometry",
       "stylers": [{
         "color": "#fdfcf8"
       }]
     },
     {
       "featureType": "road.highway",
       "elementType": "geometry",
       "stylers": [{
         "color": "#f8c967"
       }]
     },
     {
       "featureType": "road.highway",
       "elementType": "geometry.stroke",
       "stylers": [{
         "color": "#e9bc62"
       }]
     },
     {
       "featureType": "road.highway.controlled_access",
       "elementType": "geometry",
       "stylers": [{
         "color": "#e98d58"
       }]
     },
     {
       "featureType": "road.highway.controlled_access",
       "elementType": "geometry.stroke",
       "stylers": [{
         "color": "#db8555"
       }]
     },
     {
       "featureType": "road.local",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#806b63"
       }]
     },
     {
       "featureType": "transit",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "transit.line",
       "elementType": "geometry",
       "stylers": [{
         "color": "#dfd2ae"
       }]
     },
     {
       "featureType": "transit.line",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#8f7d77"
       }]
     },
     {
       "featureType": "transit.line",
       "elementType": "labels.text.stroke",
       "stylers": [{
         "color": "#ebe3cd"
       }]
     },
     {
       "featureType": "transit.station",
       "elementType": "geometry",
       "stylers": [{
         "color": "#dfd2ae"
       }]
     },
     {
       "featureType": "water",
       "elementType": "geometry.fill",
       "stylers": [{
         "color": "#b9d3c2"
       }]
     },
     {
       "featureType": "water",
       "elementType": "labels.text",
       "stylers": [{
         "visibility": "off"
       }]
     },
     {
       "featureType": "water",
       "elementType": "labels.text.fill",
       "stylers": [{
         "color": "#92998d"
       }]
     }
   ], {
     name: 'Styled Map'
   });

 // standard map
 map = new google.maps.Map(document.getElementById("map"), myOptions);

 map.mapTypes.set('styled_map', styledMapType);
 map.setMapTypeId('styled_map');

 //Drawomg Controls
 var drawingManager = new google.maps.drawing.DrawingManager({
   drawingControl: false,
   drawingControlOptions: {
     position: google.maps.ControlPosition.TOP_CENTER,
     drawingModes: ['rectangle', 'polygon']
   },
   rectangleOptions: {
     fillColor: '#555555',
     fillOpacity: 0.35,
     strokeWeight: 0,
     clickable: false,
     editable: false,
     zIndex: 1
   },
   polygonOptions: {
     fillColor: '#555555',
     fillOpacity: 0.35,
     strokeWeight: 0,
     clickable: false,
     editable: false,
     zIndex: 1
   }
 });
 drawingManager.setMap(map);

 //creates the simulation panel.
 var overlay = null;

 //Deals with drawing shaps on the map
 var shape = null;
 google.maps.event.addListener(drawingManager, "drawingmode_changed", function () {
   if (overlay != null) {
     overlay.setMap(null);
   }
   if ((drawingManager.getDrawingMode() == google.maps.drawing.OverlayType.RECTANGLE || drawingManager.getDrawingMode() == google.maps.drawing.OverlayType.POLYGON) &&
     (shape != null))
     shape.setMap(null);
 });

 google.maps.event.addListener(drawingManager, 'overlaycomplete', function (event) {
   if (event.type == google.maps.drawing.OverlayType.RECTANGLE) {
     if (shape != null)
       shape.setMap(null);
     shape = event.overlay;
     var bounds = shape.getBounds();
     console.log(bounds);
     drawingManager.setDrawingMode(null);
     var simulation = new google.maps.LatLng(bounds.getSouthWest().lat(), bounds.getNorthEast().lng());
     var zoom = new google.maps.LatLng(bounds.getSouthWest().lat() - 7, bounds.getNorthEast().lng());
     map.panTo(zoom);
     overlay = new SimulationMarker(
       simulation,
       map, {},
       bounds.getNorthEast().lat(),
       bounds.getSouthWest().lng(),
       bounds.getSouthWest().lat(),
       bounds.getNorthEast().lng()
     );

   } else if (event.type == google.maps.drawing.OverlayType.POLYGON) {
     if (shape != null)
       shape.setMap(null);
     shape = event.overlay;
     var path = shape.getPath();
     console.log(path);
     drawingManager.setDrawingMode(null);
   }

   document.getElementById("draw").style.backgroundColor = "rgba(0,0,0,0)";
   document.getElementById("select").style.backgroundColor = "rgba(0,0,0,0)";

 });

 function clearDrawing() {
   shape.setMap(null);
 }

 //rgb(185, 195, 185)
 function DrawRectangle() {
   if (drawingManager.getDrawingMode() == google.maps.drawing.OverlayType.RECTANGLE) {
     drawingManager.setDrawingMode(null);
     document.getElementById("select").style.backgroundColor = "rgba(0,0,0,0)";
   } else {
     drawingManager.setDrawingMode(google.maps.drawing.OverlayType.RECTANGLE);
     document.getElementById("select").style.backgroundColor = "rgb(185, 195, 185)";
     document.getElementById("draw").style.backgroundColor = "rgba(0,0,0,0)";
   }
 }

 function DrawPoly() {
   if (drawingManager.getDrawingMode() == google.maps.drawing.OverlayType.POLYGON) {
     drawingManager.setDrawingMode(null);
     document.getElementById("draw").style.backgroundColor = "rgba(0,0,0,0)";
   } else {
     drawingManager.setDrawingMode(google.maps.drawing.OverlayType.POLYGON);
     document.getElementById("draw").style.backgroundColor = "rgb(185, 195, 185)";
     document.getElementById("select").style.backgroundColor = "rgba(0,0,0,0)";
   }
  }

 async function CreateMarker(lat, lng, color, value){
    var marker = new google.maps.Marker({
      position: {lat: lat, lng: lng},
      map: map,
      icon: {
        path: google.maps.SymbolPath.CIRCLE,
        fillColor: color,
        fillOpacity: 0.6,
        scale: 7
      },
      value: value 
    });

    google.maps.event.addListener(marker, 'click', function(){
      print(this.value);
    })
 }

 Shiny.addCustonMessageHandler("CellUpdated", function(message){
   lat = message["lat"];
   lng = message["lng"];
   color = message["color"];
   value = message["value"];

   CreateMarker(lat, lng, color, value);
 })