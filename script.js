function iniciarMap() {
    var coord = { lat: -33.0106349, lng: -71.5485294 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 25,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}