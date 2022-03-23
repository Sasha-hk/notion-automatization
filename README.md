# 📔 Notion automation

This is python automation script for Notion. The script runs on my server every minute.

## Installation

Requirements:

- python3.9

Run:

```sh
. ./setup.sh
```

Create an .env file with the following content:

```txt
TOKEN=<token>
DATABASE_ID=<id>
```

Put your token and database in the variables.

### Cron

The command above creates `run.sh` file that required for [Cron](https://en.wikipedia.org/wiki/Cron "Cron wiki").

Now open Cron:

```sh
crontab -e
```

and type this:

```sh
* * * * * <project dir>/run.sh
```

The line means that the file run.sh file will run every minute
