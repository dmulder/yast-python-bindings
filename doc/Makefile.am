#
# Makefile.am for python-bindings/doc
#

txtdir = $(docdir)

yast.html:
	pydoc3 -w $(srcdir)/../src/yast.py

ycpbuiltins.html:
	pydoc3 -w $(srcdir)/../src/ycpbuiltins.py

txt_DATA = yast.html ycpbuiltins.html

EXTRA_DIST = $(txt_DATA)
CLEANFILES = $(txt_DATA)
