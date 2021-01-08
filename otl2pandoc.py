#!/usr/bin/env python
import sys

def count_indent(line):
    """ Determine the section level """
    count = 1
    for character in line:
        if character == "\t":
            count += 1
        else:
            return count

def otl2markdown(argv):
    """ Convert text from otl to Markdown """
    otlfile = open(argv[1], 'r').readlines()
    outputlines = []
    for line in otlfile:
        if line == '\n':
            pass
        elif line.strip().startswith(':'):
            outputlines.append(line.strip()[2:])
        elif line.strip().startswith(';'):
            outputlines.append(line.strip()[2:])
        elif line.strip().startswith('%'):
            outputlines.append(line.strip())
        elif line.strip().startswith('+'):
            outputlines.append(line.strip())
        elif line.strip().startswith('|'):
            outputlines.append(line.strip())
        elif line.strip().startswith('>'):
            outputlines.append("\t%s" % (line.strip()[2:]))
        elif line.strip().startswith('<'):
            outputlines.append("\t%s" % (line.strip()[2:]))
        elif line.strip().startswith('['):
            cline = line.replace("[_]","[ ]")
            if count_indent(line) == 1:
                outputlines.append("+ %s" % (cline.strip()))
            else:
                cblevel = (count_indent(line)-1) * '\t'
                outputlines.append("%s+ %s" % (cblevel, cline.strip()))
        else:
            heading = count_indent(line) * '#'
            outputlines.append("\n%s %s\n" % (heading, line.strip()))
    return "\n".join(outputlines)

if __name__ == '__main__': 
    try:
        print(otl2markdown(sys.argv))
    except:
        print('Usage: o2p.py [FILENAME]')
        sys.exit(1)
