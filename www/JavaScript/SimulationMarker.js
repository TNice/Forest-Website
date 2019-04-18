//Rectangle region = bounds. Use getSouthWest or getNorthEast Functions
var nwlat = 0;
var nwLng = 0;
var seLat = 0;
var seLng = 0;

function SimulationMarker(latlng, map, args, nwlat, nwlng, selat, swlng) {
    this.latlng = latlng;
    this.args = args;
    this.setMap(map);
    nwLat = nwlat;
    nwLng = nwlng;
    seLat = selat;
    seLng = swlng;
}

SimulationMarker.prototype = new google.maps.OverlayView();

SimulationMarker.prototype.draw = function () {

    var self = this;

    var div = this.div;

    if (!div) {

        //create main div
        div = this.div = document.createElement('div');
        div.className = 'simulation-box';

        //create title of the dive
        title = document.createElement('label');
        titleText = document.createTextNode("Simulation");
        title.appendChild(titleText);
        title.className = "title";
        div.appendChild(title);

        //create inputs
        container = document.createElement('div');
        container.className = "row";

        labels = document.createElement('div');
        labels.className = 'col-6';


        timestepLabel = document.createElement('label');
        timestepLabel.className = "simulation-label";
        timestepText = document.createTextNode("Time Step:");
        timestepLabel.appendChild(timestepText);
        labels.appendChild(timestepLabel);

        sizeLabel = document.createElement('label');
        sizeLabel.className = "simulation-label";
        sizeText = document.createTextNode("Side Length:");
        sizeLabel.appendChild(sizeText);
        labels.appendChild(sizeLabel);

        varLabel = document.createElement('label');
        varLabel.className = "simulation-label";
        varText = document.createTextNode("Side Variance:");
        varLabel.appendChild(varText);
        labels.appendChild(varLabel);

        inputs = document.createElement('div');
        inputs.className = 'col-6';

        timestepInput = document.createElement('input');
        timestepInput.id = "timestep-input";
        timestepInput.type = "number";
        timestepInput.value = "5";
        timestepInput.className = 'simulation-input';
        inputs.appendChild(timestepInput);

        sizeInput = document.createElement('input');
        sizeInput.id = "size-input";
        sizeInput.type = "number";
        sizeInput.value = "30";
        sizeInput.className = 'simulation-input';
        inputs.appendChild(sizeInput);

        varInput = document.createElement('input');
        varInput.id = "var-input";
        varInput.type = "number";
        varInput.value = "3";
        varInput.className = 'simulation-input';
        inputs.appendChild(varInput);

        simulateButton = document.createElement('button');
        simulateButton.className = 'simulate-button';
        simulateButton.innerText = "Simulate";
        simulateButton.addEventListener("click", function (event) {
            let timestep = document.getElementById("timestep-input").value;
            let size = document.getElementById("size-input").value;
            let variance = document.getElementById("var-input").value;

            console.log("SIMULATION INPUTS\nTimestep: " + timestep + "\nSize: " + size + "\nVariance: " + variance);

            var xmlhttp = new XMLHttpRequest();
            xmlhttp.timeout = 20000;
            xmlhttp.onreadystatechange = function () {
                if (this.readyState == 4 && this.status == 200) {
                    console.log(this.responseText);
                    if (this.responseText == "Done") {
                        LoadHeatMap();
                    }
                }
            };

            xmlhttp.open("GET", "./util/Simulate.php?time=" + timestep + "&size=" + size + "&var=" + variance + "&nwLat=" + nwLat + "&nwLng=" + nwLng + "&seLat=" + seLat + "&seLng=" + seLng, true);
            console.log("Runing Simulation");
            xmlhttp.send();


        });
        inputs.appendChild(simulateButton);

        container.appendChild(labels);
        container.appendChild(inputs);

        div.appendChild(container);

        if (typeof (self.args.marker_id) !== 'undefined') {
            div.dataset.marker_id = self.args.marker_id;
        }

        google.maps.event.addDomListener(div, "click", function (event) {
            google.maps.event.trigger(self, "click");
        });

        var panes = this.getPanes();
        panes.overlayImage.appendChild(div);
    }

    var point = this.getProjection().fromLatLngToDivPixel(this.latlng);

    if (point) {
        div.style.left = point.x + 'px';
        div.style.top = point.y + 'px';
    }
};

SimulationMarker.prototype.remove = function () {
    if (this.div) {
        this.div.parentNode.removeChild(this.div);
        this.div = null;
    }
};

SimulationMarker.prototype.getPosition = function () {
    return this.latlng;
};

SimulationMarker.prototype.setPosition = function (latlng) {
    this.latlng = latlng;
};

SimulationMarker.prototype.setBoundsCords = function (nwlat, nwlng, selat, swlng) {
    this.nwlat = nwlat;
    this.nwlng = nwlng;
    this.selat = selat;
    this.selng = swlng;
};