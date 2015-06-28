To build the Python module:

In Windows, open libactp/PythonLib/actp.vcproj in Visual Studio 2008 ( I use VS2008 Express ). Press build. It will make libactp/PythonLib/actp.pyd, which is a Python module

In "Windows Explorer" go to libactp/PythonLib and double-click on sample.py, it should make a test.tap file.

Have a look at sample.py, to see the Python script.




In Ubuntu, open terminal

type:
cd /Desktop/libactp/PythonLib
( depending where you have checked-out the source code to )

type:
make

it will make libactp/PythonLib/actp.so, which is a Python module

type:
python sample.py

It should have made a "test.tap" file.