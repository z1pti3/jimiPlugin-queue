import time

import jimi

class _queueEvent(jimi.db._document):
    queueTriggerID = str()
    queueEventData = dict()
    runTime = int()
    autoClear = bool()
    delay = int()

    _dbCollection = jimi.db.db["queueEvent"]

    def new(self, acl, queueTriggerID, queueEventData, autoClear=True, delay=0):
        self.acl = acl
        self.queueTriggerID = queueTriggerID
        self.queueEventData = queueEventData
        self.autoClear = autoClear
        self.delay = int(time.time() + delay )
        self.runTime = 0
        return super(_queueEvent, self).new()
