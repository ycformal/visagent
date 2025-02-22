Question: A collage of 5 different shades of lipstick are depicted on a woman's lips.

Reference Answer: False

Left image URL: https://3.bp.blogspot.com/-fv3wX9H_vFE/WPsB-z22toI/AAAAAAAAZss/2ysBn9BEZ90yupurfumNInOInXBZ-26AACEw/s1600/chanel-summer-2017-cruise-collection-rouge-coco-stylo-complete-care-lipshine-swatches-review-217-panorama-1.jpg

Right image URL: https://4.bp.blogspot.com/-9NzyY3CMyyk/WPsB-VVkmoI/AAAAAAAAZso/GMZdhtUKUm01w462j-bm2A37s0u1pTrhQCEw/s1600/chanel-summer-2017-cruise-collection-rouge-coco-stylo-complete-care-lipshine-swatches-review-217-panorama.jpg

Program:

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
Answer: Runtime error: 'An'

