class Config:
    def __init__(self, roms_directory: str = '', saves_directory: str = '', states_directory: str = '', tags: [str] = '', name_format: str = ''):
        self.roms_directory: str = roms_directory
        self.saves_directory: str = saves_directory
        self.states_directory: str = states_directory
        self.tags: [str] = tags
        self.name_format: str = name_format

    def __str__(self):
        return f'config:\n  roms_directory: {self.roms_directory},\n  saves_directory: {self.saves_directory},\n  states_directory: {self.states_directory},\n  tags: {self.tags},\n  name_format: {self.name_format}'

    def get_roms_directory(self):
        return self.roms_directory

    def get_saves_directory(self):
        return self.saves_directory

    def get_states_directory(self):
        return self.states_directory

    def get_tags(self):
        return self.tags

    def get_name_format(self):
        return self.name_format

    def add_tag(self, new_tag):
        if new_tag in self.tags:
            return
        self.tags.append(new_tag)
