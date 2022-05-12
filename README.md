# RasaChatBot

Very simple chabot. Just for learning purposes.

To install rasa, use the command `pip3 install -U --user pip && pip3 install rasa`

You can also do `pip install rasa` but it is very slow for some reason.

Also install `rasa[spacy]` using `pip install rasa[spacy]` I dont know why we have to do it separately.

Once everything is ready first run the actions by using `rasa run actions`. It will run on 5055 port by default.

Then finally run the chatbot by using `rasa shell` or `rasa interactive` in case you want to annotate data.
