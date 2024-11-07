from datetime import datetime
from colorama import Fore

class Logger:
    def __init__(self, prefix: str = "HSW-API") -> None:
        self.WHITE: str = "\u001b[37m"
        self.MAGENTA: str = "\033[38;5;97m"
        self.MAGENTAA: str = "\033[38;2;157;38;255m"
        self.RED: str = "\033[38;5;196m"
        self.GREEN: str = "\033[38;5;40m"
        self.YELLOW: str = "\033[38;5;220m"
        self.BLUE: str = "\033[38;5;21m"
        self.LIGHTBLUE = Fore.LIGHTBLUE_EX
        self.PINK: str = "\033[38;5;176m"
        self.CYAN: str = "\033[96m"
        self.prefix: str = f"{self.PINK}[{self.MAGENTAA}{prefix}{self.PINK}]"

    @staticmethod
    def get_time() -> str:
        return datetime.now().strftime("%H:%M:%S")

    def message(self, level: str, message: str) -> str:
        time_now = (f" {self.PINK}[{self.MAGENTAA}{self.get_time()}{self.PINK}] {self.WHITE}|")
        return f"  {self.prefix} {self.WHITE}|{time_now} {self.PINK}[{level}{self.PINK}] {self.WHITE}-> {self.PINK}[{self.MAGENTA}{message}{self.PINK}]"

    def success(self, message: str, level: str = "Success") -> None:
        print(self.message(f"{self.GREEN}{level}", f"{self.GREEN}{message}"))

    def warning(self, message: str, level: str = "Warning") -> None:
        print(self.message(f"{self.YELLOW}{level}", f"{self.YELLOW}{message}"))

    def info(self, message: str, level: str = "Info") -> None:
        print(self.message(f"{self.LIGHTBLUE}{level}", f"{self.LIGHTBLUE}{message}"))

    def failure(self, message: str, level: str = "Failure") -> None:
        print(self.message(f"{self.RED}{level}", f"{self.RED}{message}"))

    def debug(self, message: str, level: str = "Debug") -> None:
        print(self.message(f"{self.MAGENTAA}{level}", f"{self.MAGENTAA}{message}"))

    def captcha(self, message: str, level: str = "hCaptcha") -> None:
        print(self.message(f"{self.CYAN}{level}", f"{self.CYAN}{message}"))

    def PETC(self):
        input(f"  {self.PINK}[{self.MAGENTAA}Press Enter To Continue{self.PINK}]")

log = Logger()