import jimi

class _queueEvent(jimi.db._document):
    queueTriggerID = str()
    queueEventData = dict()
    runTime = int()
    autoClear = bool()

    _dbCollection = jimi.db.db["queueEvent"]

    def new(self, acl, queueTriggerID, queueEventData, autoClear=True):
        self.acl = acl
        self.queueTriggerID = queueTriggerID
        self.queueEventData = queueEventData
        self.autoClear = autoClear
        self.runTime = 0
        return super(_queueEvent, self).new()
