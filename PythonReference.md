index numbers start at zero and go up to and including n-1



### error = makerough('cone.stl') ###
This calculates the toolpath for the given .stl file. You might want to change some of the parameters with the set...  functions below, before calling this.
Returns 0, if succesful.
Then you can call the get.. functions below, see http://code.google.com/p/libactp/source/browse/trunk/PythonLib/sample.py for an example

### n = getnumpaths() ###
Returns the number of paths in the toolpath.

### n = getnumpoints(path\_index) ###
Returns the number of points in a given path, first path is 0.

### z = getz(path\_index) ###
Returns the z height of the given path.

### x, y = getpoint(path\_index, point\_index) ###
Returns the x and y coordinates of the given point of the given path.

### n = getnumbreaks(path\_index) ###
Returns the number of breaks in the given path.

### b = getbreak(path\_index, break\_index) ###
Returns the position of the given break in the given path

### n = getnumlinkpths(path\_index) ###
Returns the number of link paths in a given path

### n = getnumlinkpoints(path\_index, link\_index) ###
Returns the number of points in a given link path of a given path

### x, y, z = getlinkpoint(path\_index, link\_index, point\_index) ###
Returns the x, y and z coordinates of a given link point of a given link path of a given path

### setleadoffdz(value\_in\_mm) ###
default value is 0.1

### setleadofflen(value\_in\_mm) ###
default value is 1.1

### setleadoffrad(value\_in\_mm) ###
default value is 2.0

### setretractzheight(value\_in\_mm) ###
default value is 20.0

### setleadoffsamplestep(value\_in\_mm) ###
default value is 0.6

### settoolcornerrad(value\_in\_mm) ###
The corner radius of the tool.
default value is 3.0

### settoolflatrad(value\_in\_mm) ###
The radius of the flat part of the tool ( 0 for a ball nose tool )
default value is 0.0

### setsamplestep(value\_in\_mm) ###
default value is 0.4

### setstepdown(value\_in\_mm) ###
default value is 5.0

### setclearcuspheight(value\_in\_mm) ###
default value is 1.67

### settriangleweaveres(value\_in\_mm) ###
default value is 0.51

### setflatradweaveres(value\_in\_mm) ###
default value is 0.71

### setdchangright(value\_in\_mm) ###
default value is 0.17

### setdchangrightoncontour(value\_in\_mm) ###
default value is 0.37

### setdchangleft(value\_in\_mm) ###
default value is -0.41

### setdchangefreespace(value\_in\_mm) ###
default value is -0.6

### setsidecutdisplch(value\_in\_mm) ###
default value is 0.0

### setfcut(value) ###
default value is 1000

### setfretract(value) ###
default value is 5000

### setthintol(value\_in\_mm) ###
default value is 0.0001

### setstartpoint(x, y, vx, vy) ###
The start point and direction.
If not set, then the top left is used.

### setminz(z) ###
default value is -10000000.0

### boundaryclear(z) ###

### boundaryadd(x, y) ###

### boundarybreak() ###

### resetdefaults() ###