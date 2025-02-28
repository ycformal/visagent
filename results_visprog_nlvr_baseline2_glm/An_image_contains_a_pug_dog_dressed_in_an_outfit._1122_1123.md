Question: An image contains a pug dog dressed in an outfit.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/33/57/57/335757311618a8d049198e0c069e880d--funny-dog-memes-funny-pugs.jpg

Right image URL: https://media4.s-nbcnews.com/j/msnbc/components/video/201703/tdy_klg_pug_170324.nbcnews-ux-1080-600.jpg

Original program:

```
Statement: An image shows a person wearing a red hat and a blue jacket.
Program:
ANSWER0=VQA(image=LEFT,question='Is there a person in the image?')
ANSWER1=VQA(image=RIGHT,question='Is there a person in the image?')
ANSWER2=VQA(image=LEFT,question='Is the person wearing a red hat?')
ANSWER3=VQA(image=RIGHT,question='Is the person wearing a red hat?')
ANSWER4=VQA(image=LEFT,question='Is the person wearing a blue jacket?')
ANSWER5=VQA(image=RIGHT,question='Is the person wearing a blue jacket?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains a pug dog dressed in an outfit.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA5AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzOTSryLevksssZVGRvkcE9tp5oe1WF1aZY5UH987c/h6ivpfxboHhrxRof9qSW9vcykKsF3CcMSWCqCw6jJAwc4rwm50q4fWZhJeSbbOd7eWKaMcEfh9BzWEo8quxpKxknyZYgyQoBGRgqM5PoM/SseZwlyuQFV2wpPT6110lhLLjb5WFHzIo25H4dxWfJpV0FkUXLojHndtfK/iKyjKK6idjCnuLcnIkMkoz8u3C+1ek/DLQLnW9MkfHlQi4bzJCOBwOB6muHOgqYv3KguG4kDZyPSvbvhJbLpXgG6kvJQqR3krs57DalOVCnibU5bG+Gxc8LJ1Ke9rHXWGlWGkQHyI1XAy8r9SPUnsP0rk/F3jzSvC5ElwxuZ3TdDBCRllPct0A965/xXq2o+JZXt4zJBp4OEgU8v7v6n26CuG+JWn3FvqdmA0s0s9vDEqGErkKqhcevJK8eletXwKw1GNtL9F0OSli3iasnJ3831IbvxnrvibU7cwPb21yhLh8kbM8gZJPboABUz+PfF2gX8L6lqLzjgtGyJhlz0yB3Fco0MtjpsMkls0TNK6PMepcH7pPbAxx75qG786808zs7O/mDg+ijls/kK4W7anSux9K+FfFmneKbM3NkjokRUO8q7VDEZKj/d7/AFrU1Lw1DqlzNLPLtLIBHsQAoR3P97PvXm/g3XLOf4X/ANlyRyC5ZZYFEaZDE8gk/wDAq2/B/iK80lo7DU5HnsD8qSNy0P4919u3auylgViaEr2dun9dTnljJYWtFxbT7/10Kl94cv7K6aE28kgHKvEhZWHr/wDWor11YAyhlbKkZBB4IorwJZFSbdptH0cOJq6ik4Js8i1XSrKz1G+0+xma3097hmW3SVgjH2APNeceJ7KW11OZHgQRnmLZnaVPf3PrnmrvxEvXPjQGB9qwcxlDwDuPI/IflXQThNV06C7aBZyqjcgPJB6j/D3NenJanhIwPAc8tvY6k+pm3GmCIyI80bFw+SFVCvJyQcjP5ZqZ5jJH5wtmHzYZVjbCnHTmvTdJ8K6Pq+jIukvNHZyALFJCGXyz6Eng/rVHW9Ks/C89rpsVyr3EkTSupA3EA43HH5fhUSpRqaMmaVjzO4gnljBt4/KJ+8udpNeheBobmXwabGTIQXskjDOdxwuPyqnLKhbaQGx265Nd74Fs1m0d2KKv+ktn34Wt8JBUanO9bHLWhzQsizofhaEuJ7hAVB+6e/tXz1rurXd98Q5I7y7klit794w0h4jRJTtUegAr61RVRAq4wK+MvGG6PxvrMRG0LezABhgn5yf61WJrTrO7Z0YanGlGy3PZtRt9DtbSCGWFI4RJ5yRxqH347kHr941554yj0jSNNkttPsJmuJRhrqQgAeoCg4ra8Ox3Gq6B9kkdiY4wI5s8j/ZHPbArD8SaFcW2i3Vzf3RuJgyCNQc7eST+gFeZDEOc1B9DscbJlT4e2s1zrGj+VcyFIdUhSeAOQGicjnH1zXv+s+F47eYywrlG5rwr4Tuv/CWW4cDzGu4csf8AezivquaNJoyjYNelhMTOlOVtrnFiqMakVfc5XS9TudNsVtTCJVQnYWPQelFap09QSMCiu6U6Mndo4F7WKsmfL/ju5WfxZJOjFklXIJGCQWOOK3PCWoCeBLY/MxBG30xVHx5pxutZN7EhjE2WWPdu684DdyCTwe1Q+DBsN7dkEeVHgZ7E8n+VefNNaM9GLvqiyninXdC8QutrfvDBC7RQKr709Wyh45Jz7nOKi1PV7/xBrlzq93II7w7ArITtBUYG3Pb/ABNZcekz6nM0v3jNIrJgkBVGSWb9D+NXNT0bUIZvs1oHktpgP3w6Kf4s46CiDHI6TTdVbUbUT5AlRtjqMEZ9R7VwPxClceI48My/6Mncju1dzp8EWmaalvCVKjg7h1Pc15/48YNr0WDn/Rl6HPdqpkLc5rzpf+ej/wDfRppJJySSaSipKHB2HRj+dIWY9WP50lFAChiOhI/GnedL/wA9H/76NMooAf50n/PR/wDvo0UyigD6Ov8ATheWk1pcb2bsAAQ2eQRjn+dcGn2mxkutOMO4y5UuoII4xk+tehXf/Hpaf9cI/wCZrEn/AOPgf73/ALLXXOKnuc8W47FOx09LazjjV3BI+bA/IfSo/Pls32lu2cdjWrP98fRP5VmP/H/n0rnas7I0TuWlS3vI90kXlscfdbGa8x8eQC38QKqtuUwKQfbLV6dB96P/AHjXm3xC/wCRii/69U/m1JjW5ydFFFSWFFFFABRRRQAUUUUAf//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains a pug dog dressed in an outfit.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

