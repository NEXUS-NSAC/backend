import json
from fastapi import APIRouter
from models.input import (
    InputBaseModel,
    OutputBaseModel,
    ModifiedOutputModelBase,
    InputModel,
)
from openai import OpenAI
from typing import Final
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()
client: Final = OpenAI()
assistant_id: Final = "asst_O20YXfM20bjFTS8uLn2gxokD"


@router.get("/")
async def read_root():
    return {"message": "Flying to the stars..."}


@router.post("/{date}", response_model=dict)
async def generate(date: str, input: InputBaseModel):

    content = InputModel(parameters=input.model_dump(), date=date)

    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=content.model_dump_json(),
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
        # instructions="Please address the user as Jane Doe. The user has a premium account.",
    )
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        # print(messages)
    else:
        print(run.status)

    message_content = messages.data[0].content[0].text.value
    message_content = message_content.strip("```json").strip("```")
    message_content = json.loads(message_content)
    print(message_content)

    def normalize(value, min_value, max_value):
        return 1 + (value - min_value) * (5 - 1) / (max_value - min_value)

    min_value = min(
        int(message_content["extreme_heat"]),
        int(message_content["tropical_cyclones"]),
        int(message_content["earthquakes_and_volcanoes"]),
        int(message_content["floods"]),
        int(message_content["landslides"]),
    )
    max_value = max(
        int(message_content["extreme_heat"]),
        int(message_content["tropical_cyclones"]),
        int(message_content["earthquakes_and_volcanoes"]),
        int(message_content["floods"]),
        int(message_content["landslides"]),
    )

    norm_extreme_heat = normalize(
        int(message_content["extreme_heat"]), min_value, max_value
    )
    norm_tropical_cyclones = normalize(
        int(message_content["tropical_cyclones"]), min_value, max_value
    )
    norm_earthquakes_and_volcanoes = normalize(
        int(message_content["earthquakes_and_volcanoes"]), min_value, max_value
    )
    norm_floods = normalize(int(message_content["floods"]), min_value, max_value)
    norm_landslides = normalize(
        int(message_content["landslides"]), min_value, max_value
    )

    total_sum = (
        norm_extreme_heat
        + norm_tropical_cyclones
        + norm_earthquakes_and_volcanoes
        + norm_floods
        + norm_landslides
    )

    average = total_sum / 5

    return {
        "content": message_content,
        "disasters": average,
        "date": date,
    }
