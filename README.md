### [WIP] Generate Vertex Animation Textures in blender and read them in TouchDesigner

-----------

**This is not done yet I will finish this in the next few days**

In this repository you can find the code to export Vertex Animation Textures in Blender using Python. Also the code to convert them into animations again in TouchDesigner. 

This workflow will also probably work for Unreal and Unity you just need to edit the shader a bit.

VAT's are way more optimized then keyframed animations so if you are planning on instantiating a lot of animations it is probably smart to use VAT's

##### Dependencies

---

* Blender 2.92
* Touchdesigner 099

#### Basic workflow

---

​	1 Make an animation

![blender](https://i.imgur.com/0KIPJ8p.gif)

​	2 Go in to the scripting layout in blender and import the GenerateVAT.py script

​	2 Change the parameters at the top of the script.

![script](https://i.imgur.com/zKsl5sz.png)

​	3 Run the script with the animated object selected.

​	4 Expected outcome

![output](https://i.imgur.com/tzpKmxJ.png)

5 Start up Touchdesigner and recreate this layout

6 Import the .FBX mesh and PNG images

![](https://i.imgur.com/EvA0z66.png)



7 Edit the parameters

8 Finish!

![TD](https://i.imgur.com/l10CD22.gif)

---

#### References

https://medium.com/tech-at-wildlife-studios/texture-animation-techniques-1daecb316657#

https://github.com/JoshRBogart/unreal_tools

https://www.youtube.com/watch?v=NQ5Dllbxbz4




