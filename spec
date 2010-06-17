API Key: bf57a984d7e6f7e8330a4872bdb9a806
Secret: 9a1e716f1a4b19454009e976f7da7843

Libraries (add as needed but try to keep the list small):
	httplib (python http library) http://docs.python.org/library/httplib.html
	re (python regular expressions library) http://docs.python.org/howto/regex.html
	pyQT4 (GUI toolkit) http://zetcode.com/tutorials/pyqt4/introduction/
	os and/or sys (system commands like copy)
	id3-py (id3 tags)
	python-gpod (iPod support)
	python-sqlite2 (Python support for sqlite3 for storage/speed of the user's local library)

Main Files: (add 
	last.py: handle connections to last.fm and generate top albums.
		Format: ./last.py [username] [timeperiod]
		username is the user whose albums should be returned.	
		timeperiod is the period to look at (7 days - Overall)
	backfreshpod.py
		Backend. Handle requests from the GUI.
	freshpod.py
		GUI code.

