$(document).ready(function() {
    $('.sidenav').sidenav();
    $(".dropdown-trigger1").dropdown();
    $(".dropdown-trigger2").dropdown();
});

var locationEthio = { lat: 9.1156, lng: 38.7722 };

function initMap() {
    var myOptions = {
            zoom: 5,
            center: locationEthio,
        },
        map = new google.maps.Map(document.getElementById('map'), myOptions),
        marker = new google.maps.Marker({
            map: map,
        }),
        infowindow = new google.maps.InfoWindow;
    map.addListener('rightclick', function(e) {
        map.setCenter(e.latLng);
        marker.setPosition(e.latLng);
        infowindow.setContent("Latitude: " + e.latLng.lat() +
            "<br>" + "Longitude: " + e.latLng.lng());
        document.getElementById('latitude').value = e.latLng.lat();
        document.getElementById('longitude').value = e.latLng.lng();
        infowindow.open(map, marker);
    });
}