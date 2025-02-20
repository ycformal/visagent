# from engine import validator

# prog = """BOX0=LOC(image=IMAGE,object='necktie')
# IMAGE0=CROP(image=IMAGE,box=BOX0)
# BOX1=LOC(image=IMAGE,object='shoe')
# IMAGE1=CROP(image=IMAGE,box=BOX1)
# ANSWER0=VQA(image=IMAGE0,question='What color is the necktie?')
# ANSWER1=VQA(image=IMAGE1,question='What color is the shoe?')
# ANSWER2=EVAL(expr="'yes' if {ANSWER0}!= {ANSWER1} else 'no'")
# FINAL_RESULT=RESULT(var=ANSWER2)"""

# module_list = ["LOC", "CROP", "CROP_ABOVE", "CROP_BELOW", "CROP_LEFTOF", "CROP_RIGHTOF", "CROP_BEHIND", "CROP_INFRONT", "CROP_INFRONTOF", "CROP_AHEAD", "FROP_FRONTOF", "COUNT", "VQA", "RESULT", "EVAL", "GET"]

# question = "Does the necktie have a different color than the shoe?"

# print(validator.validate(prog, question, module_list))

from PIL import Image

from engine.utils import ProgramInterpreter

interpreter = ProgramInterpreter(dataset='gqa')

prog = """BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is carrying the umbrella?')
FINAL_RESULT=RESULT(var=ANSWER0)"""

image = Image.open('./examplar_images/2390296.jpg')
image.thumbnail((640,640),Image.Resampling.LANCZOS)
print(image)
init_state = dict(
    IMAGE=image.convert('RGB')
)
result, prog_state, html = interpreter.execute(prog,init_state, inspect=True)
print(result)

# with open('output.md', 'w') as f:
#     f.write(html)

# import os
# # Enforce the download/cache directory for Hugging Face models.
# os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
# from transformers import ViltProcessor, ViltForQuestionAnswering
# import requests
# from PIL import Image
# import torch

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# # prepare image + question
# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# text = "How many cats are there?"

# processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
# model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa").to(device)
# model.eval()

# # prepare inputs
# encoding = processor(image, text, return_tensors="pt")
# encoding = {k:v.to(device) for k,v in encoding.items()}

# with torch.no_grad():
#     outputs = model(**encoding)
# logits = outputs.logits
# idx = logits.argmax(-1).item()
# print(model.config.id2label[idx])

# import os
# # Enforce the download/cache directory for Hugging Face models.
# os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
# from transformers import PaliGemmaForConditionalGeneration, AutoProcessor
# import requests
# from PIL import Image
# import torch

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# # prepare image + question
# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# text = "How many cats are there?"

# processor = AutoProcessor.from_pretrained("google/paligemma-3b-ft-vqav2-448")
# model = PaliGemmaForConditionalGeneration.from_pretrained("google/paligemma-3b-ft-vqav2-448").to(device)
# model.eval()

# encoding = processor(image, text, return_tensors="pt")
# encoding = {k:v.to(device) for k,v in encoding.items()}

# with torch.no_grad():
#     outputs = model.generate(**encoding, max_new_tokens=10)
# print(processor.decode(outputs[0], skip_special_tokens=True))

# import os
# # Enforce the download/cache directory for Hugging Face models.
# os.environ["HF_HOME"] = "/home/hice1/yxu846/scratch/models"
# from transformers import BlipForQuestionAnswering, AutoProcessor
# import requests
# from PIL import Image
# import torch

# device = "cuda:0" if torch.cuda.is_available() else "cpu"
# # prepare image + question
# url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(url, stream=True).raw)
# text = "What is shown in the image?"

# processor = AutoProcessor.from_pretrained("Salesforce/blip-vqa-capfilt-large")
# model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-capfilt-large").to(device)
# model.eval()

# encoding = processor(image, text, return_tensors="pt")
# encoding = {k:v.to(device) for k,v in encoding.items()}

# with torch.no_grad():
#     outputs = model.generate(**encoding, max_new_tokens=10)
# print(processor.decode(outputs[0], skip_special_tokens=True))
