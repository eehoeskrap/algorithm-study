'''
https://leetcode.com/problems/logger-rate-limiter/description/

frist, if the value of prev_timestamp does not exists, the timestamp and message are stored in pairs. 
Then, each time the shouldPrintMessage function is called, it compares with the previous pair and returns true or false. 
'''
class Logger(object):

    def __init__(self):
        
        self.prev_timestamp = {}


    def shouldPrintMessage(self, timestamp, message):
        """
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self.prev_timestamp.keys(): 
            self.prev_timestamp[message] = timestamp + 10
            return True 
        

        if timestamp < self.prev_timestamp[message]:
            return False
        else:
            self.prev_timestamp[message] = timestamp + 10
            return True 

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)