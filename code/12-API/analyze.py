import sys
import logging

from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_code_pb2, status_pb2

from config import clarifai_api_key, unsplash_api_key, unsplash_secret

logging.basicConfig(level=logging.DEBUG)

model_general = 'aaa03c23b3724a16a56b629203edc62c'

image_file = sys.argv[1]
with open(image_file, "rb") as f:
    file_bytes = f.read()


channel = ClarifaiChannel.get_insecure_grpc_channel()
metadata = (('authorization', f'Key {clarifai_api_key}'),)

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

print(post_model_outputs_response, file=sys.stderr)

for concept in post_model_outputs_response.outputs[0].data.concepts:
    print(f"<tr><td>{concept.name}</td><td class='right'>{round(concept.value*100, 2):02.2f} %</td></tr>")
