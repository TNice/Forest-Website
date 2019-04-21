function CellMarker(map, latlng, value=0, color="#0000FF") {
    this.pos = latlng;
    this.value = value;
    this.color = color;
    this.map = map;
}

CellMarker.prototype = new google.maps.Marker({
    position: this.pos,
    map: this.map,
    icon: {
      path: google.maps.SymbolPath.CIRCLE,
      fillColor: this.color,
      fillOpacity: 0.6,
      scale: 7
    },
    value: 12 
  });