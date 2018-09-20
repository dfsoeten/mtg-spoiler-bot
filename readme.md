# MTG Spoiler Bot
This nifty "little" python application will scrape the newest spoilers from [Mythic Spoiler](http://mythicspoiler.com/) 
and caches the data into `.json` files. Images will be saved into aswell!

In the future this application will be able to be linked with [Whatsapp web](https://web.whatsapp.com/) and atuomatically send the newest spoilers inside your groups app!

## Getting Started
Clone this repo: `git clone https://github.com/iamdann/mtg-spoiler-bot.git`
Run it with **python 3**: `pyton3 main.py`


## Options
| Option           | Values    | Description                                                             |
|------------------|-----------|-------------------------------------------------------------------------|
| domain           | [url]     | Domain of mythicspoiler.com, probably don't wanna touch this            |
| new-sets-url     | [url]     | Newest sets on mythicspoiler, probably don't wanna touch this either    |
| silent           | [boolean] | Turns all output on or of                                               |
| debug is-enabled | [boolean] | Turns on debug messages when an exception is thrown while scraping data |
| debug card-index | [int]     | Index of the to debug card in a set                                     |

## Pretty Printing
Can pretty print magic cards!

![pretty print example](pretty-print-example.jpeg)

## Todo
- Link [Whatsapp web](https://web.whatsapp.com/) with selenium.
- Check periodically for newest spoilers
- Add `is_new()` method to cards 