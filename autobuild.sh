while true;
do
  inotifywait -e close_write -r ./rst conf.py *.rst *.bib *.py
  make latexpdf
done
