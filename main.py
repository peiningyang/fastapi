from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "What is your horoscope?"}

@app.get("/generate/{month}/{day}")
async def horoscope(month: int, day: int):
    """Takes in user's birthday and generates their horoscope"""
    
    if month == 12:
        sign = "Sagittarius" if (day < 22) else "Capricorn"
    elif month == 1:
        sign = "Capricorn" if (day < 20) else "Aquarius"
    elif month == 2:
        sign = "Aquarius" if (day < 19) else "Pisces"
    elif month == 3:
        sign = "Pisces" if (day < 21) else "Aries"
    elif month == 4:
        sign = "Aries" if (day < 20) else "Taurus"
    elif month == 5:
        sign = "Taurus" if (day < 21) else "Gemini"
    elif month == 6: 
        sign = "Gemini" if (day < 21) else "Cancer"
    elif month == 7:
        sign = "Cancer" if (day < 23) else "Leo"
    elif month == 8: 
        sign = "Leo" if (day < 23) else "Virgo"
    elif month == 9:
        sign = "Virgo" if (day < 23) else "Libra"
    elif month == 10:
        sign = "Libra" if (day < 23) else "Scorpio"
    elif month == 11:
        sign = "Scorpio" if (day < 22) else "Sagittarius"
    
    return {"Your sign is": sign}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')