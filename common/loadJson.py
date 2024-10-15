class LoadJson:
    
    def __init__(self) -> None:
        with open('./common/configFiles/config.json', 'r') as f:
            self.json = eval(f.read())
        f.close()