BOT_NAME = "otodom"

SPIDER_MODULES = ["otodom.spiders"]
NEWSPIDER_MODULE = "otodom.spiders"

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEED_FORMAT = "csv"
FEED_URI = "results.csv"
