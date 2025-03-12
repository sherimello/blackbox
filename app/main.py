from fastapi import FastAPI, HTTPException
import httpx

# Create the FastAPI app
app = FastAPI()

# Define the POST endpoint
@app.post("/chat")
async def chat(q : str, imageGenerator : bool):
    url = "https://www.blackbox.ai/api/chat"
    
    # Hardcoded Payload
    payload = {
        "messages": [
            {
                "id": "6kXJ4t8",
                "content": q,
                "role": "user"
            }
        ],
        "agentMode": {},
        "id": "6kXJ4t8",
        "previewToken": None,
        "userId": '7f26c6a7-c1d2-4216-abb4-0681912ea0a5',
        "codeModelMode": False,
        "trendingAgentMode": {},
        "isMicMode": False,
        "userSystemPrompt": None,
        "maxTokens": 2048,
        "playgroundTopP": None,
        "playgroundTemperature": None,
        "isChromeExt": False,
        "githubToken": "",
        "clickedAnswer2": False,
        "clickedAnswer3": False,
        "clickedForceWebSearch": False,
        "visitFromDelta": False,
        "isMemoryEnabled": True,
        "mobileClient": True,
        "userSelectedModel": "@2",
        "validated": "00f37b34-a166-4efb-bce5-1312d87f2f94",
        "imageGenerationMode": imageGenerator,
        "webSearchModePrompt": False,
        "deepSearchMode": False,
        "domains": None,
        "vscodeClient": False,
        "codeInterpreterMode": False,
        "customProfile": {
            "name": "",
            "occupation": "",
            "traits": [],
            "additionalInfo": "",
            "enableNewChats": True
        },
        "session": {
            "user": {
                "name": "shahriar rahman",
                "email": "shahriarr.inan@gmail.com",
                "image": "https://lh3.googleusercontent.com/a/ACg8ocLeF2SJqSX7FnAH7RpYMKQ1lrta37sGpzYl4eawbOM_JbqbqQ=s96-c"
            },
            "expires": "2025-03-30T11:02:54.764Z"
        },
        "isPremium": True,
        "subscriptionCache": {
            "status": "PREMIUM",
            "expiryTimestamp": None,
            "lastChecked": 1740740574503
        },
        "beastMode": False
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "accept": "*/*",
        # "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-US,en;q=0.9,ar-JO;q=0.8,ar;q=0.7,bn;q=0.6",
        "dnt": "1",
        "origin": "https://www.blackbox.ai",
        "referer": "https://www.blackbox.ai/"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            # Send POST request to the BlackBox API
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise error for bad responses
            
            # Debugging: Check the raw response headers and content
            raw_response = {
                "status_code": response.status_code,
                "headers": dict(response.headers),
                "content": response.text  # Get raw content as string
            }
            
            # Return raw response for inspection
            return raw_response
            
        except httpx.HTTPStatusError as http_err:
            raise HTTPException(status_code=http_err.response.status_code, detail="Error occurred")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"An error occurred: {err}")