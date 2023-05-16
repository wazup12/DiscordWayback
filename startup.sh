if [[ "$VIRTUAL_ENV" != "bot-env" ]]
then
	source bot-env/bin/activate
fi
python3 bot.py
