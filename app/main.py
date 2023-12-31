from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .routers import post, user, auth, vote, community,event,comment, holiday, business

from .config import settings




app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
app.include_router(community.router)
app.include_router(event.router)
app.include_router(comment.router)
app.include_router(holiday.router)
app.include_router(business.router)

@app.get("/")
def root():
    return {"message": "ARBAB"}