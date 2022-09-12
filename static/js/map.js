function initMap(){

    // {% for station in stations %}
    //     locations.push({name: {{ station.name }}, latlng: new google.maps.LatLng({{ station.lat }}, {{ station.lng }}) });
    //     //var uluru = { lat: {{ station.lat }}, lng: {{ station.lng }} };
    // {% endfor %}
    
    var options = {
        zoom:12,
        center:{lat:40.7306,lng:-73.9352}
    }
    console.log(station[0].name)
    const map=new google.maps.Map(document.getElementById('map'),options);
    var marker;
    for(var j=0; j<locations.length; j++){
        marker=new google.maps.Marker({
            position:locations[j].latlng,
            map,
            title:locations[j].name,
        })
        var infowindow = new google.maps.InfoWindow({
            content: locations[j].name,
        });
        google.maps.event.addListener(marker, 'click', (function(marker, j) {
            return function() {
                infowindow.setContent(locations[j].name);
                infowindow.open(map, marker);
            }
       })(marker, j));
    }
}