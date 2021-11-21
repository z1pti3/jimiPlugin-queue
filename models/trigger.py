import time
import secrets

import jimi

from plugins.queue.models import queue

class _queueTrigger(jimi.trigger._trigger):
    webhookToken = str()
    limit = 1

    def __init__(self, restrictClass=True):
        self.webhookToken = secrets.token_hex(128)
        super().__init__(restrictClass=restrictClass)

    def doCheck(self):
        self.result = { "events" : [], "var" : {}, "plugin" : {} }
        events = []
        bulkClass = jimi.db._bulk()
        queueTriggerEvents = queue._queueEvent().getAsClass(query={ "queueTriggerID" : self._id, "runTime" : 0, "delay" : { "$lt" : time.time() } },limit=self.limit)
        for event in queueTriggerEvents:
            if event.autoClear:
                event.runTime = int(time.time())
                event.bulkUpdate(["runTime"],bulkClass)
            events.append(event.queueEventData)
            events[-1]["queueEventID"] = event._id
        bulkClass.bulkOperatonProcessing()
        self.result["events"] = events
        return self.result["events"]