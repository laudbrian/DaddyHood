var map;
var directionsDisplay;
var directionsService = new google.maps.DirectionsService();
var currentLat;
var currentLng


$(document).ready(function() {
    getMap();
    

    $('.save_event').on('click', function() {
        if ($(this).hasClass('green') == true) {
            $.ajax({
                type: 'POST',
                url: '/save-event',
                data: {
                    'event_id': $(this).attr('id')
                },
                success: function(data) {}
            });
            $(this).removeClass('green');
            $(this).addClass('blue');
            $(this).html('<img id="check-mark" src="/static/img/check.png" />Added!');
        }
    });
}); 


// ------------------------------------------------------------------ //
//                           Google Maps                              //
// ------------------------------------------------------------------ //
function getMap() {
//    console.log('GET THE MAP')
    if(navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(makeMap);
    } else {
        // No GEO location
    }
}


function makeMap(position) {
//    console.log('make the map');
    currentLatLng = position;
    currentLat = position.coords.latitude;
    currentLng = position.coords.longitude;

    directionsDisplay = new google.maps.DirectionsRenderer();

    var mapOptions = {
        center: new google.maps.LatLng(currentLat, currentLng),
        zoom: 16,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(
        document.getElementById("map"),
        mapOptions
    );

    directionsDisplay.setMap(map);
    directionsDisplay.setPanel(document.getElementById('directions'));

    var infowindow = new google.maps.InfoWindow({
        content: 'Current Location'
    });

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(currentLat,currentLng),
        map: map,
        title: 'Current Location'
    });

    // google.maps.event.addListener(marker, 'click', function() {
    //     infowindow.open(map, marker);
    // });
 
}

function makeMarker(lat, lng) {
//    console.log(lat + ' - ' + lng);
//    console.log('inside marker');

    // var infowindow = new google.maps.InfoWindow({
    //     content: title
    // });

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(lat, lng),
        draggable: false,
        // title: title,
        map: map
    });
    // google.maps.event.addListener(marker, 'click', function() {
    //     infowindow.open(map, marker);
    // });
}


// ------------------------------------------------------------------ //
//                           Google Directions                        //
// ------------------------------------------------------------------ //

function getDirections() {
//    console.log('directions');
    var start = new google.maps.LatLng(currentLat, currentLng);
    var end =  new google.maps.LatLng(daddyObj.fields.lat, daddyObj.fields.lng);

    var request = {
        origin: start,
        destination: end,
        travelMode: google.maps.TravelMode.DRIVING
    };
    directionsService.route(request, function(response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}
