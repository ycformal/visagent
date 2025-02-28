Question: One image shows exactly one white rodent lying down on the belly on a pale wooden floor.

Reference Answer: False

Left image URL: http://24.media.tumblr.com/tumblr_m3pfdpGIvE1qdedm3o1_500.jpg

Right image URL: http://www.catexpert.co.uk/wp-content/themes/shopperpress/thumbs/Beth-the-hamster-is-getting-used-to-life-on-three-limbs1.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows exactly one white rodent lying down on the belly on a pale wooden floor.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAsAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDzrQ9CtdTsS7ywQCOMNIzqM4x/PrXRWvgCKaS2QeXNFKm/csYBQe5rmtCjuJZLZLcHJRQ/GRtOOteqayddj0Iro9vm7by13KANijHr2AFcdSck+VPc9icFGXMuxxl98O/stwqlV8hjkSCMcex4/WoL7wGlq0YjhWUSvtVicL+eK9k06xmutDtm1ADzzGGlUdA3f9a5ayOttr2pW93b/wDEvi2/ZWAGDjI/OsI15667CujziDwRJqMuyzit5VdhGrxNjYxOPmVuevB/Ouj8MeB7rw9rt3b6ikJuBDFKnlNlQrFx+fy13HguPTPtOo28MLJe28nz7+cBsn5fbqKtPDu8aX2RnFlbf+hTU44uU63suljmrRtAnstOVFHy1djMIu/siN+/2b9oHarsMWBzVTWILl7Gf+zrhI9QaBhCu7aWbsT3xWsvdVzCnHmdjQW2lSLzMAYHG4023t0uVDS8nuc1z+g6hqkdtaaVq0onvI4w1xIWzjJOAT3Na8E4tLoo7HYyk7fQ5/lWMql3bodMaVl5ktzA1ph1G6H+JfSotRt1jtm8sAkjrVq91K0tYVad8eb8iDHWolgmvbH96GjBHyjvj3qlUfwjjSV+ex5Pq0gGoOHCMR6iitrU/A11c38ksV9EFPZ0OR+VFUpQ7ltT7GPoPhQ6bounzxzGaWa3iuThcbdy52j8K9BsVSa0SQjy5FXDbh/Wsvw8s01hoEceMf2dASW6Y2Cu5ksdsJ5VhjnNc6ftNZCnJo5iRrmBhBHvmjl/1LxsCCevXNWI7EKz5cTY5YLzz6VFeeBdK1K/ttQfT4mZPmJUlQ2fVa6O3sbazaO3jQISpIIAwMdgO1XKEWtBSqaKxxNroot/EqX6kxSzNggHqPerc7pF41vd7qubG26nGfmmrcudNLams/mlgg+VccA8814J8dJGfxlYMeD/AGdHnH+/JUUoXxCfkZVZXpnvcVxGVGJY/wAWFZt+yC7fULSG3kvBCYElQguVznAPYZr5H3t/eP50u9v7x/OvQlR5upjSqxhurn03ZaT4hm1N766FogK4WPz8En1J5rej0q6uIkN3qcUMinlbfbz7bm/wr5G3t/eP50b2/vH86z+qLubPGPsfZEem2kOx2b7XKvAeSRfkHt6VfuL6CGIs0sYwOm8V8Ub2/vH86Te394/nT+rW2ZLxV90fUdx4ltftD/6RH1/vCivlzJ9TRUfUl3L+uvsfUWj3CWnh/wAOyuQC9lDGCe52Agfoa6aTxLZy2yiGaMF/lOWGQO/4184XvjzVr3w1FpkkdqsNvDEsTIrB124AOd3XiqUnjLVLiMNIsBkKgM+w5b3PPWsKVCSWr6s0coux9Mx+L7GCeOxVzcFRtaSPkJ6BjWPqvimCPWJGklPkhF8sKvKOD69/5V4j4c8fano9tNDDa2MqTNl/OjY5/JhU974/1G5vY5HsdOGzkARvg/X58mtHTd7EqcVJ6H0Xpt4dVzcbCsR5XIxketfPnx1ZW8cWwXotio/8iPW1F8ZvEVvb+VFY6UqgY/1Umf8A0OvOvG3iK68TazFeXcNvFIkAiCwKQCNzHJyTzkmijFqqjGrJOLsc3RRRXoHKFFFFABRRRQAUUUUAf//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows exactly one white rodent lying down on the belly on a pale wooden floor.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

