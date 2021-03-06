# Timx
A minimal timer made with Qt Designer and Python using PyQt framework.  

![alt tag](https://github.com/subtleseeker/Timx/blob/master/ss.png) 

The timer is made to fulfill the needs of a competitive coder, so that he can keep up with the number of questions attempted,  the time elapsed and also add some time if needed.  

### Features
* Keep track of number of questions completed with automatically adding the time of completion to the notes.
* Keep up with the elapsed time.
* Timer which can be incremented if you need more time to complete the question.
* Embedded notepad to remember anything which comes to mind.

### How to use?
* Install pyqt framework with:  
`sudo apt install python-qt4`
* Install `python2`, `pygame` with:  
`sudo pip install python2 pygame`
* Then run the timer with:  
`python2.7 timx.py`
* **BONUS:** You can even set an alias by adding this in your `.bashrc` or `.zshrc`:  
`alias -g timx="python2.7 ~/Desktop/Timx/timx.py & disown; exit"`  
After which you can run the timer with just `timx`.
