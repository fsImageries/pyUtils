# pyUtils
A little python helper library composed of mainly visual inspired functions and classes.
Mostly used in maya in use with these libraries,<br/>
[mayapyUtils](https://github.com/fsImageries/mayapyUtils.git)<br/>
[shaderHelper-maya](https://github.com/fsImageries/shaderHelper-maya.git)<br/>
etc...

<br/>
<br/>
<br/>
### INSTALLATION:
Only tested in OSX 11.4, Maya2020, python2.7.15. 

(You have to use sudo here because mayas site-packages is in a secured folder and
you also have to locate your mayapy executable, [help here](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2020/ENU/Maya-Scripting/files/GUID-83799297-C629-48A8-BCE4-061D3F275215-htm.html).)

#### Recommended approach (mayapy pip):
- open the terminal, CMD on win
 
- install from git:
-`sudo path/to/mayapy -m pip install git+https://github.com/fsImageries/<repo>.git`
    
    ##### or  


- download the git repo
  `cd into/repo`<br/>
  `sudo path/to/mayapy -m pip install path/to/repo`


#### Second approach (setup.py):
(Doesn't install dependencies at the moment, if anyone knows why pls let me know.)
  - download the git repo  
    `cd into/repo`  
    `sudo path/to/mayapy setup.py install`  

  
#### Third approach (copy files):
  - download the git repo
  - copy the package from src to a folder on your PYTHONPATH, preferably mayas site-packages  


#### Install in Maya
- open Maya and the script editor
- the following command will create a shelf button in the Custom shelf to open the GUI
- `from righelper.righelper import shelf`
- `shelf()`

  
  
### DEPENDENCIES:
  - [setuptools](https://pypi.org/project/setuptools/)
  - [mayapyUtils](https://github.com/fsImageries/mayapyUtils)
 


