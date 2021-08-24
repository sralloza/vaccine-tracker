# Simple Vaccine tracker

A python script that will parse vaccine anouncements from Castilla y León (Spain) and will notify the user.

**Note**: parsed links are stored in a S3 bucket. You must create the bucket first, then run the script.

## Environment variables

- `BOT_TOKEN`: the telegram bot's token to send notifications from.
- `ADMIN_ID`: the admin's telegram ID. The notifications will be sent to this telegram ID.
- `OTHER_IDS`: (optional) other users telegram IDs. Useful to send notifications to multiple users.
- `AWS_ACCESS_KEY_ID`: AWS credentials.
- `AWS_SECRET_ACCESS_KEY`: AWS credentials.
- `FILTER_KEYWORD`: (optional) simple word filter to apply to announcements titles. Designed to be a city name. It will be lowercased.
- `S3_BUCKET`: AWS S3 bucket used to store the parsed links.

## Docker comands

```shell
# Build
docker build -t vaccine-tracker .

# Run (Production)
docker run --rm --env-file .env vaccine-tracker

# Run (development, windows)
docker run --rm -e AWS_ACCESS_KEY_ID=%AWS_ACCESS_KEY_ID% -e AWS_SECRET_ACCESS_KEY=%AWS_SECRET_ACCESS_KEY% --env-file .env vaccine-tracker
```

The .env file has to look like this:

```env
BOT_TOKEN=xxxxxxx
ADMIN_ID=xxxxxx
OTHER_IDS=[xxxxxx, xxxxxx]
AWS_ACCESS_KEY_ID=xxxxxxxxx
AWS_SECRET_ACCESS_KEY=xxxxxxxxxxx
S3_BUCKET=xxxxxx
FILTER_KEYWORD=xxxx
```
