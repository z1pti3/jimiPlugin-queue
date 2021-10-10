import jimi

class _queue(jimi.plugin._plugin):
    version = 0.1

    def install(self):
        jimi.model.registerModel("queueEvent","_queueEvent","_document","plugins.queue.models.queue")
        jimi.model.registerModel("queueAdd","_queueAdd","_action","plugins.queue.models.action")
        jimi.model.registerModel("queueClear","_queueClear","_action","plugins.queue.models.action")
        jimi.model.registerModel("queueTrigger","_queueTrigger","_trigger","plugins.queue.models.trigger")
        return True

    def uninstall(self):
        jimi.model.deregisterModel("queueEvent","_queueEvent","_document","plugins.queue.models.queue")
        jimi.model.deregisterModel("queueAdd","_queueAdd","_action","plugins.queue.models.action")
        jimi.model.deregisterModel("queueClear","_queueClear","_action","plugins.queue.models.action")
        jimi.model.deregisterModel("queueTrigger","_queueTrigger","_trigger","plugins.queue.models.trigger")
        return True

    def upgrade(self,LatestPluginVersion):
        if self.version < 0.1:
            pass
        return True
