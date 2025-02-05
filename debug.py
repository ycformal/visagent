from PIL import Image

from engine.utils import ProgramInterpreter

interpreter = ProgramInterpreter(dataset='gqa')

prog = """
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is carrying the umbrella?')
FINAL_RESULT=RESULT(var=ANSWER0)
"""
image = Image.open('./examplar_images/2390296.jpg')
image.thumbnail((640,640),Image.Resampling.LANCZOS)
init_state = dict(
    IMAGE=image.convert('RGB')
)
result, prog_state = interpreter.execute(prog,init_state)
print(result)