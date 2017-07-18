import sys
import os

# Takes the csv file name and creates a .sql file with the name of
# "{basename}-build.sql"

def populateBuildScript(directory, csvFileName) :
    print csvFileName
    basename = csvFileName.replace(".csv", "")
    basename1 = "`" + basename + "`"
    buildName = directory + "-build-" + basename + ".sql"
    print buildName

# opens csvFile for reading and the build file for writing
    csvfile = open(csvFileName, "r")
    buildFile = open(buildName, "w")

# these lines are for the specific files i was working with
# they were formatted differently and may not be needed for your files
    value = csvfile.readline().strip()
    value = value.replace(",", ", ")


    for line in csvfile.readlines() :
        line = line.strip()
        line = line.replace(",", ", ")

        #creates INSERT statements for a table with the same name as {basename}
        if line != "" :
            command = "INSERT INTO " + basename1 + " VALUES(" + line + " );\n"
            buildFile.write(command)

    buildFile.write("\n")
    buildFile.close()
    csvfile.close()
    return

cwd = os.getcwd()
dir = sys.argv[1]
os.chdir(dir)

print "\n" + os.getcwd()


for f in os.listdir(os.getcwd()) :
    if f.__contains__(".csv") :
        populateBuildScript(dir, f)
