class Logger:
    def __init__(self, log_level):
        self.log_level = log_level
    
    
    def __call__(self, message):
        if self.log_level == "Info":
            print(f"{self.log_level}: {message}")
        elif self.log_level == "Warning":
            print(f"{self.log_level}: {message}")
        elif self.log_level == "Error":
            print(f"{self.log_level}: {message}")
        else:
            print(f"{self.log_level}: {message}")


logger = Logger("Info")
logger("Something happened!")
