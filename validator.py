# Example of a custom module to be imported

import re

def validate_email(email):
    if len(email) > 7:
        return bool(re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([azA-Z]{2,3}|[0-9]{1,3})(]?)$", email)
        )
    
