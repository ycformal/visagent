Question: Has this plane taken off?

Reference Answer: yes

Image path: ./sampled_GQA/156445.jpg

Original program:

```
ANSWER0=VQA(image=IMAGE,question='Has this plane taken off?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question='Has this plane taken off?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDW88KKBPVLcTSgnHJrA2LXngt15p4l3VTDAHpTxIo7UAW8c8mnZAqn5yn1oMoAzyfYdaBk01zjgVWMkp7cVjXWtQSyYtbx4WBwVeMZH170231a7DYlWOeP+9Fw35HrU3NFC6umjcC5GWNIVVeRVJdVtGyHl8sgZIcEEfnUwnhlXdFKrj1U5pp3E4Sjq0SF8VBJLjtmmu4Az0Hqax9X16DTrVjG8Ms54VN4wPc89KZK1di+zlmzg0Vm22trNaxSSW9yZGUFvJgdlB9jjmimB0AyR6Um31ekEwApPNz6UECk46ZpQc9aYZPam7ie9MCXd70b8VDz70nzUAVNZjgNlLctp6Xc8a5VQBuP49xXFX+oW1qkUunSXG9yA0LkMVJ9PXnivQDwKi8pNxbykz3O0ZpWQHESa/qdy0CGOZTaSrI6CL07MMfoajvtWl1G5iWyxYPz5jiTyw3/ANeuwitpotVuLtrt2ilRVEGwALjvnqe/51Hd6ZY3t5Ddz24klhBCZPH4joadkO7tucxZ6bZXEatqOo3E0hPO2T5R+fWoptG0yylDyXaz2spxjYVdfyzmupfStPY5NjAPouKb/ZtipytpD/3zSaurXHGXK72HLq0LKPLhu2UDAItnx/KipVwihVG1R0AFFOwrl0OBS+aPUVS88elIZwewqrEXLvne4oMw/vVQMy9OM0nmj1osFy95/wBad51Z3m+9J5vuaLBc0vP96aZ896z/ADR70hlHpRYOYvNKPUVE0o/vCqZlFMMtFguWzJ/tU0yf7X6VTMxFRNcgLuLAL654osFy6ZeepoqgZjminYLjX1azjIDXUQP+9mol12yZsCbI9QpNZgkjDZWNB7YjA/lTxcMTwHA9nA/kKy9r5FchKviONpWyhA52n+WaG14vLGY4ptgPzgRk5+lQgTtITmQpx8vzk/nUvkFxg28xB92H9aXtfIOQQazeIzkWVxKrNkZQjA9KVNY1ABS2nOwI55ApRbOOlp/30w/xp3kP/wA+9uv+84o9ox8iGNq+oHhLFVbrzIOn50NqGrMuRbQJ9ZB/jT/LkX/n1Htk01o27vbf9+yaPaSDkRC15qyIS0tr65yKhe+1TnN1aLn3H+FWSp/57oP92EVG2wdblvwVRRzyHyxKxn1Ns7r+L/gK5/8AZarG3uvJ8k3reXx8oU44q6zwd7iU/wDAx/So2a39XP1kNLnfcOVdii1jIzZa8mJ9cH/GirRe2B/1Y/76P+NFHO+4cq7G4zlPuhR9FFM+0S/3yPpRRUFCedKRzI3503ex6sfzoooAikdlXINU5LmYE4f9BRRUyYmQ/aZm6yGk82Rurt+dFFZtsRIEUrkjP1NO8mPn5BRRWd2bRSGsiqThR+VVZmKnAwPwooq4BPYg3t6/pRRRWtjK7P/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Has this plane taken off?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: no

