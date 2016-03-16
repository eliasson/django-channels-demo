from channels import Group, Channel
from channels.handler import AsgiHandler

from .models import ChatMessage


def chat_message_consumer(message):
    print("Processing chat message...{0}".format(message.content['message']))
    ChatMessage.objects.create(message=message.content['message'])
    Group("chat").send({"text": "[someone says] {0}".format(message.content['message']), })


def ws_add(message):
    Group("chat").add(message.reply_channel)


def ws_message(message):
    # Emit a message to broadcast message to group (async)
    Channel("chat-messages").send({"message": message.content['text'], })


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


channel_routing = {
    'websocket.connect': ws_add,
    "websocket.receive": ws_message,
    "websocket.disconnect": ws_disconnect,
    "chat-messages": chat_message_consumer,
}
