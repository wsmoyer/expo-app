from channels.generic.websocket import AsyncConsumer
import json
import asyncio
from .mixins import SocketsDatabaseMixin
from .models import Question,Response
from channels.exceptions import StopConsumer

class SurveyConsumer(AsyncConsumer,SocketsDatabaseMixin):
    async def websocket_connect(self, event):
        print('CONNECTED', event)
      
        await self.channel_layer.group_add(
            'index',
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept',
        })
   
    async def fetch_responses(self,command):
        responses = await self.get_responses()
        new_arr = []
        for r in responses:
            new_dict = {
                'question':r.question.question_text,
                'response':r.response,
                'command':command
            }
            new_arr.append(new_dict)
        await self.channel_layer.group_send(
            'index',
            {
            "type":"handle_response",
            "text": json.dumps(new_arr)
            })

    async def fetch_questions(self,command):
        questions = [question for question in Question.objects.all()]
        new_arr = []
        for question in questions:
            new_dict = {
                'question':question.question_text,
                'question_id':question.id,
                'command':command
            }
            new_arr.append(new_dict)
        await self.channel_layer.group_send(
            'index',
            {
            "type":"handle_response",
            "text": json.dumps(new_arr)
            })

    async def handle_submission(self,command,dict_data):
        response = dict_data.get('message',None)
        question = dict_data.get('question_id',None)

        if question is not None:
            res = await self.save_response(response,question)
            question_count = await self.count_questions()
            finalResponse = {
                'response':response,
                'question_id':question,
                'question':res.question.question_text,
                'question_count':question_count,
                'command':command
            }
            new_arr = []
            new_arr.append(finalResponse)
            await self.channel_layer.group_send(
                'index',
                {
                "type":"handle_response",
                "text": json.dumps(new_arr)
            })

    async def websocket_receive(self, event):
        print('RECEIVED',event)
        recieved_text = event.get('text', None)
       
        if recieved_text is not None:
            dict_data = json.loads(recieved_text)
            command = dict_data.get('command',None)
            commands = {
           'fetch_responses':self.fetch_responses(command),
           'fetch_questions': self.fetch_questions(command),
           'handle_submission':self.handle_submission(command,dict_data)
            }
            c = commands.get(command,None)
            await c

    async def handle_response(self,event):
        # print('response',event)
        await self.send({
            "type":"websocket.send",
            "text":event['text'],
        })
   
    async def websocket_disconnect(self, event):
        print('DISCONNECTED',event)
        raise StopConsumer

