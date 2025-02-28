Question: In at least one of the images, all four legs of the hyena are shown, and the fact that the shoulders are higher than the haunches can be easily seen.

Reference Answer: True

Left image URL: http://farm1.static.flickr.com/15/93943570_f07794cefc_b.jpg

Right image URL: http://farm1.static.flickr.com/29/87973179_6162b940b2_b.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one of the images, all four legs of the hyena are shown, and the fact that the shoulders are higher than the haunches can be easily seen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzMaVc7gdowM81ZtbJ4yFdNuDn1yK6OG3e4X5FB/DFWk0rOAWVW74BOKw55Pocq55bI5o2k+S8GDz93oMUrwzSKcptkPJB6GumuvL0mGAiCOWSZiijLDLYyOnb1po1SzedVni2AAZIcsM1Vm9WaeyvuzkzZtGxk8vaFwMjnmrAglzvAYZ9+n+NdpPZW15bK6KHU8qynpWVcaNPKcANtHpUyTIlSktVqGjwtNaRpIG2gnn8a1NMhMVki3fzTb2x8vOMnH6UaVb+RYJGybSucg/Wr2OckewGKcdjopwUVccshQ4HyjoAKbPFG6pdOrSGDewx1Hy4NOmkjt4jLKQiKBkntVGO+s5VDJcAAsygElTweRg1pG19Spt2sjk76Lz5nkk27icqo5xVCSGXzQS37sA8Y6Gupu7GJH3onynupqm9qrISQWHoRWLunZs4ppxdrnLEwIcO24nnIAorpFsbZhn7PCT7gUU7onmOmjYqAu0bfapVc942+uKpW9whYbhz61fZ1WFinXoMHNbTg4nbTqxnsVZ7tAGYnaqckntXPy6Qkt0kYuDbzzRvO+cEKSwwoHfvmugEEbjy5MHLZw3r1qaSxSdSszO4II+mfT0qFoauzMTwzezHEcxV1IZSy/wsp4/AjkH2roVmXBySOcVBFaR2hYRcKxGc+wwB9AKcFzM0e0YIyDTepKstCwgBywbKk0pYNIABgepqEvtOwdu1OVuAcc1Axuo2lte2phuFMkbEHaGI6fSuNv7C6R5ntVD2scqRR5b5izcbR64PH4111wzH7gG9VO3J4z2rOktbj7DaQQpGDFKkh3k4Yrz29TTTCUbmFp2ozQx27XMbx28tyYD5h6sOD+ArSnikgZsn5M8YFWTZN/ZklpIEYuHLMRnls5IH1NEif6MBL8zooUsR1wOtKfvGM6SaM0vk/dH4UUxlJbKx5HrjFFZ6nLysvx9q0IuifWiivTq/CFD40WYf+Pg/7tWv4TRRXEekxg/1f40jf6yOiih7E9StL/rm+oqzH0FFFJjRDJ9+T60qdUooqUUxsv8Aq6qT/db8P50UU0SzIuP9Z+H9aKKKl7nHLc//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one of the images, all four legs of the hyena are shown, and the fact that the shoulders are higher than the haunches can be easily seen.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

