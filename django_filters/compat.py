try:
    from django.db.models.constants import LOOKUP_SEP
except ImportError:
    # django 1.4 has this in a different location
    from django.db.models.sql.constants import LOOKUP_SEP
    
