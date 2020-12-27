from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatRoomConsumer(AsyncWebsocketConsumer):
    """define a class for the chat room"""
    
    # first of all we must be connected to a chat room
    async def connect(self):
        #fetch the room name
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        #then fetch the group of this chat
        self.room_group_name = '%s_chat' % self.room_name

        # now let's create the group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # create an await for sendding
        await self.channel_layer_group_send(
            self.room_group_name,
            {   
                # define a message
                'type' : 'tester_message',
                'tester' : 'welcome all'
            }
        )
    
    #create a tester to test our message
    async def tester_message(self, event):
        tester = event['tester']

        #let's send this message accross the group
        await self.send(text_data=json.dumps({
            'tester' : tester,
        }))

    # create an async for disconnecting
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            
            # define the group and channel data
            self.room_group_name,
            self.channel_name
        )