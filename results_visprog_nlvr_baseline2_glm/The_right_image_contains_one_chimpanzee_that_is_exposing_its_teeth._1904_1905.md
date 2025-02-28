Question: The right image contains one chimpanzee that is exposing its teeth.

Reference Answer: True

Left image URL: http://mmafitnessclub.weebly.com/uploads/1/8/2/2/1822368/gorilla-teeth.jpg

Right image URL: https://listverse.com/wp-content/uploads/2017/03/feature-6a-angry-chimp-122203715.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains one chimpanzee that is exposing its teeth.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAiAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCV9ZhS1eSS68uYgiW281jI+B0yM8DrxXC6VruoR6lcW+mlnhnyPKjdsYOcdTn8TWteaNfaak12beEFYwUjaZW3MM5JB7e3eovDdjZ2th9uijl+1plJmk6bCcgjHA6EY6141CEJvlet/wDhzOKuXXW4jt44Dr0dpKq7Us4Ygie+cZz+IxSDSbO9mgjsdZWa7LNJfTHGxRkcKn3iQMgEfpWLb2+lX2tbbx5zcPIT8jcEdgeMgduM1s6rocPhaSLUrO1uoSXULJMcZ9R9D05r0ZYWCjaCsy+S+xsXXg2C41GGWxuVs54Q8sc0jsRJzj5j1B9veq2iuNI0yWLXLyO3iix8qylyRyQMDpkkevQ1evNQtLzS4bh1ljRLlQGUExOjD7pHQE+2O9c/q1zDfRzR3kzYjT5m2/eYdBnrxmvMire6lt3uzF32O0ssXljFLEB8w3A4wMfSqWr6vHpsYih3PdMcDy1ztHcn0o0K4tbHwtZ3DSZSKHOd3bnj3rh4tetrvVbie8/dBpSyNycDsCRXbh6Sk7vY6FayOjnmgin3SGW4uH685x0z/hVa4vbyV/m2pGuQAp5/OnRO4kZQQxA3ZAyTn0rpTZ6LHp6G91SKGeXaVigQu5LDIzkYA57DHvXe5RSsaQpSlscvbeILvSbdbuD/AEq1UbWRn+b9e9dXpmr2+uWou7dsqRgqfvKe4Iry7xFcrp73NgrDJuM4AxwAMn6E1T0LxRP4bvxIA0lrLxPF3I9R71zVqKmrx3Jatoexu6I2CCPTjNFQ211bXlulzbSiSGVQ6MOhBFFcOoWMsTWenTS3V35Yvn5CodwcZHIDDGMfw1DrLNc6ReTshtmkkbKpjEjZ4Y/jn65rCXU0urPN1udo2BVVmJjb6rjr69M1iTa3eXcj2ckhWI/LGq8be2OK2weGlFRlJ7fj5mMYmItxc/2sJ7RitxGd6HGcMrA5+g60ySDUrS1k+07lEkyoxz1OScH8RVy4tbvw1f213Cd0kDF9xGRz2+napZ/EFz4gkgsvJhjgSbziqIB831rukm5Jm8XHlae5qnXYZ7a1sfssLQxKGwzkZYcbsDvS/b7eWQwz/u4JJA7EnOD25PRe9Y2u6fc2jJNHAURuccdfb/Cs2CG7aMsUOeoG7kj6USpRkrWM2kep+IZPI0vSrZyiiQsZBHjaSOmAOMc5rnLqygttMJhP793z04x6Vx994q1Yx29jI8eyyysWYxkfU96gk8V6pKu13iI/65iilHkhysDrNP1a5s9egaUMYAMMRyFHbPtmvZtNGkXCR3gmtYoUiJZJWGQccYz2zXzRH4k1CNmYGIlhg5QUw+ItT2siXBjjbqicL+Xam1c3pVnBNHZ6/Hb3uo313GwLSSMyEnqOn9KxLu2hubW3VZAkvQgDJNYD6rdOqqSoCjAwuKS31O5tpGkQpvb+JlyR9KaMpO7ud9pXiC78M2f9nLslQMXUyA5UHt9M5P40Vwv9tXp6y5+ozRWbpQbu0K52dux89hk4ELEe3NUemprj+8P50UVpH4UHU2dRAe1nLjceOTz2rn/DQAupyAAQDgjtRRR1GaGqM0lwnmMW4/iOayrckXcOD/EBRRVCMbXABrd2AMDzDWfRRUiCiiigAooooAKKKKAP/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains one chimpanzee that is exposing its teeth.' true or false?')=<b><span style='color: green;'>fake</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>fake</span></b></div><hr>

Answer: fake

