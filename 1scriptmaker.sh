#!/bin/bash
#-------------


#Gather name from execution:   ./1scriptmaker.sh script.sh
scriptname="$1"
#--------------------------------------
# Create the intended script
touch $1
#-------------------------------------
# Make it executable
chmod +x $1
#--------------------------------------
# Add the first two lines
echo "#!/bin/bash" >> $1
echo "#------------------------------------------" >> $1
echo "#---Made by:   ./1scriptmaker.sh" >> $1
echo "#---This is:   $1" >> $1
echo "#------------------------------------------" >> $1
#--------------------------------------
# Open it with nano to then work on it
nano $1
