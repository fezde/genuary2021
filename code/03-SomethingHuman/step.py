import json
import os
import shutil
import sys
from time import sleep

import requests
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2, status_pb2
from unsplash.api import Api
from unsplash.auth import Auth

from config import clarifai_api_key, unsplash_api_key, unsplash_secret

current_step = int(sys.argv[1])
print(f"Running on iteration {current_step}")


used_concepts = []
if os.path.isfile("used_concepts.json"):
    with open("used_concepts.json", "r") as fh:
        used_concepts = json.load(fh)

model_general = 'aaa03c23b3724a16a56b629203edc62c'

image_file = f"output/{current_step:03d}.png_out.png"
with open(image_file, "rb") as f:
    file_bytes = f.read()


channel = ClarifaiChannel.get_insecure_grpc_channel()
metadata = (('authorization', f'Key {clarifai_api_key}'),)

print(f"Requesting data from clarifai using {image_file}")

stub = service_pb2_grpc.V2Stub(channel)
post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        model_id=model_general,
        # version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        base64=file_bytes
                    )
                )
            )
        ]
    ),
    metadata=metadata
)
print("Data received")
if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

possible_concepts = [x.name for x in post_model_outputs_response.outputs[0].data.concepts if x.name not in used_concepts]
print(f"Possible concepts: {possible_concepts}")


unsplash_auth = Auth(unsplash_api_key, unsplash_secret, "", code="")
unsplash_api = Api(unsplash_auth)

found_something = False
concept_idx = 0

while not found_something:
    if len(possible_concepts) > 0:
        new_concept = possible_concepts[concept_idx]
        used_concepts.append(new_concept)
    else:
        new_concept = post_model_outputs_response.outputs[0].data.concepts[0].name
    print(f"new concept: {new_concept}")

    result = unsplash_api.search.photos(new_concept)
    if len(result["results"]) > 0:
        found_something = True
    else:
        concept_idx += 1
        if concept_idx < len(possible_concepts)-1:
            print("Did not find something trying next concept")
        else:
            print("Out of concepts")
            sys.exit(-1)

photo_id = result["results"][0].id
print(photo_id)
photo = unsplash_api.photo.get(photo_id)
print(photo.urls.regular)


url = photo.urls.regular
response = requests.get(url, stream=True)
with open('temp.jpg', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response


os.system(f"convert temp.jpg -resize x600\> output/{(current_step+1):03d}.png")
os.system(f"plingo output/{(current_step+1):03d}.png")

with open("output/table.html", "a+") as fh:
    fh.write("<tr><td valign='center' class='right'>")
    fh.write(f"{new_concept} --&gt;")
    fh.write("</td><td>")
    fh.write(f"<a href='{(current_step+1):03d}.png'><img src='{(current_step+1):03d}.png' height='200'/></a>")
    fh.write("</td><td>")
    fh.write(f"<a href='{(current_step+1):03d}.png'><img src='{(current_step+1):03d}.png_out.png' height='200'/></a>")
    fh.write("</td><td>")
    fh.write(
        f'<span>Photo by <a href="{photo.user.links.html}" target="_blank">{photo.user.name}</a> on <a href="{photo.links.html}" target="_blank">Unsplash</a></span>')
    fh.write("</td></tr>")
    fh.write("\n")

with open("used_concepts.json", "w") as fh:
    json.dump(used_concepts, fh)

print(f"Done with iteration {current_step}")
