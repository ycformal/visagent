from PIL import Image

from engine.utils import ProgramInterpreter

interpreter = ProgramInterpreter(dataset='gqa')

prog = """BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is carrying the umbrella?')
FINAL_RESULT=RESULT(var=ANSWER0)"""
prog = """BOX0=GET(image=IMAGE)
IMAGE0=CROP_BELOW(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='bag')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)"""

image = Image.open('./examplar_images/2390296.jpg')
image.thumbnail((640,640),Image.Resampling.LANCZOS)
init_state = dict(
    IMAGE=image.convert('RGB')
)
result, prog_state, html = interpreter.execute(prog,init_state,inspect = True)
print(result)
print(html)