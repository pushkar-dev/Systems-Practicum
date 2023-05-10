from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.get("/")
async def resolve_dns(name: str):
    try:
        # Send a DNS over HTTPS (DoH) query to a DoH server
        url = f"https://1.1.1.1/dns-query?name={name}&type=A"
        headers = {"accept": "application/dns-json"}
        response = requests.get(url, headers=headers)

        # Parse the DoH response
        data = response.content.decode("iso-8859-1")
        # print(type(data))
        # print(data['status'])
        # print("Data Status is"+data['Status'])
        data=json.loads(data)
        if data["Status"] == 0:
            return data["Answer"]
        else:
            return "Error: Unable to resolve DNS"
    except:
        return "Error: Unable to resolve DNS"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)