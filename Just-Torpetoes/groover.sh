#!/bin/bash
REL="../bash_pipe/"
if [ -z "$1" ]; then
  echo "what challenge are you grooving?"
  read TITLE
  echo "Groovy!"
else
  TITLE="$1" 
fi

if [ -z "$2" ]; then
  echo "what is your command for $TITLE"
  read COMMD
else
    COMMD="$2"
fi

if [ $COMMD == "--init" ]; then
  bash $REL"init.sh" $TITLE

elif [ $COMMD == "--case" ]; then
  if [ -z "$3" ]; then
    bash $REL"case.sh" $TITLE
  else
    bash $REL"case.sh" $TITLE $3
  fi
elif [ $COMMD == "--test" ]; then
  if [ -z "$3" ]; then
    bash $REL"test.sh" $TITLE
  else
    bash $REL"test.sh" $TITLE $3
  fi
elif [ $COMMD == "--submitted" ]; then
  if [ -z "$3" ]; then
    bash $REL"submitted.sh" $TITLE
  else
    bash $REL"submitted.sh" $TITLE $3
  fi
else
  echo "Invalid Command"
fi

