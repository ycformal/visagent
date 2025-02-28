Question: Two dogs are near green vegetation.

Reference Answer: False

Left image URL: https://get.pxhere.com/photo/white-sweet-puppy-dog-animal-cute-canine-pet-portrait-small-brown-mammal-friend-spaniel-close-up-face-furry-head-vertebrate-domestic-adorable-dog-breed-friendly-breed-pup-cavalier-doggy-companion-cavapoo-purebred-pedigree-cavalier-king-charles-spaniel-pedigreed-king-charles-spaniel-king-charles-dog-like-mammal-carnivoran-dog-crossbreeds-cavachon-phalene-929359.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/0d/3c/ec/0d3cec2594feb36592a9c2502c780afc.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Two dogs are near green vegetation.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two dogs are near green vegetation.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

