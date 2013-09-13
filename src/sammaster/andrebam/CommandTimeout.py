'''
Created on Sep 13, 2013

@author: jcollado@stackoverflow
#http://stackoverflow.com/a/4825933
#Adapted to my use by me (Andre B. Amundsen)
'''

import threading, subprocess

class Command(object):
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    def run(self, timeout):
        def target(cmd):
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            out, err = self.process.communicate()
            self.process.ret_o = out
            self.process.ret_e = err

        thread = threading.Thread(target=target, args=[self.cmd])
        thread.start()

        thread.join(timeout)
        if thread.is_alive():
            self.process.terminate()
            thread.join()
        return self.process
