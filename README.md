# Minecraft Facts Twitter Bot - Fact Sharing

This is a Twitter bot that shares interesting facts about Minecraft on an hourly basis. The bot uses OpenAI GPT-3.5 to generate the facts, and is written in Python.

## Installation

1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Create a Twitter API key and access tokens from the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).
4. Create a `.env` file in the project directory
5. Run the bot using `python main.py`.

## Usage

The bot is set up to share a new Minecraft fact every hour. (Wait time is hardcoded in main.py)

You can also modify the `generateFact()` function in `ai.py` to change the way facts are generated. By default, the bot uses OpenAI GPT-3.5 to generate the facts, but you can use any method you like to generate your own facts.

## Contributing

If you find a bug or have a suggestion for a new feature, please open an issue and we'll be happy to help. If you want to contribute code, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.


## Warning

The `snscrape` library used in this project has been known to be blocked by Twitter in the past. Use of `snscrape` in this project may be against Twitter's terms of service. Use at your own risk.
We are using it with alt accounts and with 5 minutes delay between tweets, so we are not worried about it. <br>
Also, we changed the code of snscrape to make it work with the new Twitter API,
Check out `snscrape/NOTE.md` for more information.