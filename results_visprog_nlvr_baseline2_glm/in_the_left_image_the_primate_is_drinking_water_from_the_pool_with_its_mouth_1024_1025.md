Question: in the left image the primate is drinking water from the pool with its mouth

Reference Answer: False

Left image URL: http://www.sapeople.com/wp-content/uploads/2016/03/Hippo.png

Right image URL: https://i.ytimg.com/vi/1cqwd5Y6j9k/maxresdefault.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'in the left image the primate is drinking water from the pool with its mouth' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAiAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDKvfAMhjmka+QwxgNGWwNw75PtzWRc+GNOsxCZNRhmhmZVZ43I2fNgnH0/nXpC/DWGZzLe397cb1+dRNt+nap5vAPh1LRxNBcLboAxaW+IUY75xgVh7GrHdmbxVF9fzOFtPC+g3ksYs7wu8bkkB+GA6A8d8fzrqYYp9N0xxLEirET80R+Vu+R6da0tL8F+HZ7aQ6cg8sttYw3bP0/+vV5Ph7bxZMF/ew56/MGH6is3hZz66eY/rVKLszzrULqHxAj2jWskUjSCTejAFSM8c8c1Tk04nUZzPZLdRoiqkJdnaPAyTkdiP5V6bJ8ObV/9ZqN6/BXkqOD+FRWvw0sLBme1v7yMsMHLitVhZJWRP1qm9zgLU6M8B09VaBo1D70Xdu53FSe/GMZ7j2q/oHiux0HUybS1BtbljBOskuVPYHP4nPTrXRXHgm/gnkS0E0kLEKJcY3555x71ymr/AA6eC2llmtJI405cpEW/lzRGnys2TTV0cz4zupY57ma3u0KSSeSvkSEgR4JC46AEdhxxWBpYkEqyzwAxOMKSuRxXc2vhDSpxHNfXMsMcUe/G3Lsgz90c+nQisz+0odIu3fRLLbAkhEb3HzyHHG/aeFJHtxRZWsh26sw57cxamJo5JbfcS5LptIyCBhR2+nrWppWnQySwJJHIjOypEzkhfy7Dvz+FdFrPjNPEWnWOkTxxtdHDySlgd3PAz/Dxzj2rmbaa90i+dLC9SbZuVGZfMXBGMrkcHHelGLkrA0kW5dUjtJXjlkELbmO0BiPvEZGPpRXN6t9u1DUHuJxuc4A2ggAdgKK09mLmPo9dcle3BzGpwMgnH9axtTWLVYWS8iSWJgAVPzA15gPHOuDAZ7aQDgb7dTUo+IOsgAMloQBj/VY/ka9ONakuh5jwVXdNHoel6XZ2u/7NEYPm6xkgdK1LexSG6E6XFyZV+6TO/wCXXpXnOm+O9QkSUva2p5HABHb61pDx5dp0soD9GYZo9rSL9hX6u56ULu8iQ5l5xnc7AgfpVd9TuN2Eu43cdVDD+tcKvxEuVUk6dDuPTErACq58f3TfeskY5B5maocqZP1aoe56FO9zo8EsmNzZzgg9z6U+9sbe7x9ojeULyAvavBZPj7caJH/Zsfh+Jmi/5a/aDznngbeOtVh+0NcMk3m6LI7uML/pgCr+ASuV2u2jsSkoqNj17xDZaQgcxwpDdSIobA+YIOgx25rzu88PWs9/FMkyLjcJC65OD6fjXNz/ABytZbYRjwvmT+J3vM5H4J+tZLfFqMsSNEIB7faun/jtUnG1mYSjWvdG9q3gu3ieEwNAqgZZlj+Y+lOTRbQxqPs4JAwX5Bb6+9c7dfFhLgjboxRQAABc57f7tVj8T1YfNpLfhcf/AGNZyd3odVNWiubc6aXQLSVy3lS+nExFFcufiXGTk6Qf/An/AOxopXZehjMTiowx3dTRRVlGrpbHy5eT94fyrRyfWiigka5OepqMk46miigDjNd/5DE//Af5Cs6iioEFFFFABRRRQAUUUUAf/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'in the left image the primate is drinking water from the pool with its mouth' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

