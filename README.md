# PyTiles

PyTiles is a very simple python application that can serve map tiles according to geographical user data input.

It allows you to render map tiles on you application map using a private API.


## How it works

This is a standalone web app that responds to URLs of the form:
````
<tile_style>/<zoom>/<x>,<y>.png
````
Pytiles returns 255x255 images like:

![](http://pytiles.herokuapp.com/tile_example.png)

that can be placed over embeded Google Maps v3 through Google Maps API Custom Overlays. https://developers.google.com/maps/documentation/javascript/examples/overlay-simple


