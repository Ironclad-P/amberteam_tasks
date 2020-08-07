class Config:
    def __init__(self, browser):
        self.which_browser = {
            'chrome': 'Chrome',
            'firefox': 'Firefox',
            'opera': 'Opera',
        }[browser]