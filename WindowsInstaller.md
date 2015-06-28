I built the source code using Microsoft Visual Studio 2008 Express ( which is free to use ).
I had to download VTK and CMake and learn how to use CMake.
It also needed wxWidgets.
I made the installation using Inno Setup 5.

I had to fix a couple of build errors ( probably because it was orignally made in another version of Visual Studio ).

It works, but you can't rotate the view ( some errors appear ).

If you do things in the wrong order it crashes.

The only thing I know that works, for sure is
1. run freesteel
2. menu File->Open file
3. open "mm.stl", you see it colored in orange
4. menu Machining->Core Roughing. OK the dialog.
5. menu Replay->Toolpath 0.   so it is ticked.
6. drag the slider along to the end. The toolpath should appear.


![http://3.bp.blogspot.com/_lpgMldGi1O4/SWIS5rd4NLI/AAAAAAAAAD4/t9L7BtqGxMg/s1600/freesteel.png](http://3.bp.blogspot.com/_lpgMldGi1O4/SWIS5rd4NLI/AAAAAAAAAD4/t9L7BtqGxMg/s1600/freesteel.png)

Dan Heeks.