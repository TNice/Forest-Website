function SimulationMarker(latlng, map, args) {
	this.latlng = latlng;	
	this.args = args;	
	this.setMap(map);	
}

SimulationMarker.prototype = new google.maps.OverlayView();

SimulationMarker.prototype.draw = function() {
	
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
        timestepInput.className = 'simulation-input';
        inputs.appendChild(timestepInput);

        sizeInput = document.createElement('input');
        sizeInput.className = 'simulation-input';
        inputs.appendChild(sizeInput); 
        
        varInput = document.createElement('input');
        varInput.className = 'simulation-input';
        inputs.appendChild(varInput); 
        
        simulateButton = document.createElement('button');
        simulateButton.className = 'simulate-button';
        simulateButton.innerText = "Simulate";
        simulateButton.addEventListener("click", function(event){
            console.log("SIMULATE!");
        });
        inputs.appendChild(simulateButton);

        container.appendChild(labels);
        container.appendChild(inputs);

        
        
        div.appendChild(container);

		if (typeof(self.args.marker_id) !== 'undefined') {
			div.dataset.marker_id = self.args.marker_id;
		}
		
		google.maps.event.addDomListener(div, "click", function(event) {			
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

SimulationMarker.prototype.remove = function() {
	if (this.div) {
		this.div.parentNode.removeChild(this.div);
		this.div = null;
	}	
};

SimulationMarker.prototype.getPosition = function() {
	return this.latlng;	
};

SimulationMarker.prototype.setPosition = function(latlng){
    this.latlng = latlng;
};