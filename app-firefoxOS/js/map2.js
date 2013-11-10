$(document).ready(function() {

$("form#search-form").on("submit", function() {
	
		var searchTerm = $("input#address").val();

		// Binding of DOM elements to several variables so we can install event handlers.
		// var progressUiElt = document.getElementById("progress");

		// progressUiElt.innerHTML = "Looking for '" + searchTerm+ "'...";

		/* Once the map is initialized and ready (an event that is fired only once),
		 * trigger a geocoding request.
		 */
		map.addListener("displayready", function () {
			searchManager.geoCode({
				searchTerm: searchTerm,
				onComplete: processResults
			});
		});

	});


});
		