import zipfile
zfile=zipfile.ZipFile("evil.zip")
try:
	zfile.extractall(pwd="secret")
except Exception as e:
	print(type(e))    # the exception instance
	print(e.args)     # arguments stored in .args
	print(e)          # __str__ allows args to be printed directly,
...                         # but may be overridden in exception subclasses
	
