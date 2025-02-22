Question: There is at least one ladder leading to a bed in the left image

Reference Answer: True

Left image URL: https://notreadyforaarp.files.wordpress.com/2015/07/img_00131.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/71/fc/f3/71fcf32147d28540067da069301a3266--living-in-a-yurt-tent-living.jpg

Program:

```
Statement: There is at least one ladder leading to a bed in the left image
Program:
ANSWER0=VQA(image=LEFT,question='Is there at least one ladder leading to a bed?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Answer: Runtime error: 'There'

