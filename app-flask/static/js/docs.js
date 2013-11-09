$(document).ready(function() {
// 	var FOURSQUARE_CLIENT_ID = 'G1H4IBM4VPMNJKLCS052GHLQ1KGFLERLJ2PZSUEQPT2DYO4N';
// 	var FOURSQUARE_CLIENT_SECRET = 'JY0OEGB41GBV1FVCJDIOCPUUJDZKQBBUFVCDYSHNTGTC2CF2';

// 	// http://www.codeproject.com/Tips/191892/How-to-find-current-location-based-on-the-IP-addre
// 	// http://dotnetnukes.blogspot.com.br/2013/03/javascript-get-user-ip-address-latitude.html
	var lat = geoip_latitude();
	var lng = geoip_longitude();

	var arr = new Array();
	var curr_marker;
	// var curr_circle;
	var icone = L.icon({
    	iconUrl: '/static/img/marker.png',
    	iconSize:     [31, 41], // size of the icon
   		iconAnchor:   [17, 44], // point of the icon which will correspond to marker's location
    	// popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
	});
	
	var map = L.map('map', {
		center: [lat,lng],
		zoom: 14,
		minZoom: 10,
		maxZoom: 20
	});

	L.tileLayer('http://{s}.tile.cloudmade.com/ba52dbcbe23f4cdba4adb592d2420275/101015/256/{z}/{x}/{y}.png', {
    	// attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
    	maxZoom: 18
	}).addTo(map);


// 	// Geolocation Engine for IP or navigator.geolocation
// 	function geo_success(position) {
// 	  	lat = position.coords.latitude;
//   		lon = position.coords.longitude;
//   		getUserLocation(lat, lng);
// 	}

// 	function geo_error() {
// 	  	getUserLocation(lat, lng);
// 	}

// 	var geo_options = {
// 	  	enableHighAccuracy: true, 
// 	  	maximumAge        : 30000, 
// 		timeout           : 27000
// 	};

// 	getUserLocation(lat, lng);
// 	if(navigator.geolocation) {
// 		navigator.geolocation.watchPosition(geo_success, geo_error, geo_options);
// 	}

// 	$('.centerSide input#address').val(geoip_city() + ', ' + geoip_country_code());


// // http://dev.w3.org/geo/api/spec-source.html
// 	// function buttonClickHandler() {
//  //      // Cancel the updates when the user clicks a button.
//  //      navigator.geolocation.clearWatch(watchId);
//  //    }

// 	function getUserLocation(lat, lgn){
// 		if (curr_marker != undefined)
// 			map.removeLayer(curr_marker);
// 		// if (curr_circle != undefined)
// 		// 	map.removeLayer(curr_circle);

// 		map.setView( new L.LatLng(lat, lng),13, false);
// 		curr_marker = L.marker([lat, lng]).addTo(map);
// 		// curr_circle = new L.Circle( new L.LatLng(lat, lng), 2000, {fillColor:'#b3ebf9', stroke:true}).addTo(map);				
// 	}

// 	// categories
// 	var categories = [];
// 	date = new Date().getFullYear() + new Date().getMonth()+1 + new Date().getDate();
// 	q = "https://api.foursquare.com/v2/venues/categories?locale=pt&v=" + date + "&client_id=" + FOURSQUARE_CLIENT_ID + "&client_secret=" + FOURSQUARE_CLIENT_SECRET;
// 	$.getJSON(q).done(function (data){
// 		console.log(data.response.categories);
// 		$.each(data.response.categories, function(key, value){
// 			categories.push(value.name);
// 			console.log(value.name);
// 		});

// 			// console.log(categories);
// 	});
// 	// venue
// 	// http://tatiyants.com/how-to-use-json-objects-with-twitter-bootstrap-typeahead/
// 	$('.centerSide input#search').typeahead({
// 		source: function(query, process) {
// 			keywords = [];
// 			keywords.push($('.centerSide input#search').val());

// 			date = new Date().getFullYear() + new Date().getMonth()+1 + new Date().getDate();
// 			q = "https://api.foursquare.com/v2/venues/suggestcompletion?locale=pt&ll="+lat+","+lng+"&radius=7000&v=" + date + "&query=" + $(".centerSide input#search").val() + "&client_id=" + FOURSQUARE_CLIENT_ID + "&client_secret=" + FOURSQUARE_CLIENT_SECRET;
		
// 			$.getJSON(q).done(function (json){
// 				$.each(json.response.minivenues, function(key, value){
// 					keywords.push(value.name);
// 				});
// 				process(keywords);
			
// 			});

// 		},
// 		updater: function (item) {
//     		$('.centerSide button').click();
//   			return item;
// 		},
// 		template: [                                                                 
//     		'<p class="repo-language">{{language}}</p>',                              
//     		'<p class="repo-name">{{name}}</p>',                                      
//     		'<p class="repo-description">{{description}}</p>'                         
//   		].join(''),
// 	});
// 	// http://twitter.github.io/typeahead.js/examples/

// 	$(".centerSide button").click(function(e) {
// 		$.each(arr, function(key, value) {
// 			map.removeLayer(arr.pop());
// 		});

// 		date = new Date().getFullYear() + new Date().getMonth()+1 + new Date().getDate();
// 		lat = lat;
// 		lng = lng;
// 		q = "https://api.foursquare.com/v2/venues/search?ll="+lat+","+lng+"&radius=7000&v=" + date + "&query=" + $(".centerSide input#search").val() + "&client_id=" + FOURSQUARE_CLIENT_ID + "&client_secret=" + FOURSQUARE_CLIENT_SECRET;
// 		q = "https://api.foursquare.com/v2/venues/search?near=Ribeirão+Preto&radius=7000&v=" + date + "&query=" + $(".centerSide input#search").val() + "&client_id=" + FOURSQUARE_CLIENT_ID + "&client_secret=" + FOURSQUARE_CLIENT_SECRET; 
// 		$.getJSON(q).done(function (json){
//     		$.each(json.response.groups[0].items, function(key, value){
//     			var marker = L.marker([value.location.lat, value.location.lng], {
//     			riseOnHover: true,
//     			opacity: 0.6,
//     			title: value.name,
//     			icon: icone
//     			});
//     			arr.push(marker);
//     			marker.addTo(map);
//     		});
//     	});
		
// 	});






// 	// Physical location
// 	$('.geolocationBT').click(function(){
// 		if(navigator.geolocation) {
// 			navigator.geolocation.watchPosition(geo_success, geo_error, geo_options);
// 		}
// 	});
	
	// function mapOnGeolocation(position){
	// 	lat = position.coords.latitude;
	// 	lon = position.coords.longitude;
	// 	map.setView( new L.LatLng(lat, lon),14, false);
	// 	curr_marker = L.marker([lat, lon]).addTo(map);				
	// }

	

});