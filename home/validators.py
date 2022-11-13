from django.core.exceptions import ValidationError

def fileSize(val):
    filesize = val.size
    if filesize > 838860800:
        raise ValidationError(" Maximum file size id 100MB")

