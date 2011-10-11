from functools import wraps

from whovedonethis.loggedinuser import LoggedInUser

def add_created_user(f):
    '''
        Decorate pre_save signal for adding created user
    '''
    @wraps(f)
    def wrapper(sender, instance, **kwargs):
        if not instance.id:
            created_by_attr = getattr(instance, "created_by_field",
                "created_by"
            )
            setattr(instance, created_by_attr, LoggedInUser().current_user)
        return f(sender, instance, **kwargs)
    return wrapper

def add_updated_user(f):
    '''
        Decorate pre_save signal for adding created user
    '''
    @wraps(f)
    def wrapper(sender, instance, **kwargs):
        updated_by_attr = getattr(instance, "updated_by_field",
            "updated_by"
        )
        setattr(instance, updated_by_attr, LoggedInUser().current_user)
        return f(sender, instance, **kwargs)
    return wrapper
    
add_created_and_updated_user = lambda x: add_created_user(add_updated_user(x))
add_created_and_updated_user.__doc__ =\
    '''
        Decorate pre_save signal for adding created user
    '''
