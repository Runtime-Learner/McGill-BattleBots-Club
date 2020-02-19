# MechEng curriculum
## Preamble
Note: this info can be stored two ways. I've decided to make the following distinction:
1) Written tutorial (tut): Essentially a "textbook". A well-organized tutorial consisting of full sentences that teaches the student through written word.
2) Presenter's outline (notes): These are essentially slide notes. A reminder to the workshop presenter of the topics they should cover and the order to introduce them in in order to minimize confusion.

I initially set out to write a presenter's outline but found myself drifting into a written tutorial. In these early stages I really think we should develop presenter's outlines, and once we have oodles and oodles of time (as well as identified the need for them) we can create written tutorials. Or even Youtube tutorials. See, written tutorials might be invalidated by later decisions, but the presenter's outline will not change no matter what teaching medium we later choose. 
####
Thus, I think we should create a presenter outline.

I may not be here to teach this curriculum next semester, so I would like to get the following feedback from those who might be giving these workshops:

1) Is this readable, and are there ways I can make it more so?
2) Do you think there's a better way of me structuring this information so it can be more easily edited?

## Pedagogy
1. Audience: Members with some familiarity of geometry (i.e. degrees of freedom, cartesian coordinates, and measurement), but no prior experience with SolidWorks specifically. Members can have experience in AutoCAD and elsewhere (this will help with geometry) but much of this curriculum will be introduction to the interface, so there will be little redundancy.
2. Purpose: To enable students to be able to create simple parts and assemblies for a robot that they can later 3D print
3. Organization: (see mind map file somewhere and lesson plan below)
4. Style: Semi-formal in the way a Club often is.
####
Begin Module 1 of the SolidWorks workshops.

## M1: Overview of SolidWorks Principles

### Book Recommendation: SolidWorks Bible
1. The SolidWorks website has help, but make sure you're on the latest version
    1. Sometimes Google will serve up the 2014 version when there's a perfectly fine 2019 version
    2. Sometimes interfaces change
    3. It's written more like a reference book instead of a tutorial (i.e. hard to understand). Uses lots of names and doesn't tell you where to find the buttons it tells you to press
    
2. Tell folks that Matt Lombard's book is much easier to learn from and can be used as a complete resource if you want to learn something new. His books have helpful screenshots and definitions to help you grow your SW vocab and understand where to find all the different buttons
    
3. He has the following books (Physical AND ebooks can be borrowed from McGill Library)
    1. Mastering SolidWorks (2018) (most up-to-date, but also includes a lot of superfluous information about how to customize SolidWorks)
    2. SolidWorks Bible (2015) - interfaces might change here and there but it's still useable and keeps only the fundamentals needed to start

### Part vs Assembly vs Sketch: what are they?
As this is the first choice users must make when they start SolidWorks.
We will tell them:
- An assembly is a collection of parts
- A part is a physical body that does not consist of other parts

They can think of parts as lego pieces, and assemblies as collections of lego pieces, put together in specific ways. 

- A sketch (from part) is a technical drawing.
    - an efficient way to communicate info to others about your 3D object via 2D pieces of paper
    - traditionally used by engineers to tell machinists how to make things
    - low priority for us because the 3D printers read GCode instead of tech drawings
    - However, still useful for communicating info. e.g. Arduino standoff hole locations is given as tech drawing (show arduino tech drawing)

## Navigating SolidWorks
### Reference Geometry: What are they, and why are they useful?
This comes before Viewport commands because Standard Views is tied to reference planes.

1. Origin Point: significance and usefulness? (answers below)
    1. Anchoring point for all geometry to refer to in 3d space
    2. Can be used as a reference point when assembling this piece with other pieces in an assembly

2. Front/Top/Right Planes: usefulness and significance?
    1. Super super useful for mirroring geometry while sketching. Saves lots of time
    2. Can also be used in assembly for screw patterns and mirrors, or mirrored components in assembly
    3. Ensures that the part won't open upside-down when someone else tries to open it (can get irritating having to rotate the part all the time)

Example Phase: show several objects on-screen. Open discussion with students: where would be good places to put the origin for CADding? What would be useful reference frames? Example objects:
- A starterbot chassis
- a wheel
- an item box from Mario Kart
- imported model of a Star Destroyer




### Basic Viewport Commands
How to manipuate the object and rotate the camera around it. Recommend loading an interesting 3D model with hidden interior geometry (for using the cross-section tool) as something to look at
1. How to Rotate, Zoom, and Pan
    - Object remains fixed; the camera is the one that moves.

