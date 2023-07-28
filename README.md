# Telegram-Analysis-Bot

Telegram-Analysis-Bot is a comprehensive Telegram bot designed to perform data analysis and visualization on advertising campaign data.

## Features

- **Interact with Bot**: Users can interact with the bot using specific commands, such as `/start`, `/help`, `/about`, `/summary`, and `/plot`.

- **Data Analysis**: The bot performs data analysis tasks on advertising campaign data, including calculations for total spent, total conversion, and cost per click (CPC) for specific campaigns.

- **Data Visualization**: Generates and provides visual plots showing the total spent, total approved conversion, and average CPC across age groups for specific campaigns.

- **Text Templating**: The bot uses text templates to structure responses to users.

## Setup

1. Clone the repository.

2. Install the necessary packages as listed in `requirements.txt` by running:
```bash
pip install -r requirements.txt
```

1. Set up the environment variables. The bot requires a Telegram Bot API token. Create a file named .env in the root directory of the project, and add your Telegram Bot API token to this file in the format TOKEN=<Your_Token_Here>.

1. Run the bot script:

```
python bot_local.py
```

## Usage
Interact with the bot in Telegram using the following commands:

* **`/start`** or **`/help`**: The bot will send a welcome message.
* **`/about`**: The bot will provide information about itself.
* **`/summary`**: The bot will ask for a campaign ID and provide a summary of the campaign.
* **`/plot`**: The bot will ask for a campaign ID and provide a plot of the campaign metrics.
