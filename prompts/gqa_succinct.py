import random

GQA_CURATED_EXAMPLES="""Question: Is the vehicle in the top of the image?
Chain:
INPUT(IMAGE)
LOC(TOP)|CROP|LOC(vehicle)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Are there trains or fences in this scene?
Chain:
INPUT(IMAGE)
LOC(train)|COUNT|ASSIGN(RESULT0)
LOC(fence)|COUNT|ASSIGN(RESULT1)
EVAL('yes' if {RESULT0}>0 or {RESULT1}>0 else 'no')|ASSIGN(OUTPUT)

Question: Who is carrying the umbrella?
Chain:
INPUT(IMAGE)
VQA(Who is carrying the umbrella?)|ASSIGN(OUTPUT)

Question: Which place is it?
Chain:
INPUT(IMAGE)
VQA(Which place is it?)|ASSIGN(OUTPUT)

Question: What color is the curtain that is to the right of the mirror?
Chain:
INPUT(IMAGE)
LOC(mirror)|CROP_RIGHT|LOC(curtain)|CROP|VQA(What color is the curtain?)|ASSIGN(OUTPUT)

Question: Is the pillow in the top part or in the bottom of the picture?
Chain:
INPUT(IMAGE)
LOC(TOP)|CROP|LOC(pillow)|COUNT|ASSIGN(RESULT0)
EVAL('top' if {RESULT0}>0 else 'bottom')|ASSIGN(OUTPUT)

Question: Do you see bottles to the right of the wine on the left of the picture?
Chain:
INPUT(IMAGE)
LOC(LEFT)|CROP|LOC(wine)|CROP_RIGHT|LOC(bottle)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Is the street light standing behind a truck?
Chain:
INPUT(IMAGE)
LOC(truck)|CROP_BEHIND|LOC(street light)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Which side is the food on?
Chain:
INPUT(IMAGE)
LOC(RIGHT)|CROP|LOC(food)|COUNT|ASSIGN(RESULT0)
EVAL('right' if {RESULT0}>0 else 'left')|ASSIGN(OUTPUT)

Question: What do the wetsuit and the sky have in common?
Chain:
INPUT(IMAGE)
VQA(What do the wetsuit and the sky have in common?)|ASSIGN(OUTPUT)

Question: Do the post and the sign have a different colors?
Chain:
INPUT(IMAGE)
LOC(post)|CROP|VQA(What color is the post?)|ASSIGN(RESULT0)
LOC(sign)|CROP|VQA(What color is the sign?)|ASSIGN(RESULT1)
EVAL('yes' if {RESULT0} != {RESULT1} else 'no')|ASSIGN(OUTPUT)

Question: Does the traffic cone have white color?
Chain:
INPUT(IMAGE)
LOC(traffic cone)|CROP|VQA(What color is the traffic cone?)|ASSIGN(OUTPUT)

Question: Are these animals of different species?
Chain:
INPUT(IMAGE)
VQA(Are these animals of different species?)|ASSIGN(OUTPUT)

Question: Which side of the image is the chair on?
Chain:
INPUT(IMAGE)
LOC(RIGHT)|CROP|LOC(chair)|COUNT|ASSIGN(RESULT0)
EVAL('right' if {RESULT0}>0 else 'left')|ASSIGN(OUTPUT)

Question: Do you see any drawers to the left of the plate?
Chain:
INPUT(IMAGE)
LOC(plate)|CROP_LEFT|LOC(drawer)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Does the mat have the same color as the sky?
Chain:
INPUT(IMAGE)
LOC(sky)|VQA(What color is the sky?)|ASSIGN(RESULT0)
LOC(mat)|VQA(What color is the mat?)|ASSIGN(RESULT1)
EVAL('yes' if {RESULT0} == {RESULT1} else 'no')|ASSIGN(OUTPUT)

Question: Is a cat above the mat?
Chain:
INPUT(IMAGE)
LOC(mat)|CROP_ABOVE|LOC(cat)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Is the cat above a mat?
Chain:
INPUT(IMAGE)
LOC(cat)|CROP_BELOW|LOC(mat)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Is the mat below a cat?
Chain:
INPUT(IMAGE)
LOC(mat)|CROP_ABOVE|LOC(cat)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)

Question: Is a mat below the cat?
Chain:
INPUT(IMAGE)
LOC(cat)|CROP_BELOW|LOC(mat)|COUNT|ASSIGN(RESULT0)
EVAL('yes' if {RESULT0}>0 else 'no')|ASSIGN(OUTPUT)
"""

def create_prompt(inputs,num_prompts=8,method='random',seed=42,group=0):
    if method=='all':
        prompt_examples = GQA_CURATED_EXAMPLES
    elif method=='random':
        random.seed(seed)
        prompt_examples = random.sample(GQA_CURATED_EXAMPLES,num_prompts)
    else:
        raise NotImplementedError

    prompt_examples = f'Think step by step to answer the question. \n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nChain:\n".format(**inputs)