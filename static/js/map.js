console.log(station.name);

function initMap(){
    var locations=[];
    //locations.push({name: {{ station.name }}, latlng: new google.maps.LatLng( {{ station.lat }}, {{ station.lng }}) });
    var options = {
        zoom:11,
        center:{lat:40.7306,lng:-73.9352}
    }

    var map=
    new google.maps.Map(document.getElementById('map'),options);
}