import random

GQA_CURATED_EXAMPLES=[
"""Question: Is the vehicle in the top of the image?
Chain:
LOC(TOP)->LOC(vehicle)
""",
"""Question: Are there trains or fences in this scene?
Chain:
LOC(train)
LOC(fence)
""",
"""Question: Who is carrying the umbrella?
Chain:
LOC(umbrella)->VQA(Who is carrying the umbrella?)
""",
"""Question: Which place is it?
Chain:
VQA(Which place is it?)
""",
"""Question: What color is the curtain that is to the right of the mirror?
Chain:
LOC(mirror)->CROP_RIGHT->LOC(curtain)->VQA(What color is the curtain?)
""",
"""Question: Is the pillow in the top part or in the bottom of the picture?
Chain:
LOC(TOP)->LOC(pillow)
""",
"""Question: Do you see bottles to the right of the wine on the left of the picture?
Chain:
LOC(LEFT)->LOC(wine)->CROP_RIGHT->LOC(bottle)
""",
"""Question: Is the street light standing behind a truck?
Chain:
LOC(truck)->CROP_BEHIND->LOC(street light)
""",
"""Question: Which side is the food on?
Chain:
LOC(RIGHT)->LOC(food)
""",
"""Question: What do the wetsuit and the sky have in common?
Chain:
VQA(What do the wetsuit and the sky have in common?)
""",
"""Question: Do the post and the sign have a different colors?
Chain:
LOC(post)->VQA(What color is the post?)
LOC(sign)->VQA(What color is the sign?)
""",
"""Question: Does the traffic cone have white color?
Chain:
LOC(traffic cone)->VQA(What color is the traffic cone?)
""",
"""Question: Are these animals of different species?
Chain:
VQA(Are these animals of different species?)
""",
"""Question: Which side of the image is the chair on?
Chain:
LOC(RIGHT)->LOC(chair)
""",
"""Question: Do you see any drawers to the left of the plate?
Chain:
LOC(plate)->CROP_LEFT->LOC(drawer)
""",
"""Question: Does the mat have the same color as the sky?
Chain:
LOC(sky)->VQA(What color is the sky?)
LOC(mat)->VQA(What color is the mat?)
""",
"""Question: Is a cat above the mat?
Chain:
LOC(mat)->CROP_ABOVE->LOC(cat)
""",
"""Question: Is the cat above a mat?
Chain:
LOC(cat)->CROP_BELOW->LOC(mat)
""",
"""Question: Is the mat below a cat?
Chain:
LOC(mat)->CROP_ABOVE->LOC(cat)
""",
"""Question: Is a mat below the cat?
Chain:
LOC(cat)->CROP_BELOW->LOC(mat)
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
    prompt_examples = f'Think step by step to answer the question. Avoid VQA unless necessary.\n\n{prompt_examples}'


    return prompt_examples + "\nQuestion: {question}\nChain:\n".format(**inputs)