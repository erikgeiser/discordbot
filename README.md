# discordbot
A modular bot for the free voice/text messaging software Discord, written for Python 3.

# Dependencies
To run discordbot you need the following packages for Python 3:

* discord.py - API for Discord ([info for contributors](https://github.com/Rapptz/discord.py))
  * `pip install discord.py`
* praw - API for the Reddit module
  * `pip install praw`
* urbandict - API for the Urban Dictionary module
  * `pip install urbandict`
* wolframalpha - API for the Wolfram Alpha moudle
  * `pip install wolframalpha`

Python 2.x may work but is neither supported nor tested.

# Usage
Start the bot via `python3 discordbot.py`.

On startup you will be asked for the Discord login credentials as well as for your Wolfram Alpha API Key. You can also specify these details if you create a file called `.login` in the discordbot folder with the following content:
```
mail mailadress@domain.com
pw yourpassword
waapi yourwolframalphaapikey
```
Some commands are restricted for the common user. You can add the Discord IDs of the users that are authorized to do administrative tasks in a file called `.auth` so that they can execute said commands.

Custom commands can be created by creating a file called `.commands` in the discordbot directory. The commands are defined like this:
```
!greet Welcome
!2liner This is a response
!2liner on two lines!
...
```
You can also create custom responses to keywords by creating a file called `.keywords`. In the following example of `.keywords` the bot will post "Now I'm hungry" everytime someone posts a message containing the word food (note that keywords are not case sensitive):
```
food Now I'm hungry
```

# Commands
* **Redit module**
  * `!r subreddit`: Get the top 5 submission from the subreddit's hot page
  * `!csgo`: Shortcut for /r/globaloffensive
  * `!tfts`: Shortcut for /r/talesfromtechsupport
* **Urbandictionary module**
  * `!def word`: Gets the top definition/example of the word from Urbandictionary
  * `!def word n`: n specifies the number of definitions that will be shown
* **Wolfram Alpha module**
  * `!wa query`: Returns the results for the given query from Wolfram Alpha
* **Respond module**
  * `!id`: Prints your ID
  * `!host`/`!where`: Prints out the bot's hostname
  * Custom commands from .response file
* **Admin module** *(restricted if ID is not in .auth)*:
  * `!! rename newname`: Changes bot name to "newname"
  * `!! authid id`: Adds "id" to the `.auth` file

# To do list
* Improve code documentation
* Add additional modules and improve existing ones
* Load modules dynamically (maybe autodetect new modules, *might be out of scope though*)
