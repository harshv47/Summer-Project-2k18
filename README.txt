# Summer-Project-2k18
#Team Members:
1. Augustine Theodore Prince
2. Harsh Vardhan


This core idea of this project was concieved as a Summer Project as part of the larger RoboISM Expo of the year 2018.

That however doesn't limit this project and over time we came to the realisation that the full scope of this project requires a lot of work, more than previously assumed.

Thus, to facilitate smooth transfer of ideas and seamless coding we are using Github for the Software part of the project.


The instructions to follow:
#This text is taken from snowboy git.
Dependencies
To run the demo you will likely need the following, depending on which demo you use and what platform you are working with:

SoX (audio conversion)
PortAudio or PyAudio (audio capturing)
SWIG 3.0.10 or above (compiling Snowboy for different languages/platforms)
ATLAS or OpenBLAS (matrix computation)

You can find the exact commands you need to install the dependencies on Raspberry Pi below:

First apt-get install swig, sox, portaudio and its Python binding pyaudio:

sudo apt-get install swig3.0 python-pyaudio python3-pyaudio sox
pip install pyaudio
Then install the atlas matrix computing library:

sudo apt-get install libatlas-base-dev
Make sure that you can record audio with your microphone:

rec t.wav
If you need extra setup on your audio (especially on a Raspberry Pi), please see the full documentation (http://docs.kitt.ai/snowboy/)
You can read the documentation if you have any problem.

#Although compilation is not necessary but do it if you have some problem.
Compile a Python Wrapper
cd swig/Python
make
SWIG will generate a _snowboydetect.so file and a simple (but hard-to-read) python wrapper snowboydetect.py. We have provided a higher level python wrapper snowboydecoder.py on top of that.

Feel free to adapt the Makefile in swig/Python to your own system's setting if you cannot make it
