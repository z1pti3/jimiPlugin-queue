import time
import jimi

from plugins.queue.models import queue

class _queueAdd(jimi.action._action):
    queueTriggerID = str()
    useEvent = False
    queueEventDataStr = str()
    queueEventData = dict()
    autoClear = True
    delay = 0

    def doAction(self,data):
        queueTriggerID = jimi.helpers.evalString(self.queueTriggerID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        queueEventDataStr = jimi.helpers.evalString(self.queueEventDataStr,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })
        queueEventData = jimi.helpers.evalDict(self.queueEventData,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })

        if queueTriggerID == "":
            return { "result" : False, "rc" : 1, "msg" : "No queue trigger provided."  }

        queueEvent = {}
        if self.useEvent:
            queueEvent = data["flowData"]["event"]
        elif queueEventDataStr:
            queueEvent = queueEventDataStr
        elif queueEventData:
            queueEvent = queueEventData

        if queueEvent:
            queueEventID = queue._queueEvent().new(self.acl,queueTriggerID,queueEvent,self.autoClear,self.delay).inserted_id
            return { "result" : True, "rc" : 0, "msg" : "New queueEvent created.", "queueEventID" : queueEventID }
        else:
            return { "result" : False, "rc" : 500, "msg" : "No queue event data provided."  }

class _queueClear(jimi.action._action):
    queueEventID = str()

    def doAction(self,data):
        queueEventID = jimi.helpers.evalString(self.queueEventID,{"data" : data["flowData"], "eventData" : data["eventData"], "conductData" : data["conductData"], "persistentData" :  data["persistentData"] })

        if queueEventID == "":
            return { "result" : False, "rc" : 403, "msg" : "No queue trigger."  }

        queueObject = queue._queueEvent().getAsClass(id=queueEventID)
        try:
            queueObject = queueObject[0]
            queueObject.runTime = time.time()
            queueObject.update(["runTime"])
            return { "result" : True, "rc" : 0, "msg" : "queueEvent cleared."  }
        except:
            return { "result" : False, "rc" : 500, "msg" : "No queue object loaded."  }
