from fastapi import APIRouter
from models.input import InputBaseModel, OutputBaseModel, ModifiedOutputModelBase

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Flying to the stars..."}


@router.post("/{date}", response_model=ModifiedOutputModelBase)
async def generate(date: str, input: InputBaseModel):
    def normalize(value, min_value, max_value):
        return 1 + (value - min_value) * (5 - 1) / (max_value - min_value)

    min_value = min(
        input.extreme_heat,
        input.tropical_cyclones,
        input.earthquakes_and_volcanoes,
        input.floods,
        input.landslides,
    )
    max_value = max(
        input.extreme_heat,
        input.tropical_cyclones,
        input.earthquakes_and_volcanoes,
        input.floods,
        input.landslides,
    )

    norm_extreme_heat = normalize(input.extreme_heat, min_value, max_value)
    norm_tropical_cyclones = normalize(input.tropical_cyclones, min_value, max_value)
    norm_earthquakes_and_volcanoes = normalize(
        input.earthquakes_and_volcanoes, min_value, max_value
    )
    norm_floods = normalize(input.floods, min_value, max_value)
    norm_landslides = normalize(input.landslides, min_value, max_value)

    total_sum = (
        norm_extreme_heat
        + norm_tropical_cyclones
        + norm_earthquakes_and_volcanoes
        + norm_floods
        + norm_landslides
    )

    average = total_sum / 5

    return ModifiedOutputModelBase(
        **input.model_dump(
            exclude={
                "extremeHeat",
                "tropicalCyclones",
                "earthquakesAndVolcanoes",
                "floods",
                "landslides",
            },
            by_alias=True,
        ),
        disasters=average,
        date=date
    )
