"""
Contains custom exceptions
"""


class MissingSetting(Exception):
    """
    When a setting is missing
    """

    def __init__(self, setting_name):
        self.setting_name = setting_name
        super().__init__(
            f"Could not find setting '{self.setting_name}' in 'PAGE_SHARER' settings."
        )
