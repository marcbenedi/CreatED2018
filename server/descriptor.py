
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from json_to_sentence import get_sentence
# Create your API key in your account's `Manage your API keys` page:
# https://clarifai.com/developer/account/keys
def describe(image):
    app = ClarifaiApp(api_key='ee1de8e59757433caa06edd607b3325e')

    # You can also create an environment variable called `CLARIFAI_API_KEY`
    # and set its value to your API key.
    # In this case, the construction of the object requires no `api_key` argument.

    model = app.models.get('general-v1.3')
    json_ans = model.predict([image])
    return (get_sentence(json_ans))
