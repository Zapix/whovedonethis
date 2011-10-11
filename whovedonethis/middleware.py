from whovedonethis.loggedinuser import LoggedInUser
class LoggedInUserMiddleware(object):
    '''
        Insert this middleware after django.contrib.auth.middleware.AuthenticationMiddleware
    '''
    def process_request(self, request):
        '''
            Returned None for continue request
        '''
        logged_in_user = LoggedInUser()
        logged_in_user.set_user(request)
        return None
