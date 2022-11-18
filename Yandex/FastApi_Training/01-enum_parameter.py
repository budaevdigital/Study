"""
Задание:
Для астрономической лаборатории нужно написать микросервис, который:

в параметре diameter принимает диаметр космического объекта;
возвращает название соответствующего объекта (по-английски).
Функция, обрабатывающая запрос, должна принимать только один query-параметр diameter; в параметре diameter должны приниматься только значения из перечня.

Перечень объектов и их диаметры:

Солнце (Sun): 1_392_000
Юпитер (Jupiter): 139_822
Сатурн (Saturn): 116_464
Уран (Uranus): 50_724
Нептун (Neptune): 49_224
Земля (Earth): 12_742
Венера (Venus): 12_104
Марс (Mars): 6_780
Ганимед (Ganymede): 5_262
Титан (Titan): 5_151
Меркурий (Mercury): 4_879
"""

from enum import IntEnum
from fastapi import FastAPI 
from typing import Optional
import uvicorn


app = FastAPI()

class DiameterPlanet(IntEnum): 
	Sun = 1392000
	Jupiter = 139822
	Saturn = 116464
	Uranus = 50724
	Neptune = 49224
	Earth = 12742
	Venus = 12104
	Mars = 6780
	Ganymede = 5262
	Titan = 5151
	Mercury = 4879


@app.get('/diameter')
def return_diameter_planet(diameter_planet: Optional[DiameterPlanet]=None,) -> dict[str, str]:
	if diameter_planet is not None:
		return {"Планета ": diameter_planet.name }

if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)

