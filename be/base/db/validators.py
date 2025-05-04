from django.core.validators import RegexValidator

class BlankValidator(RegexValidator):
    """
    Create a regex validator to validate a field is not blank.
    """

    def __init__(
            self,
            message="This field cannot be blank.",
            code="blank_invalid",
            inverse_match=None,
            flags=None
        ):
        """
        Initialize a blank regex validation
        """
        regex = r"[^\s]+"
        super().__init__(
            regex=regex,
            message=message,
            code=code,
            inverse_match=inverse_match,
            flags=flags
        )