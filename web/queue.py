import json
from flask import Blueprint, render_template, request

from plugins.queue.models import queue
from plugins.queue.models import trigger

import jimi

queuePages = Blueprint('queuePages', __name__)

@queuePages.route("/public/<token>/",methods=["POST"])
def __PUBLIC__queueWebHook(token):
    webhook = trigger._queueTrigger().getAsClass(query={ "webhookToken" : token })
    if len(webhook) == 1:
        webhook = webhook[0]
        event = json.loads(jimi.api.request.data)
        queue._queueEvent().new(webhook.acl,webhook._id,event)
        return { }, 200
    return { }, 404
