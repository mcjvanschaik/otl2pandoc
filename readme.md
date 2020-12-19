
# otl2pandoc.py

otl2pandoc.py is a simple python script to convert Vimoutliner files to
Pandoc markdown.

In the test.otl file you can find examples for the supported syntax and
how to make use of the special features like tables and verbatim text.


## Usage

To print to stdout call the script followed by the name of the otl-file
you wish to convert.

	otl2pandoc.py [filename]

Typically you would like to pipe the output of the script to Pandoc to
convert the document to a different format. For example to create a pdf
called otl.pdf:

	otl2pandoc.py [filename] | pandoc -o otl.pdf

In order to convert to markdown as a file, you can direct the output to a
file. For example to create this readme file use:

	otl2pandoc.py readme.otl > readme.md

