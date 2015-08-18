# Monitor your WebAfrica data cap

I got tired of runnng out of WebAfrica ADSL data every month. Their website is great, but logging in to it is a bit of a pain and I'm very lazy.

So this little script logs in for me and scrapes the HTML for how much data I've used so far. As an added bonus it figures out what percentage of my data I've used in relation to how much of the month is through.

Nifty.

# Installation

```
pip install requests
pip install beautifulsoup4
```

# Configuration

```
cp settings.py.default settings.py
```

Edit settings.py with your credentials

# Run

```
python webafrica.py
```


