# PrettyLogger

PrettyLogger is a simple modular python logger, primarily made for easy implementation in web scraping and automated checkout scripts.

## Usage

```python
from prettylogger import Logger

# Instantiates the logger
log = Logger(site="Amazon AU")

# Example usage for logging
self.captcha("HCaptcha")
self.error("Proxy Ban")
self.info("Loading profiles")
self.check("Product Name")
self.success("Product Name", "Profile 1")
self.stock("Product Name")
```
![Example](/assets/images/example.png)

## Contributing
As I use this for my own projects, it may not be best suited for every use case. If you have any ideas, just open an issue and tell me what you think.

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are welcomed.

## License
[MIT](https://choosealicense.com/licenses/mit/)