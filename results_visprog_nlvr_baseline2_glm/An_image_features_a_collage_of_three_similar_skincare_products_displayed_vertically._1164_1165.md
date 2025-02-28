Question: An image features a collage of three similar skincare products displayed vertically.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/236x/c7/af/33/c7af3377d2116b8ed75054ff783bfb34.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/236x/a1/c7/78/a1c778f466ee8f95064147b0ac862706.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image features a collage of three similar skincare products displayed vertically.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABkAEYDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+mSuscTOxwB3p9Zmu6jb6dYF7hmAZgFCjJOOf5CpnLli2VGPM0kOtdb068miit7tJHkUuqjPzKDtJ/MYrRry3w7f21jqWnTTTApHbSRNtBJBMrPn6YIr1EEMoI6EVnRq+0TuXVpuD1K9/by3VnJBDcNbu/HmKMkDvj3xVeSzlhjZ21S5SNASxOw4A56la0aw/GTzJ4O1b7PjzmtnRMnHLDH9a2Mjz65+MGj2t4fKn1W8XoAYkjT654Nd/wCE/E0HinSTeRRGF0kMckbMGIPUHI9QQa+dofA2t3zAxJaenNwor2L4XaFq+hLex6ikKxSpGU8uQNlhkHp7EVCkmx2PRaKKKsQVheJLBNSW1tZJGjVnc7lHT5DW7WbqiqZ7TdnG5+n+4amSTVmVBtO6ORHhG1t4WkS+kcxRuQNo54rvYf8AUp/uj+Vc/IsX2a4w27905HHsa6CL/Up/uj+VTCEY/Ci6k5StzMfWR4pQyeGb9R/zzz+RBrXqG7gW6tJrdukqFD+IxVvVGR5hpNvaswLRxZ7kgdq7/R1ClgoAUKAAOgrgLO0ltbx4JQkciNgq8fP869E0eExWQZl2l+gxjjtXPTXvGknoaNFGaK6TMKztSAa4s1Pdn/8AQTWjWL4gu0sjaTOxUB3GQucHYe1KTsrlQV3ZEd0kC2VyyYysbZw2ccGtuL/VJ/uiuFfXbH7PciKdmNwjEgQkZO3Gck8dq7qL/Up/uj+VTCSlsVUg47kN47IsYRiCzYJHpWOby4F1MTO4iQevArQ1mf7PZiTuDgflXJamtzPoV1bW8qx3FzEyq7dFLDAJ/Os6jsy6aujze++N1/F4kYw2sE2kxy7cuD5rL3YN29QMV6smsvf2MVxaXcjRzIHRlbqD0rxCX4V3EWnjdq8Pm+YQf9Fk9K7XwrbXWl6TFYT3Ale2+QMmQCO3Wpc0/hZfI1ujS1SLxEZ91r4gv4uxUSZFFadvKNxLknjvRRzMXKjr/wDhKfD3/Qd0z/wMj/xrn/FmraRqdjClrrelMySEkG9jHBUj1r42zRmt5RUlZmEJuElJH0uVtSsa/wBq6UMDBP2+L/GvUE8UeH1jUHXdM4AH/H5H/wDFV8MZozUU6Sp7GlWtKra/Q+19X1fTNTigistSs7krJvdIJ1c4weSAemcVj3s2xAT1JH5V4d8E2C+JtQY44sj/AOhrXr99OdrH72DtHuazqq7KpOyTKd9reHEQC8cYMoGfwqlYXn7ybP8AewKzb6V/OOEVm6bhSWcnljrkk1jCNjoqSTWh1cM24bqKzbWbch9BRWhkfMtFFFdZyBRRRQB6l8DLcXHiu/U54s88H/bWvb9T06wtYGlnaSOKJDlt/QYyT+Wa8V+AjbPFepP/AHbA/wDoa16z4xs73WdGuNPs5ESeWPaGkJCjPXOPbNYVLX1N6d7HjU/jpm1oy/ZV/svzMeSCfM8v/f8A73fpXrVloWj3llFdWskxjkUMp8zsR9K85u/hDrENjC7ajp+45JwX/wAK67wlb3WmaTHY3UiPJb/JuQnBHbrU80XsXyyW5tHRvKGIJGUZ/i5oq/HLlBxRSA+SaKKK6jlCiiigD1T4Ff8AI06j6fYuf++1r225faGc/wARxXhnwSYp4k1Ijr9iwP8Av4teu6tqNvACs1xHGIhnDOASx6D+tc1VXbR0UdLGbrOuMt/FaoG2hACdnfJqlY3R+0z+5H8qyNT1ywa680N5sigqrICePr0rNi8QGHd5VuWd2zlm/oKypwfY6qibWh6BDdFiRnGKK4CXX9WhPKiAE45i/wAaK25WZ+zZ43RRRXQcIUUUUAdJ4Nmlh1C48qV490ODsYjI3D0rqXJJBPJPJJoorOW534f4CF+tICQQQcEciiikjYnmup7n/XzPJyT8x7miiigD/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image features a collage of three similar skincare products displayed vertically.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

