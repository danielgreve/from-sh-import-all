#! /usr/bin/env python

from os import chdir, environ, getenv, listdir, pathsep, system
import sh

path_blacklist = ["", "/sbin", "/usr/sbin"]

path = [
    directory
    for directory in environ["PATH"].split(pathsep)
    if directory not in path_blacklist]

path_contents = [
    executable
    for directory in path
    for executable in listdir(directory)]

executables_blacklist = ["hy" "sh"]

executables = [
    executable
    for executable in path_contents
    if executable not in executables_blacklist]

resolvable_executables = [
    executable.replace("-","_")
    for executable in executables
    if "." not in executable]

for executable in resolvable_executables:
    locals()[executable] = getattr(sh, executable)

def cd(path=environ["HOME"]):
    chdir(path)

def editor(filename):
    system(environ.get("EDITOR", "nano") + " " + filename)

ls = ls.bake("-F")

la = ls.bake("-a", "-F")

ll = ls.bake("-l")

