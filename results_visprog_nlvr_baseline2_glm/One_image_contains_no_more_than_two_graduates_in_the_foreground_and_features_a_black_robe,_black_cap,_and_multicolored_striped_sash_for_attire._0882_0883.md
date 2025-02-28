Question: One image contains no more than two graduates in the foreground and features a black robe, black cap, and multicolored striped sash for attire.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/05/1e/e1/051ee1d7aa816f9a8726ceceb96c1cd4--graduation-serape-graduation-caps.jpg

Right image URL: http://globalclubwvc.weebly.com/uploads/5/3/6/2/53624823/6921869_orig.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image contains no more than two graduates in the foreground and features a black robe, black cap, and multicolored striped sash for attire.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAuAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0+JTUyzxC4Fv5sfnldwi3DcR6464rM16S5h0ZxZ3P2a4kkjiSbYHKbnC5APBPNeP6b4QuJPFtvNqV7cXM320pJIHZZJFDEbt4OR0zgfStJSS3LjTk1zI96FZeu+JtJ8NW6zardGFW+6FjZy30wK0ohtULkkKMZJyfzrA8b2pvNAKEIYEbzJd/TA6DHc57UpOyuKEeZ2G+GvHeieKp5YLBrlJkPCTwldw9QeR+BOaZ8Rx/xbnXz/06H/0Jai+H8VvHDdm2WCITFC0UShckA84HXr1rS8d2hvfAus2obaZbYqGI6fMKSkpRuEoOMuU898STXOqeDvscFnMzzLCsOQP3rYGQB1/xrz2z0C/e0tr6BDIk9zIvkRrl18n5mPPbqOtaqeJL6z1UNZq8sdlcLIgBO1okUK/PpgA/jWhbalaaf4pudPSbzNEMt2fMRvkeN48ZyOwZU56ZrGNNtaluaLMev2xkwJMseQoxmp7jV1gkMdwkkUgyChwdv1IyKydCurLVIP7Mn+0JcSabNA1wspwgRWkQBemWI5z6cYql4ft5bPwg981xIiz6pBbNtPQKpdm9jnAz9aPZvoP2iNR7zUNdv9JvY5beK1mu3tEhQEbSq/ebHBz19eK0mnZLw2sglMquyDbGSrMOoBxz2496zLLWV1ax0yKaZbeSPWPNuJeIkihbJX5s9eZT/wDrFa32nULmG6e3m8qV/E0UUL7cmMSbyefoF/KnKEm73CMoxVrHF3Wp3ou5le5WMq5Gx5Rkc9DzRW5Loen6zfX1zLHOki3U0bFVDb9rn5jlhzjGcDtRUaLRlOMpO6R6H4z8c2HhmW1s5bVru5nAkEfAVVB4Yk98jge1cImuG3tf7XDu03ni4jIICs5b5kJ65zk4/ukVQ+JNw4+JFhIoWQpbxMqP93IZjg+1WP8AhJZLm/BudDsrhliYm3jIWLBI+fH97t9K0qOPMua/yt+rN8LRnODcYp692vls9+56Z4U8bWPii0mkhSS3mgYLNFIQduehB7jg/lXmqeJj4j1i5v8AVvEMlpFbXJFvZqhKGP6D19TzWf4X1Aacvim6hi8hS4Cx7s7OHOPwrG8LWmlXcF02o6ubJ1lAVRHu3DHJ/OtVeStFX+V/wOZKEZ/vHZLz/Wz/ACOo1PWLFdDmibU7430UZZGtAEids5XcR6DA+ortNB8QXWtfB69muHkuby3R4GY8u+CpUn1OCPyrzK8n8Pz+HriX/Sl1IxlVWJdsBYHAOPQjB+tb/gPWzpfw28UT+WszWjJL5TnAbcqjn8qSp8kbWt936frqE5xbTg/z/X9NDlljvvtIggWVBOshK8qORg9fUZ/Kq9vZzSXE0ETBJBA+/nggLyMj1x071db4rMzln0C0Y9OZWpV+K+xi6+HLEMwCs285IHQHilfQy6lW4ttSjt1nCsP9GjffG2CqngDjHOOKr6et1JpcscbSfZkUSyoGO0kHAOO5Ga0v+FrruVj4asCyncCXY4PqOKcvxa2psXw3YBORtDkDnr2pIbauV7jS71gJi8cksk4iMatmTdgAZGOO1EEutW0ctyJ7q3XKOZFc7fMDZ3fX3qwfizuj8tvDlltzkYlYY/IVUl+JFvMjI/hmxKN1XzWwfwouF0dTo93f/YjNLBNI88jSlkiOCSf8n8aKwE+LUsaLHHodqiKAqqsrAADtRUOCZssRJKxJ4wurWb4oZvEeS1hSJJVjPzFduSB781Kr+DpNVbMeowWnkDGDlt+48/TFYs8cmu/Ea8iVxG8106BmGcBQQP8A0Gty38FXk2sXFol7CHit45CxQ4IZmGP0reNH2mvLf5tfkVTxFKiuWdRxe+iTVu+vU5+GeOG01wW7MYGkwhbqV5Az74qTwla2t1b3JudYg087xgSpnePUUmnWyMl/bTAOPtLI/YHHFM1C9k0vU3itwoTyo8AgHoMdxUpuL0/zMnyt3bdvLR/kzQltNNXwlJKuuq11hj9jA6/Nx+nNHhu5MfhPxpaOCplsUkVSMZCuoz+TVgnUZnsUtePLJ24wPXPpXrepCOb4Km5aJDMulKiyFRuA3KCM9ccVV29/yIly/Zv83c+fz1NFB60VmSFFFFABRRRQAUUUUAf/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image contains no more than two graduates in the foreground and features a black robe, black cap, and multicolored striped sash for attire.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

