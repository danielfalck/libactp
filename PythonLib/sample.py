import actp
fout = open("test.tap", 'wb')

actp.makerough('cone.stl')

npaths = actp.getnumpaths()
for path in range(0, npaths):
    npoints = actp.getnumpoints(path)
    nbreaks = actp.getnumbreaks(path)
    nlinkpaths = actp.getnumlinkpths(path)
    z = actp.getz(path)
    start_pos = 0
    first_z_done = False
    for brk in range(0, nbreaks):
        brkpos = actp.getbreak(path, brk)
        for point in range(start_pos, brkpos):
            x, y = actp.getpoint(path, point)
            #feed(x, y, z)
            if first_z_done == False:
                fout.write("G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n")
                first_z_done = True
            else:
                fout.write("G1 X" + str(x) + " Y" + str(y) + "\n")
        start_pos = brkpos
        nlinkpoints = actp.getnumlinkpoints(path, brk)
        for linkpoint in range(0, nlinkpoints):
            x, y, z = actp.getlinkpoint(path, brk, linkpoint)
            #rapid(x, y, z)
            fout.write("G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + "\n")
