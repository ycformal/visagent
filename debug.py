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

with open('output.md', 'w') as f:
    f.write(html)