2. Standard views hotkeys (front, top, and side) and how to access them
    1. Note: they're tied to reference planes
    2. Can use Ctrl + [1-7]
    3. Can use the Cube viewer (but sometimes you end up upside-down)

1. Cross-section tool: What it is, how to use it, how to see inside things as well as cross-sections
    
Examples: Load up an object with hidden interior geometry (Herman wants to create an item box from mario kart with a banana hidden inside) for students to get accustomed to these viewing tools

### Other Important Setup Features.
1. Other Viewport commands (making things visible, Appearances, etc)
1. How to set the Measurement system (Imperial vs Metric)
    1. Note that we're all comfortable in metric
    2. Note also that imperial fasteners are soo much more common.
    3. Breadboards and electronics components follow imperial specs
2. Enabling/Disabling Snap-to-grid (useful in sketch mode sometimes)

## SolidWorks CADding Paradigms

### 2D Sketch to 3D Object Paradigm: What It Is
1. Primarily in SolidWorks you'll be sketching on a 2D plane and then "pushing" it into the 3rd dimension
    1. Show methods of going from 2D to 3D: extruded, extruded cut, revolved, swept, so many ways.
    2. We'll cover more of this after we cover sketching section (but you can choose to demonstrate extrude, extruded cut, and revolve if you want)
    3. In any case, this is why we'll spend a lot of time in the 2D sketching section
    
2. What's the difference between 3D mode vs Sketch mode vs Feature Mode? (answers):
    1. 3D mode is the mode SW starts in
    2. Sketch mode is for drawing 2D sketches
    3. Feature mode is activated for e.g. extrusions, hole wizards, mirror, trim, any features from 3D or Sketch mode

3. How to tell which mode you're in (this was a big frustration for me, because suddenly I couldn't do things I wanted to do)
    1. Point out existence of icons in top right: one saves work, one discards work
    2. Show how the menus change


4. (Optional) Document Properties? not sure yet.

### Sequence of Operations: Rollback Bar, 2D Sketches, Features, etc
- On the left side of SolidWorks is the "Rollback Bar" - it stores the larger things you've done and the order you've done it.
    - You have access to undo/redo while within doing things within sketch or within features
    - But for features, you use the rollback bar (sketches, features, extrusions)
    - This will be obvious: every time you create a feature, it'll pop up on the rollback bar
    - SolidWorks remembers everything you did, in the order you did it.
    - If you'll be editing your part multiple times, we recommend giving these features meaningful names. SW will give generic ones like "BossExtrude_1", "BossExtrude_2" but it'll help you a lot more if, say, you called them, "BaseplateExtrude" and "TowerExtrude"

