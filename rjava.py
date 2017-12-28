#!/usr/bin/python3

import sys
import subprocess

def main():
    '''
        Entry point to script.  Finds a *.java file, compiles, and executes the class.
    '''
    javaPath = None
    classPath = None
    fileName = sys.argv[1]

    javaPath = findJavaFilePath(fileName)
   
    classPath = findClassFilePath(javaPath)

    compileFile(classPath, javaPath)

    runFile(classPath, javaPath)


def findJavaFilePath(fileName):
    '''
        Finds the file within the eclipse-workspace directory.

        Returns the filepath for the *.java file.
    '''

    javaFilePath = subprocess.check_output(["find", "/home/nolan/Documents"+
    "/eclipse-workspace", "-name", fileName])

    # Clean-up output
    javaFilePath = javaFilePath.decode("utf-8")
    javaFilePath = javaFilePath.rstrip()

    return javaFilePath

def findClassFilePath(path):
    '''
        Finds the filepath for the compiled .java files.

        Returns the filepath for the *.class file.
    '''
    javaPath = path
    index = javaPath.find("src")
    classPath = javaPath[0:index]
    classPath = classPath + "bin"
    
    return classPath

def compileFile(classPath, javaPath):
    '''
        Compiles the *.java file and places the generated file in the correct directory.
    '''
    arg0 = "javac"
    arg1 = "-cp"
    arg2 = "/home/nolan/Documents/eclipse-workspace/*:/home/nolan/Documents/jar-files/*"
    arg3 = "-d"
    arg4 = classPath
    arg5 = javaPath
    subprocess.call([arg0, arg1, arg2, arg3, arg4, arg5])

def runFile(classPath, javaPath):
    '''
        Runs the *.class file.
    '''
    index = javaPath.find("src") + 4
    execStr = javaPath[index:]
    index = execStr.find(".java")
    execStr = execStr[:index]
    execStr = execStr.replace('/','.')

    subprocess.call(['java', execStr], cwd=classPath)


if __name__ == "__main__":
    main()
