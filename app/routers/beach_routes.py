from fastapi import APIRouter, Depends
from app.schemas.beanch_schemas import BeachCondition
from typing import List
import random
import time

router = APIRouter()

# ✅ Function to simulate dynamic data
def simulate_beach_data():
    base_beaches = [
      {
            "id": 1,
            "name": "Pantai Merdeka",
            "temperature": 30.0,
            "wave_height": 1.0,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://www.shutterstock.com/shutterstock/videos/3538608219/thumb/1.jpg?ip=x480"
        },
        {
            "id": 2,
            "name": "Pantai Cahaya Bulan",
            "temperature": 32.0,
            "wave_height": 1.8,
            "crowd_level": "Medium",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://www.caridestinasi.com/wp-content/uploads/2015/08/berkelah-di-pantai-cahaya-bulan.jpg"
        },
        {
            "id": 3,
            "name": "Pantai Bagan Lalang",
            "temperature": 28.0,
            "wave_height": 1.0,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "West",
            "image_url": "https://www.caridestinasi.com/wp-content/uploads/2015/08/percutian-ke-resort-avani-bagan-lalang.png"
        },
        {
            "id": 4,
            "name": "Pantai Kuala Perlis",
            "temperature": 28.0,
            "wave_height": 0.9,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://cdn.motherhood.com.my/wp-content/uploads/sites/2/2021/12/23151516/tempat-menarik-di-Perlis.jpg"
        },
        {
            "id": 5,
            "name": "Pantai Batu Burok",
            "temperature": 31.0,
            "wave_height": 1.6,
            "crowd_level": "Medium",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://www.discoveryterengganu.com/wp-content/uploads/2024/04/1-23.jpg"
        },
        {
            "id": 6,
            "name": "Pantai Desaru",
            "temperature": 32.0,
            "wave_height": 18.1,
            "crowd_level": "High",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "South",
            "image_url": "https://cf.bstatic.com/xdata/images/hotel/max1024x768/323943628.webp?k=a0befc38838de62e47c3badc99b0e1fdeb727e9f0bd49ec03fba91d4650a2d21&o="
        },
        {
            "id": 7,
            "name": "Pantai Cenang",
            "temperature": 32.3,
            "wave_height": 1.2,
            "crowd_level": "High",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://content.r9cdn.net/rimg/dimg/6b/cb/0e46e803-city-313639-166ea418a18.jpg?width=1366&height=768&xhint=1033&yhint=1636&crop=true"
        },
        {
            "id": 8,
            "name": "Tanjung Rhu",
            "temperature": 30.2,
            "wave_height": 0.7,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "North",
            "image_url": "https://naturallylangkawi.my/wp-content/uploads/2024/11/TjRhu-6.jpg"
        },
        {
            "id": 9,
            "name": "Teluk Cempedak",
            "temperature": 30.5,
            "wave_height": 1.0,
            "crowd_level": "High",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://mbk.gov.my/portal/wp-content/uploads/2021/03/telukcempedak.jpg"
        }, 
        {
            "id": 10,
            "name": "Pantai Penarik",
            "temperature": 29.8,
            "wave_height": 1.6,
            "crowd_level": "Low",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "East",
            "image_url": "https://cdn.libur.com.my/2023/05/6f.jpg"
        },
        {
            "id": 11,
            "name": "Batu Ferringhi Beach",
            "temperature": 30.0,
            "wave_height": 0.9,
            "crowd_level": "High",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "West",
            "image_url": "https://www.awaygowe.com/wp-content/uploads/2019/10/batu-ferringhi-reasons-featured2.webp"
        },
        {
            "id": 12,
            "name": "Port Dickson Beach",
            "temperature": 33.0,
            "wave_height": 0.6,
            "crowd_level": "High",
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "regions": "South",
            "image_url": "https://www.agoda.com/wp-content/uploads/2024/05/Pantai-Cahaya-Negeri-Beach-port-dickson-malaysia.jpg"
        }, 
          
    ]

    dynamic_data = []
    for beach in base_beaches:
        dynamic_data.append({
            **beach,
            "temperature": round(random.uniform(27.0, 34.0), 1),
            "wave_height": round(random.uniform(0.5, 2.5), 1),
            "crowd_level": random.choice(["Low", "Medium", "High"]),
            "safety_flag": random.choice(["Green", "Yellow", "Red"]),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })

    return dynamic_data

# ✅ Route that returns dynamic mocked beach data
@router.get("/mock", response_model=List[BeachCondition])
def get_mocked_beaches():
    return simulate_beach_data()
