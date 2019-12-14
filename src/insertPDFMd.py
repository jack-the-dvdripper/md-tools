def includepdf(filename, filelength):
	f = open("mdScriptWherePDFShouldBeInserted.md", "a")
	for i in range(1,filelength+1):
		f.write("\includegraphics[page=%d,width=\paperwidth]{%s}\n\n#\n\n" % (i, filename))
	f.close()
	print("Insertet PDF-File: %s" % filename)

includepdf("testfile.pdf", 10)