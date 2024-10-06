from pydantic import BaseModel

from pydantic import BaseModel, Field
from typing import Optional


class InputBaseModel(BaseModel):
    extreme_heat: Optional[int] = Field(0, alias="extremeHeat")
    tropical_cyclones: Optional[int] = Field(0, alias="tropicalCyclones")
    earthquakes_and_volcanoes: Optional[int] = Field(0, alias="earthquakesAndVolcanoes")
    floods: Optional[int] = Field(0, alias="floods")
    landslides: Optional[int] = Field(0, alias="landslides")
    global_primary_energy_consumption: Optional[int] = Field(
        0, alias="globalPrimaryEnergyConsumption"
    )
    air_quality: Optional[int] = Field(0, alias="airQuality")
    glacier_mass_balance: Optional[int] = Field(0, alias="glacierMassBalance")
    precipitation: Optional[int] = Field(0, alias="precipitation")
    greenhouse_gases: Optional[int] = Field(0, alias="greenhouseGases")
    atmospheric_temperature: Optional[float] = Field(
        0.0, alias="atmosphericTemperature"
    )
    solar_radiation_absorption: Optional[int] = Field(
        0, alias="solarRadiationAbsorption"
    )
    erosion_rates: Optional[int] = Field(0, alias="erosionRates")
    snow_cover_duration: Optional[int] = Field(0, alias="snowCoverDuration")
    sea_surface_temperature: Optional[float] = Field(0.0, alias="seaSurfaceTemperature")
    water_quality_indicators: Optional[int] = Field(0, alias="waterQualityIndicators")
    forest_cover: Optional[int] = Field(0, alias="forestCover")
    soil_composition_and_quality: Optional[int] = Field(
        0, alias="soilCompositionAndQuality"
    )

    class Config:
        populate_by_alias = True


class OutputBaseModel(InputBaseModel):
    animal_impact: Optional[int] = Field(0, alias="animalImpact")
    human_impact: Optional[int] = Field(0, alias="humanImpact")
    tree_impact: Optional[int] = Field(0, alias="treeImpact")
    aquatic_impact: Optional[int] = Field(0, alias="aquaticImpact")

    class Config:
        populate_by_alias = True


class ModifiedOutputModelBase(OutputBaseModel):
    diasasters: Optional[int] = Field(0, alias="disasters")

    class Config:
        populate_by_alias = True
