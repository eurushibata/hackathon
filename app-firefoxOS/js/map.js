$(document).ready(function() {

	var lat = geoip_latitude();
	var lng = geoip_longitude();

	var arr = new Array();
	var curr_marker;

	var map = L.map('map', {
		center: [-23.566282,-46.642934],
    	zoom: 14,
    	minZoom: 10,
    	maxZoom: 20
	});

	L.tileLayer('http://{s}.tile.cloudmade.com/ba52dbcbe23f4cdba4adb592d2420275/101015/256/{z}/{x}/{y}.png', {
		maxZoom: 18
	}).addTo(map);


	// L.marker([lat, lng]).addTo(map);
		

	if (navigator.geolocation) {
	  	navigator.geolocation.watchPosition(geo_success, geo_error, geo_options);
	} else {
	  error('not supported');
	}


	// var popup = L.popup();

	// function onMapClick(e) {
	// 	popup
	// 		.setLatLng(e.latlng)
	// 		.setContent("You clicked the map at " + e.latlng.toString())
	// 		.openOn(map);
	// }

	// map.on('click', onMapClick);

	// Geolocation Engine for IP or navigator.geolocation
	function geo_success(position) {
	  	lat = position.coords.latitude;
  		lng = position.coords.longitude;
		L.marker([lat, lng]).addTo(map);
  		getUserLocation(lat, lng);
	}

	function geo_error() {
	  	getUserLocation(lat, lng);
	}

	var geo_options = {
	  	enableHighAccuracy: true, 
	  	maximumAge        : 30000, 
		timeout           : 27000
	};

	getUserLocation(lat, lng);
	if(navigator.geolocation) {
		navigator.geolocation.watchPosition(geo_success, geo_error, geo_options);
	}

	function getUserLocation(lat, lng){
		if (curr_marker != undefined)
			map.removeLayer(curr_marker);
		// if (curr_circle != undefined)
		// 	map.removeLayer(curr_circle);

		map.setView( new L.LatLng(lat, lng),14, false);
		curr_marker = L.marker([lat, lng]).addTo(map);
		curr_circle = new L.Circle( new L.LatLng(lat, lng), 1250, {fillColor:'#b3ebf9', stroke:true}).addTo(map);				
	}


	// Physical location
	$('.geolocationBT').click(function(){
		if(navigator.geolocation) {
			navigator.geolocation.watchPosition(geo_success, geo_error, geo_options);
		}
	});
	
	function mapOnGeolocation(position){
		lat = position.coords.latitude;
		lng = position.coords.longitude;
		map.setView( new L.LatLng(lat, lng),14, false);
		curr_marker = L.marker([lat, lng]).addTo(map);				
	}





	$("input#search-input").keyup(function(e) {
		alert('ass');
	});



});
		