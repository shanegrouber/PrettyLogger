from colorama import Fore, Style, init
from datetime import datetime
from threading import Lock
import json, os

class Logger:
    def __init__(self, site=""):
        init(autoreset=True)
        self.SITE = site
        self.LOCK = Lock()
        
    def setSite(self, newSite):
        self.SITE = newSite
        
    def getTime(self, longDate=False):
        if longDate:
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        return f"{Style.DIM}{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S.%f')[:-3]}{Style.RESET_ALL}"
    
    def getFillWords(self, type: str, **kwargs):
        reset = Style.RESET_ALL
        fStore = f"{Fore.CYAN}{Style.BRIGHT}{self.SITE.upper()}{reset}"
        fProduct = f"{Fore.MAGENTA}{Style.BRIGHT}{kwargs.get('product')}{reset}"
        fProfile = f"{Fore.YELLOW}{Style.BRIGHT}{kwargs.get('profile')}{reset}"
        fCaptcha = f"{Fore.RED}{Style.BRIGHT}{kwargs.get('captcha')}{reset}"
        
        match type.lower():
            case "check":
                return f"Checking: {fProduct} at {fStore}"
            case "info"|"error":
                return f"{kwargs.get('message')}"
            case "stock":
                return f"{fProduct} is in stock at {fStore}"
            case "success":
                return f"{fProduct} checked out at {fStore} with {fProfile}"
            case "captcha":
                return f"{fCaptcha} detected on {fStore}"
            
    def check(self, product):
        alertColour = f"{Fore.MAGENTA}{Style.BRIGHT}"
        message = self.getFillWords('check', product=product)
        formattedMessage = f"{alertColour}[CHECK] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
        
    def info(self, message):
        alertColour = f"{Fore.YELLOW}{Style.BRIGHT}"
        message = self.getFillWords('info', message=message)
        formattedMessage = f"{alertColour}[INFO] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
        
    def error(self, message):
        alertColour = f"{Fore.RED}{Style.BRIGHT}"
        message = self.getFillWords('error', message=message)
        formattedMessage = f"{alertColour}[ERROR] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
        
    def success(self, product, profile):
        alertColour = f"{Fore.GREEN}{Style.BRIGHT}"
        message = self.getFillWords('success', product=product, profile=profile)
        formattedMessage = f"{alertColour}[SUCCESS] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
        
    def stock(self, product):
        alertColour = f"{Fore.GREEN}{Style.BRIGHT}"
        message = self.getFillWords('stock', product=product)
        formattedMessage = f"{alertColour}[STOCK] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
        
    def captcha(self, captchaType):
        alertColour = f"{Fore.RED}{Style.BRIGHT}"
        message = self.getFillWords('captcha', captcha=captchaType)
        formattedMessage = f"{alertColour}[CAPTCHA] {self.getTime()} {message}"
        self.safePrint(formattedMessage)
    
    def writeToFile(self, message, product=None):
        if not os.path.isdir('logs'):
            os.mkdir('logs')
        writePath = f'logs/{self.SITE}.log'
        with open(writePath, 'a+') as f:
            f.write(f"{self.getTime(True)} \n{message}\n")
            if product and type(product) is dict:
                f.write(f"\nITEM_INFO: {json.dumps(product, sort_keys=True, indent=4)}\n")
            
        
    def safePrint(self, *args, **kwargs):
        with self.LOCK:
            print(*args, **kwargs)
            
    def __test__(self):
        self.captcha("HCaptcha")
        self.error("Proxy Ban")
        self.info("Loading profiles")
        self.check("Product Name")
        self.success("Product Name", "Profile 1")
        self.stock("Product Name")
    