#please run this file for best usage on linux 
sudo chmod +x terminote.py
sudo touch /usr/bin/terminote
CURRENT_DIR=$(pwd)
program_name="/terminote.py"
FILE_PATH="$CURRENT_DIR$program_name"
COMMAND="python $FILE_PATH"
echo $COMMAND | sudo tee /usr/bin/terminote > /dev/null
