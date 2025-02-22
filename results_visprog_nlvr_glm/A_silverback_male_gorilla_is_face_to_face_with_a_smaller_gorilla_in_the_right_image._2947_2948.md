Question: A silverback male gorilla is face to face with a smaller gorilla in the right image.

Reference Answer: False

Left image URL: http://media.npr.org/assets/img/2013/10/03/ap132047184934-dallas-gorilla-patrick_custom-44f4e50266cf06ecb2464afdb92f394a753b136a.jpg

Right image URL: https://secure.parksandresorts.wdpromedia.com/media/disneyparks/blog/wp-content/uploads/2014/12/WLW704701LARGE.jpg

Program:

```
Statement: A silverback male gorilla is face to face with a smaller gorilla in the right image.
Program:
ANSWER0=VQA(image=RIGHT,question='Is there a silverback male gorilla in the image?')
ANSWER1=VQA(image=RIGHT,question='Is there a smaller gorilla in the image?')
ANSWER2=VQA(image=RIGHT,question='Are the two gorillas face to face?')
ANSWER3=EVAL(expr='{ANSWER0} and {ANSWER1} and {ANSWER2}')
FINAL_ANSWER=RESULT(var=ANSWER3)
```
Answer: Runtime error: 'A'

