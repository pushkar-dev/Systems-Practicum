from resolver import DoH

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

myDoH=DoH()
app=FastAPI()

@app.get('/')
def home(name:str=None, type:str=None):
    if name is None:
        return {"message":"this is a custom DoH Server"}
    else:
        ans=myDoH.resolve(name, type)
        return JSONResponse(content=ans.json(), media_type='application/dns-json')

