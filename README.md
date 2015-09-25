# unotify

Very simple notification CLI tool.

As for now it supports telegram, xmpp and screen notifications.
`unotify` script is just a wrapper around other scripts that actually send notifications.

## Configuration
Each script expects its own command line arguments beside original notification text.
That's why `unotify` reads these arguments from config file, `${HOME}/.config/unotify/unotify.conf` by default.
This file must consist of lines in the following format: `<notification-type>:<argument>=<value>`.
For example, `xmpp:to=myjabberid@sexyjabber.com`. The list of arguments for each notification type you can find
by reading help of selected script or here.

## Features

### telegram
Telegram notification uses your own [Telegram Bot](https://core.telegram.org/bots) and Telegram Bot API.
So it requires bot token id to be entered as an argument. New bot (and its token id) can always
be requested using [telegram internal bot](https://core.telegram.org/bots#3-how-do-i-create-a-bot).
You can check your bot token id using `-c|--check` argument, 
i.e. `python telegram-notifier.py -u <token> -t 0 -m 0 -c`.
Since you know your bot token id, you must determine user id (or chat id) who is supposed to receive notifications.
As long as telegram bots can not initiate new chats with users, you must start new chat with your bot. That sends
an incoming action for your bot that you can read using `-p|--print-updates` argument, 
i.e. `python telegram-notifier.py -u <token> -t 0 -m 0 -p`. The output of this command shows you all recent 
incoming events where you can find your user's (receiver, who initiated this chat) name and user's id.
Now, you are ready to test telgram notification by sending some text,
i.e. `python telegram-notifier.py -u <token> -t <user_id> -m TEST`.

### xmpp
You must set up JabberID and password of account that will send notifications. 
For setting the password you must use `-u|--user` and `-p|--password` arguments 
(note that user_id must be valid JabberID in the form of `<username>@<domain>`),
i.e. `python xmpp-notifier.py -u <user_id> -t 0 -m 0 -c`. This command will prompt you to type your password.
Passwords are stored by python.keyring, so ideally it will use your local OS keychain storage.
Test your xmpp notifier by executing `python xmpp-notifier -u <sender_user_id> -t <receiver_user_id> -m TEST`.

### screen
Screen notifications do not need to be preconfigured. You can use `./screen-notifier.sh -c` to check 
what notification services will be used internally. Execute `./screen-notifier.sh -m TEST` to test
screen notifications.

### unotify
As it was already mentioned, `unotify` command just provides quick access to the other notifiers.
After writing config file with proper arguments to selected notifiers, you can use these notifiers by passing
`-t` flag for telegram, `-x` flag for xmpp and `-s` for screen notifier. You can set more than one notifier, 
i.e. `./unotify -ts -m Hello` will send "Hello" message to telegram 
(according to the token id and receiver id that are written in the config file) and show "Hello"
notification on the screen.

### Note
It can be helpful to shorten command by using bash aliases. For example, if you set an alias for 
`alias un='${MYPATH}/unotify -ts -m " $(history 1) -> $?"'` then `any_command ; un` will notify you
when comman is done providing you command string and exit code.

## Requirements
* python `requests` package for telegram
* python `xmpp` and `keyring` packages for xmpp
