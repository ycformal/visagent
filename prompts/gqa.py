import random

GQA_CURATED_EXAMPLES=[
"""Question: Are there trains or fences in this scene?
Type: Are A or B?
Program:
BOX0=LOC(image=IMAGE,object='train')
BOX1=LOC(image=IMAGE,object='fence')
ANSWER0=COUNT(box=BOX0)
ANSWER1=COUNT(box=BOX1)
ANSWER2=EVAL(expr="'yes' if {ANSWER0} + {ANSWER1} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER)
""",
"""Question: Who is carrying the umbrella?
Type: Who doing A?
Program:
BOX0=LOC(image=IMAGE,object='umbrella')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Who is carrying the umbrella?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Which place is it?
Type: Complex question (place, weather, etc.)
Program:
ANSWER0=VQA(image=IMAGE,question='Which place is it?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: What color is the curtain that is to the right of the mirror?
Type: What <attri> is A <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='mirror')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the curtain?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Is the pillow in the top part or in the bottom of the picture?
Type: Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_above(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='pillow')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'top' if {ANSWER0} > 0 else 'bottom'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Do you see bottles to the right of the wine on the left of the picture?
Type: Is A <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='wine')
IMAGE1=CROP_RIGHTOF(image=IMAGE0,box=BOX1)
BOX2=LOC(image=IMAGE1,object='bottles')
ANSWER0=COUNT(box=BOX2)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Which side is the food on?
Type: Which side is A?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='food')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'right' if {ANSWER0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Which side of the image is the chair on?
Type: Which side is A?
Program:
BOX0=LOC(image=IMAGE,object='all')
IMAGE0=CROP_RIGHTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='chair')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'right' if {ANSWER0} > 0 else 'left'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: What do the wetsuit and the sky have in common?
Type: What's in common between A and B?
Program:
ANSWER0=VQA(image=IMAGE,question='What do the wetsuit and the sky have in common?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Do the post and the sign have a different colors?
Type: Do A and B have different <attr>?
Program:
BOX0=LOC(image=IMAGE,object='post')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='sign')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the post?')
ANSWER1=VQA(image=IMAGE1,question='What color is the sign?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} != {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
""",
"""Question: Does the traffic cone have white color?
Type: Is A <attr>?
Program:
BOX0=LOC(image=IMAGE,object='traffic cone')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='What color is the traffic cone?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} == 'white' else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Are these animals of different species?
Type: Are As different in <attr>
Program:
ANSWER0=VQA(image=IMAGE,question='Are these animals of different species?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Is the tall lamp to the left or to the right of the laptop computer?
Type: Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='tall lamp')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='laptop computer')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Does the mat have the same color as the sky?
Type: Do A and B have same <attr>?
Program:
BOX0=LOC(image=IMAGE,object='sky')
IMAGE0=CROP(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE,object='mat')
IMAGE1=CROP(image=IMAGE,box=BOX1)
ANSWER0=VQA(image=IMAGE0,question='What color is the sky?')
ANSWER1=VQA(image=IMAGE1,question='What color is the mat?')
ANSWER2=EVAL(expr="'yes' if {ANSWER0} == {ANSWER1} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER2)
""",
"""Question: Is the candle to the left or to the right of the table?
Type: Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='table')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='candle')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'left' if {ANSWER0} > 0 else 'right'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Is the cat above a mat?
Type: Is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='mat')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the cat above a mat?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Is the street light standing behind a truck?
Type: Is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='truck')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the street light standing behind the truck?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: Is the cat on a mat?
Type: Is A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='mat')
IMAGE0=CROP(image=IMAGE,box=BOX0)
ANSWER0=VQA(image=IMAGE0,question='Is the cat on a mat?')
ANSWER1=EVAL(expr="'yes' if {ANSWER0} else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
"""Question: What is the color of the cat above the mat?
Type: What is <attr> of A <spatial pos> B?
Program:
BOX0=LOC(image=IMAGE,object='mat')
IMAGE0=CROP_ABOVE(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='cat')
ANSWER0=VQA(image=IMAGE0,question='What is the color of the cat above the mat?')
FINAL_RESULT=RESULT(var=ANSWER0)
""",
"""Question: Is the tall lamp to the left or to the right of the laptop computer?
Type: Is A <planar pos> or <planar pos> B?
Program:
BOX0=LOC(image=IMAGE,object='tall lamp')
IMAGE0=CROP_LEFTOF(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='laptop computer')
ANSWER0=COUNT(box=BOX1)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
""",
]

def create_prompt(inputs,num_prompts=8,method='random',seed=42,group=0):
    if method=='all':
        prompt_examples = GQA_CURATED_EXAMPLES
    elif method=='random':
        random.seed(seed)
        prompt_examples = random.sample(GQA_CURATED_EXAMPLES,num_prompts)
    else:
        raise NotImplementedError

    prompt_examples = '\n'.join(prompt_examples)
    prompt_examples = f'Think step by step to answer the question.\n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nType: ".format(**inputs)