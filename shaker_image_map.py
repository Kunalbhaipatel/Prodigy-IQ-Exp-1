
def get_shaker_image(shaker_name):
    image_map = {
        "Derrick 806": "images/Derrick 806.jpg",
        "Derrick DP814": "images/Derrick DP814.jpg",
        "Derrick Dualpool": "images/Derrick Dualpool.jpg",
        "Derrick 504": "images/Derrick 504.jpg",
        "Brandt King Cobra": "images/KING-COBRA-Shale-Shaker.jpg",
        "BrandT LCM 3D": "images/BrandT LCM 3D.jpg",
        "BrandT Sabre": "images/BrandT Sabre.jpg",
        "NOV Alpha": "images/NOV Alpha.jpg",
        "MI SWACO Moongoos": "images/MI SWACO Moongoos.jpg",
        "Hyperpool": "images/Hyperpool 1.jpg"
    }
    return image_map.get(shaker_name)
