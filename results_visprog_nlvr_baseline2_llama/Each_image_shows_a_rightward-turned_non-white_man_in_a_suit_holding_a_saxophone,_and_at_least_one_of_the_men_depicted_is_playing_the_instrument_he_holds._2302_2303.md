Question: Each image shows a rightward-turned non-white man in a suit holding a saxophone, and at least one of the men depicted is playing the instrument he holds.

Reference Answer: False

Left image URL: http://bassic-sax.info/blog/wp-content/uploads/2013/02/mac1063_garrett_pr_3_10_rgb__large.jpg

Right image URL: http://bassic-sax.info/version5/wp-content/uploads/2010/06/Right-Side-Upright.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the man in the image rightward-turned?')
ANSWER1=VQA(image=RIGHT,question='Is the man in the image rightward-turned?')
ANSWER2=VQA(image=LEFT,question='Is the man in the image non-white?')
ANSWER3=VQA(image=RIGHT,question='Is the man in the image non-white?')
ANSWER4=VQA(image=LEFT,question='Is the man in the image wearing a suit?')
ANSWER5=VQA(image=RIGHT,question='Is the man in the image wearing a suit?')
ANSWER6=VQA(image=LEFT,question='Is the man in the image holding a saxophone?')
ANSWER7=VQA(image=RIGHT,question='Is the man in the image holding a saxophone?')
ANSWER8=VQA(image=LEFT,question='Is the man in the image playing the saxophone?')
ANSWER9=VQA(image=RIGHT,question='Is the man in the image playing the saxophone?')
ANSWER10=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}
```
Answer: True

