from fastapi import FastAPI, Request, Form, Depends, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
from glob import glob
import json 
import uvicorn

BBOX_VIDEO_PATH = 'static/data/bbox-video/webm'
TRACKING_VIDEO_PATH = 'static/data/tracking-video'

app = FastAPI()

templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")

batch_size = 20

bbox_videos = sorted(os.listdir(BBOX_VIDEO_PATH))
n_bbox_video = len(bbox_videos)
n_batch_bbox = n_bbox_video // batch_size + (n_bbox_video % batch_size != 0)

tracking_videos = sorted(os.listdir(TRACKING_VIDEO_PATH ))
n_tracking_video = len(tracking_videos)
n_batch_tracking = n_tracking_video // batch_size + (n_tracking_video % batch_size != 0)

print(f'Total bbox videos: {n_bbox_video}')
print(f'Total bbox batches: {n_batch_bbox}')

print(f'Total tracking videos: {n_tracking_video}')
print(f'Total tracking batches: {n_batch_tracking}')

@app.get('/{source}', response_class=HTMLResponse)
def index(request: Request, source: str):
    if source == 'bbox-video':  # BBox video
        context = {
            'request': request,
            'videos': bbox_videos[0:batch_size],
            'batch_id': 0,
            'last_batch_id': n_batch_bbox - 1,
            'source': source
        }
    else:
        context = {
            'request': request,
            'videos': tracking_videos[0:batch_size],
            'batch_id': 0,
            'last_batch_id': n_batch_tracking - 1,
            'source': source
        }
    return templates.TemplateResponse('index.html', context)

@app.get('/{source}/{batch_id}', response_class=HTMLResponse)
def tracking(request: Request, source: str, batch_id: int):
    if source == 'bbox-video': # Bbox video
        context = {
            'request': request,
            'videos': bbox_videos[batch_id * batch_size:(batch_id + 1) * batch_size],
            'batch_id': batch_id,
            'last_batch_id': n_batch_bbox - 1,
            'source': source
        }
    else:
        context = {
            'request': request,
            'videos': tracking_videos[batch_id * batch_size:(batch_id + 1) * batch_size],
            'batch_id': 0,
            'last_batch_id': n_batch_tracking - 1,
            'source': source
        }
    return templates.TemplateResponse('index.html', context)


if __name__ == '__main__':
    uvicorn.run('app:app', port=6767, host='localhost', reload=True)