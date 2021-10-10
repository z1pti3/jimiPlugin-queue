import time

import jimi

from plugins.queue.models import queue

class _queueTrigger(jimi.trigger._trigger):
    limit = 1

    def doCheck(self):
        self.result = { "events" : [], "var" : {}, "plugin" : {} }
        events = []
        bulkClass = jimi.db._bulk()
        queueTriggerEvents = queue._queueEvent().getAsClass(query={ "queueTriggerID" : self._id, "runTime" : 0 },limit=self.limit)
        for event in queueTriggerEvents:
            if event.autoClear:
                event.runTime = int(time.time())
                event.bulkUpdate(["runTime"],bulkClass)
            events.append(event.queueEventData)
            events[-1]["queueEventID"] = event._id
        bulkClass.bulkOperatonProcessing()
        self.result["events"] = events
        return self.result["events"]