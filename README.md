# AutoPatcher_IG
AutoPatcher_IG

Created on Tue Dec 13 14:01:28 2011

License: GPL version 3.0  

January 25, 2016  

Copyright:  

	This file is part of AutoPatcher_IG.

    AutoPatcher_IG is a free to be used in non-profit organizations for non-commercial purposes: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    AutoPatcher_IG is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with AutoPatcher_IG.  If not, see <http://www.gnu.org/licenses/>.

Hardware Componenet requirements: 
--------------------------------------------------------
	(What is used in developing is listed in parenthesis)
	- Windows desktop ready to be used (i7 processor/12g RAM/ 2TB hard drive)
	- Manipulator Unit X 2(Scientifica PatchStar Manipulator)
	- Microscope (Scientifica Slicescope)
	- Digitizer (Molecular Devices Digidata 1550A Digitizer)
	- Amplifier (Molecular Devices Axon Digidata 1550B)
	- Data Acquisition Board (Measurement Computing USB-1208FS. Welcome to send email for detail)
	- Pressure Control Unit (Homemade. Saved as Circuit_board_set_up.jpg in the folder)

Software Component requirements: 
--------------------------------------------------------
(What is used in developing is listed in parenthesis)
	**It is recommanded to set up the environment according to parenthesis. Installing only the listed feature might not be working due to compatibility**

	Device Driver: 
	
	- Manipulator Unit Driver(Scientifica PatchStar Manipulator)
	- Microscope Driver(Scientifica Slicescope)
	- Camera Driver(ThorlabsDCx_camera software package)
	- Digitizer Driver(Molecular Devices Digidata 1550 Digitizer)
	- Amplifier Driver(Molecular Devices Axon CNS MultiClamp 700B)
	- Data Acquisition Board Driver(Universal Library. Welcome to send email for detail)

	Desktop Software & environments:
	
	- Windows 7 or higher (Windows 7. 64 bit)
	- Anaconda (Python 2.7. 32 bit)
	- Commandline Bash Simulation (Git bash)
	- Some Python libraries: (One source of the website to download: http://www.lfd.uci.edu/~gohlke/pythonlibs/)
		- OpenCV
		- Qimaging (64 bit driver)

	
To Get Started (with recommended setting):
--------------------------------------------------------
0. Make sure that you have a windows 7 (or higher) 64 bit computer

1. Make sure that you have the hardware device as listed set up (and the driver installed)

2. Install Anaconda (32bit, Python 2.7)

3. Install Git Bash (64bit, Windows)

4. Update pip package by:
	- Open a git bash window
	- Enter "pip install --upgrade pip"
	- Wait for program to finish

5. Go to website: (http://www.lfd.uci.edu/~gohlke/pythonlibs)
	- Install OpenCV (for python 2.4, 32bit)

To Run the Program:
--------------------------------------------------------
0. Open a git bash window, make sure you have turned on all device

1. Move to the target directory by using 
		"cd [path to file folder]"

2. Open the manipulator driver that comes with the manipulator

3. Run the entire program by typing
		"python Autopatcher_IG.py"

3. (If you are only insterested in using the patching functionability)
	Run the program by typing
		"python autopatcher.py"











--------------------------------------------------------
Udpating installation details:
1. Save the port data in configuration/port.csv [port, device(sci in our case), number(always be 1)]
		or 
	Use confiuration.py
2. Current running version:
	python 2.7.12
	Anaconda 4.1.1 (32bit)
