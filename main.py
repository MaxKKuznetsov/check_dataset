import base64
import datetime
import os

from fastapi import File, UploadFile, Request, FastAPI
from fastapi.templating import Jinja2Templates

from config import PATH_TO_USERS_TABLE, PATH_TO_USERS_FOLDER, PATH_TO_HISTORY_TABLE, PATH_HISTORY_FOLDER
from src.users import Users
from src.events import Events
from src.controller import Controller
from src.out_file import OutputFile


app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = Users(PATH_TO_USERS_TABLE, PATH_TO_USERS_FOLDER)
events = Events(PATH_TO_HISTORY_TABLE, PATH_HISTORY_FOLDER)
controller = Controller()
out_file = OutputFile(os.path.join(PATH_HISTORY_FOLDER, 'check_hist.csv'), PATH_TO_HISTORY_TABLE)


@app.get('/next')
async def next():
    controller.event_index += 1
    print(controller.event_index)
    # await get_event()
    out_file.save_to_file()
    return {'event_index': controller.event_index}


@app.get('/back')
async def next():
    controller.event_index -= 1
    print(controller.event_index)
    # await get_event()
    out_file.save_to_file()
    return {'event_index': controller.event_index}


##########
@app.get('/update/ok')
def ok():
    out_file.update(controller.event_index, 'false_match', 0)
    out_file.save_to_file()


@app.get('/update/error')
async def ok():
    out_file.update(controller.event_index, 'false_match', 1)
    out_file.save_to_file()


@app.get('/update/poor_brightness')
async def ok():
    out_file.update(controller.event_index, 'poor_brightness', 1)
    out_file.save_to_file()


@app.get('/update/poor_contrast')
async def ok():
    out_file.update(controller.event_index, 'poor_contrast', 1)
    out_file.save_to_file()


@app.get('/update/poor_focus')
async def ok():
    out_file.update(controller.event_index, 'poor_focus', 1)
    out_file.save_to_file()


@app.get('/update/poor_angle')
async def ok():
    out_file.update(controller.event_index, 'poor_angle', 1)
    out_file.save_to_file()


@app.get('/update/spoofing')
async def ok():
    out_file.update(controller.event_index, 'spoofing', 1)
    out_file.save_to_file()


############
@app.get('/status')
async def status():
    return {'status': 'OK', 'timestamp': datetime.datetime.utcnow()}


@app.get('/events/{index}')
async def get_event(request: Request, index: int):
    # index = controller.event_index
    event = events.get_data(index)

    if not event:
        return {'message': 'event index %i is not found' % index}

    user = users.get_data(event['identified_user_id'])

    if not user:
        return {'message': 'user %i for event index %i is not found' % (event['identified_user_id'], index)}

    return templates.TemplateResponse('show_event.html', {'request': request,
                                                          'event_index': index,
                                                          'event_id': event['event_id'],
                                                          'identified_user_id': event['identified_user_id'],
                                                          'face_img_path': event['face_img_path'],
                                                          'event_img': event['face_img_b64'],
                                                          'identified_user_name': user['name'],
                                                          'user_img_path': user['face_img_path'],
                                                          'user_img': user['face_img_b64']
                                                          })


@app.get('/users/{id}')
async def get_person(request: Request, id: int):
    user = users.get_data(id)

    if not user:
        return {'user': 'user %i is not found' % id}

    return templates.TemplateResponse('show_user.html', {'request': request,
                                                         'id': id,
                                                         'name': user['name'],
                                                         'face_img_path': user['face_img_path'],
                                                         'user_img': user['face_img_b64']
                                                         })
