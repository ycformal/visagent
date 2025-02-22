Question: One image includes closed multi-compartment zipper cases shown in six solid-color options.

Reference Answer: False

Left image URL: http://www.orientmoon.com/21643-thickbox/disney-new-arrival-car-shape-three-layered-pencil-cases.jpg

Right image URL: http://www.orientmoon.com/21642-thickbox/disney-new-arrival-car-shape-three-layered-pencil-cases.jpg

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
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAApAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDq7MsnxC8SI5L+TLHIinsrKQw/EGtO/maxl2rZXVwhXcjwoGyPzqnrm7T/ABzd3yCJ7a+tI2DIozlcDlh1yOlSWWoxSXnneZtaKJmJY8KnfHauijZpJq5z1bptp2K7eIktmLSaVqRUDB2xBv5Gsy58b6RvKyW14jejRgf1rU0fxlpN3qbWLSi6uLiT5BEN2wY7/gMk1JqH/CP3OuJZz/ZY7kxl2UyhWx/D1PPeuqPsY39pB2Xn/mc8vbOyhNXfkc9/wmmkbgRHdD/tmP8AGm6l4x0m709oI/tKuSDloeMA/Wt3+wvDNrE0t9dQxoDwZrlVH86yLrxD8ObAkLcRXTj+G3V5s/lxVe0wT+GEgUMX9qUTrvDUiXXh+zmhB8tkJGRj+I1k33i3WIGkWx8PCVUJBkkugR+S/wCNULvxLdRRaetik+m6ZLCrojQhHILEEHrjp0HqKfZ6LeyXBuWkIzyFycEdh9K44qmpucldN9f+BY3am0op7IgTW/HGplgn2DTh2DBVJ+hcnNTCx1eCJ7rUfHE/mhCdlsQyp7k8KKjkbXG1VrH7FmxCEC63BzG5Hykr6A8GuJurTXL29Qa0Xl2sQlsg2xKR/sjg9K9CHvq0IxXol+pyySi7yk2dloXj2yt7xhqHie4vokcLIRa/uowQed4XJ5x/TNegadquma3E8mmXsN0qY3eWT8uemc9OhrgbDSrdNJt7M2sU82WJZ4woBPXI/i69TxWrpejX9rI72E72sDHOyIlAzdyexrkxFKGrej/rpY3ozb22Owa3JPQ0Vj6RrctxbS4ujc+XM0RdlHVeCM4GcHNFcfs5G/MkS674aS6giltoZVe3jEexDncoAA474xXFTy6LHvtjcbndvKnLZXYnG4EHnP8A9evXJpXjGcV4l4vvxp+rXcmpQ+aJboskyJzEg6bvXn9BVUauvYqoo78tzft9B0Lw2zappsbyXM6/uI3fG7I6dOled65oCxalc3eupM91OdzEwkjPONuegxj8qfqja3rGq2mo6dqqJHEg8mSMkqCeox6/Xg16Rbay8mgLFryW1xcKhDFI8AnHGB6+uOK7Y1G3qrrucskkrx0fY8l+waJFb7YdPWR8jLzkkjpnj8OlakMWkOrKsUxlQjyo7dcK36V1B0PR7iZZlKxRuAXGV4OPXrVqOaw05fK0m0Td0MzD/JNU61C3u3bH7OtfWyOssTb3Phi1hv7fjZny3OWX5jjnrnpXCSNqnhqfyrG7a409pCzxyp8wXH889xj6V6Todut3oVq9wQ8jKdxP1NPufDVpcqQeM15cm+ZtHUtrHlOo+O44PmQTCcrtCx4xk+p/+tSQ+M7x3VS1p5ESYuzMvCnOARx36Y9q7O/+GdjdPvOcg5wOK4LxB4B1uyDLYxGSLzGkLKcOxPTPrjt9a2jWio2aIcW5Xudrot/a35320lvlzjCMM++Pau3gTyLRVIxx3r5dube60xh5tvPDNkl2ddvPbBHNa6eKNZVobSHUrpbS5txvQTEjBUhuv0P51aftX5it7NeR7Vcb2vbhYioVHxgAdcA/1orJ8FW6weGoN5JLksM9hgAD8gKKUm4ycb7EpKS5u56fIgdSK8y8d+HJnd72BPMUg+ZHjOfevUKz9S/49z9K4zoPmySB9IuHk0uYFM5MYbCtwOmenpg+lbkuqrHcm1UeY8QBMG8bmBGTs9x/d7jpWhqP/H5cf75qnqX/ACFH/wCu0X8hXRTquMGumhlKClNPqv8AgFmz1PRrkApdIr90lG1h+dOu9bsbc+VBIs85+7GjfzPQD3qjqX/H7P8A9dG/nSW/+pl/3DXoLCxtucv1qXY4vWviT4t07WLi00/XriG1jIEccONi8AnGRnGSaof8LX8df9DLe/mv+FZPjH/kbL//AHl/9BFYdcFVJVJJd2ddJ3hFvsdl/wALX8df9DLe/wDjv+FB+K3jk9fEl7+a/wCFcbRUWNDqLj4i+LbpSs+t3EgPUOqn+lZTeINUaYTG7bzB0IVR/SsyihabAdUnxI8YRIETXrpVAwANoA/SiuVooCx//9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

