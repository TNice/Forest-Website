 // don't forget to add gmaps-heatmap.js
 var myLatlng = new google.maps.LatLng(25.6586, -80.3568);
 // map options,
 var myOptions = {
   zoom: 3,
   center: myLatlng
 };
 // standard map
 map = new google.maps.Map(document.getElementById("map"), myOptions);
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

