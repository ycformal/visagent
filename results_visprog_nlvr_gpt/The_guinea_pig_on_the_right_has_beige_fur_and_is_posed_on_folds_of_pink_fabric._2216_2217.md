Question: The guinea pig on the right has beige fur and is posed on folds of pink fabric.

Reference Answer: False

Left image URL: http://img-aws.ehowcdn.com/360x360p/photos.demandstudios.com/getty/article/39/102/skd187616sdc_XS.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/56/55/22/5655224ee0f68630d68ffbb3565e7e7a.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='What color is the guinea pig's fur?')
ANSWER1=VQA(image=RIGHT,question='Is the guinea pig posed on folds of pink fabric?')
ANSWER2=EVAL(expr='{ANSWER0} == beige and {ANSWER1}')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Answer: Runtime error: name 'beige' is not defined

