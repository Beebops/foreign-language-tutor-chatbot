import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model='text-davinci-003',
    prompt='What is the Spanish word for purple?'
)
print(response.choices[0].text)
# {
#   "choices": [
#     {
#       "finish_reason": "stop",
#       "index": 0,
#       "logprobs": null,
#       "text": "\n\nMorado."
#     }
#   ],
#   "created": 1685799251,
#   "id": "cmpl-7NLgRplsD1dXQJ7AVFj7hAXFogVDh",
#   "model": "text-davinci-003",
#   "object": "text_completion",
#   "usage": {
#     "completion_tokens": 5,
#     "prompt_tokens": 8,
#     "total_tokens": 13
#   }
# }
