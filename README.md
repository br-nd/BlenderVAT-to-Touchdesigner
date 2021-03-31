### [WIP] Generate Vertex Animation Textures in blender and read them in TouchDesigner

-----------

**This is not done yet I will finish this in the next few days**

In this repository you can find the code to export Vertex Animation Textures in Blender using Python. Also the code to convert them into animation again in TouchDesigner. 

This workflow will also probably work for Unreal and Unity you just need to edit the shader a bit.

VAT's are way more optimized then keyframed animations so if you are planning on instantiating a lot of animations it is probably smart to use VAT's

##### Dependencies

---

* Blender 2.92
* Touchdesigner 099

#### Basic workflow

---

​	1 Make an animation

![Blender](https://i.imgur.com/Smv381t.mp4)

​	2 Go in to the scripting layout in blender

​	2 Change the parameters at the top of the script.

![script](https://i.imgur.com/zKsl5sz.png)

​	3 Run the script with the animated object selected.

​	4 Expected outcome

![output](https://i.imgur.com/tzpKmxJ.png)

5 Start up Touchdesigner

6 import Mesh / Textures

7 Make an GLSL shader with the decypher.glsl file

![TD](https://i.imgur.com/KU2TxG1.mp4)

8 parameters
![para](https://i.imgur.com/L7dDYmD.png)

9 Finish!





