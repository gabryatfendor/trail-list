import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')

newTrail = open("trails/trail_%s.md" % (name), "w+")
newTrail.write("### %s" % (name))
newTrail.close()