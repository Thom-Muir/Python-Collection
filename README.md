# Python script collection
This repository contains a collection of Python scripts I’ve created—either to assist with other projects or as coding exercises to explore different automation and programming concepts.

## Scripts included
### simpleHTTP.py 
- A lightweight script that temporarily hosts a directory on an HTTP server. Users can specify the port number and directory as arguments.
- Libraries: http.server, socketserver, sys, os
- Useage
```bash
python3 simpleHTTP.py <port> [/path/to/directory]
```

### library.py
- A mock library inventory system that allows users to add, view, search, and remove books from a CSV file. Showcases object-oriented programming (OOP) principles.
- Libraries: csv, os.path, pathlib
- Useage
```bash
python3 library.py
```

### fileSorter.py
- An automation script that sorts files in a given directory into categorized folders based on their file types. The file types and categories are defined in a JSON configuration file.
- Libraries: shutil, os, time, json
- Useage:
```bash
python3 fileSorter.py
```

### uptimeChecker.py
- Automatically checks the status of websites listed in a JSON file. If a site is unresponsive, it prints an alert and records the site’s uptime statistics in a CSV file.
- Libraries: requests, json, time, pandas
```bash
python3 uptimeChecker.py
```

## Prerequisites  
These scripts require Python 3 and the corresponding built-in or external libraries.
