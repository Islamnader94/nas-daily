import time
from rest_framework.throttling import BaseThrottle
VISIT_RECORD = dict()

class RateLimit(BaseThrottle):
    '''
    Rate limit requests to wait 60s,
    Can only access 10 times in 10s.
    '''
    def __init__(self):
        self.history = None

    def allow_request(self,request,view):
        #Get users ip (get_ident)
        remote_addr = self.get_ident(request)
        ctime = time.time()

        if remote_addr not in VISIT_RECORD:
            VISIT_RECORD[remote_addr] = [ctime,] 
            return True 

        history = VISIT_RECORD.get(remote_addr)

        self.history = history

        while history and history[-1] < ctime - 10:
            history.pop()

        if len(history) < 10:
            history.insert(0,ctime)
            return True

    def wait(self):
        '''
        Function to return how long will it take to visit
        '''
        ctime = time.time()
        return 60 - (ctime - self.history[-1])