Notes on the Rollback Bar:
1. SW frequently uses info in 2D sketches to build 3D Features
    1. Sketches are stored in drop down under its feature
    2. You can reuse the same sketch for multiple features (Double-click on sketch and pretend it hasn't been used yet)
    1. Changes in the 2D sketch will (most of the time) automatically propagate to the 3D feature
2. Breaking something upstream sometimes break everything that happens afterwards, but don't worry
    1. Rollback bar allows you to jump forward and jump back, fix the broken thing and then "Rebuild"
    2. Oh yeah, SW will ask you about Rebuilding a whole bunch. To save time, often it does incremental changes. Rebuild though, gets SW to do EVERYTHING from the top down to make sure all changes have been captured.

### Parametric Modeling (e.g. Constraints)
- SolidWorks highly encourages defining geometry through logical relationships
    - e.g. can define a mirror 

## Sketching [TO-DO]
We mentioned before that SolidWorks goes from 2D sketches to 3D objects. This module is where we learn how to sketch.
####
Recommend having two files open when demonstrating this: one empty part, one existing part. You will be explaining various functions that change slightly in the two use cases. You'll see what I mean soon:

### Basics
How can we enter Sketching Mode?
1. Start on a reference plane (for empty file)
2. Start on an existing plane
    2. Reference geometry you create yourself (advanced shortcut, is optional)
    1. Surface on existing model
3. Edit existing sketch

Basic Commands: Primitive Shapes
1. line, rectangle, circle, arc
    1. Where are they on menu?
    2. Show the different ways you can define each shape (e.g. rectangle can be corner-to-corner or centre-corner-corner)
    
1. Note: Most Common Commands are on RMB shortcut
    1. Right mouse click shortcut shows smart dim, line, box, circle (will explain shortly)
    2. Also their locations on the menu bars

### Dimensioning
Now that we've made a shape, we need to tell SolidWorks how long it is and where it's oriented. There are two ways:
1. Smart Dimensions (more on that later)
2. Drag and click (through snap-to-grid) (snap-to-grid can be enabled on bottom toolbar, increments can be edited in... document properties? need to confirm)

Note Degrees of Freedom concept:
1. Degrees of Freedom concept: in 2D plane, point needs two pieces of info to be defined
2. a line thus needs four pieces: xy of first point, xy of second point is one way
3. there are a PLETHORA of ways to define these coordinates, only one of which is p1 = (0,0), p2 = (10,0)

SolidWorks will tell you when a shape is not perfectly defined
1. Blue line is underdefined. Can click and drag element to see what degree of freedom is allowed
2. Black line is defined. SW sees no ambiguity about the element's shape.
3. Yellow line is overconstrained. There are more constraints than there needs to be, but the solver can find a solution
4. Red line is overconstrained, AND the solver can find no solution.
Note that these tend to propagate: frequently you'll accidentally add an extra constraint that seems to BREAK EVERYTHING. SUDDENLY THERE ARE YELLOW AND RED LINES EVERYWHERRRE. Don't worry though, usually a Ctrl+Z will fix your problems.

#### Smart Dimension (most common method)
This is how you dimension lengths and angles, and this is what you'll use most frequently.
1. The way you click on the line will tell SolidWorks the type of dimension you wish to add (show it in action)
2. Dimension Editor is SMAART! You can input the following: 2mm + 3.5in/2 (SW will automatically convert and store single value)
3. (Advanced) can also drive these by equations (by adding equals sign, then values are stored)
4. (Can demonstrate global variables quickly but can skip)

#### Constraints
There are SO MANY ways for you to define the location of these points. You won't use these constraints as frequently as smart dimension, but these will be important if you need to fix broken sketches or make smart sketches that respond automatically to higher design changes that you make. (Recommend opening an existing sketch for this part)
1. Explain that little squares shown on screen show constraints
2. Talk briefly what horiz, vertical, coincident, distance, fixed etc are conceptually
3. Mention that SW tends to add implicit constraints that can be overridden when you start dimensioning (e.g. assuming that lines are parallel or perpendicular)
3. Show the constraint editor: that you can add or delete constraints on your own
4. The way you define constraints will dictate how the part responds when you make mistakes and need to go back and make changes.
5. So if you're wise with your constraints, SW can automatically adjust everything else if, say, you mess up the size of your baseplate
4. Fixed point is thus a last-resort

Example: can create file with two holes spaced a certain way, cut from a baseplate and offset. Then make changes and show what stays the same, what changes
[example needs to be fleshed out more]

### Powerful Sketching Features
These are more advanced functions that can save you a lot of time and create shapes faster.
1. Trim: combining two elementary objects into one (e.g. combining square and circle)
2. Mirror: can be done in sketch mode or 3d mode
3. Linear Pattern: circular, linear, the different directions
4. Offset: creating thin features


## M2: Going from 2D to 3D
Now that we know how to sketch, we'll learn how to turn this sketch in to a 3D object There are several ways:
1) Extruded boss/base: most common. Rectilinear expansion into 3rd dimension
2) Extruded cut: same as above, but removes material instead of adding
3) Revolved boss/base: rotational expansion about a chosen axis in 3D. How to choose axis?
    1) Existing line in 3D can be selected
    2) Reference line can be created in 3D
Remember that you can sketch directly on new faces you make, and re-use old sketches for new features.

(include section on the different parameters you can adjust for each setting to get different things to happen)

### 3D Operations
(Chamfers and Fillets)
(Hope Wizard)
### Assembly Mode!!
(Choosing one part as starting assembly)
(Mates)
    (Different kinds and how to assign them)
    (Adding holes and propagating them to parts)





## Test Commands 
(the rest of this can be deleted before commit)
#####
Hello this is ime


#
I have new news
<br/>
Double! And it's new
<br/><br/>
TRIPLE
# okay hi
<br/>
Thehehehehe
Martian

Venusian

#List of Commands

# Header 1
<br/> Header 2

[Comment]
**bold text**
*italicized text*

* Hello* <br/> 
*Hello*
**Hello**

> Block quote

# Lists:
1. I am a dwarf
2. And I'm digging a hole
3. Diggy diggy hole
4. I'm digging a hole

- I close both blocks below the window
- Thing two
- Thing three

`Code thing
thing`

And we're back

![Titleofimage](image.jpeg)
[TitleLink](www.gmail.com)
