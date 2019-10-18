# MechEng curriculum.
Note: this info can be stored two ways. I've decided to make the following distinction:
1) Written tutorial (tut): Essentially a "textbook". A well-organized tutorial consisting of full sentences that teaches the student through written word.
2) Presenter's outline (notes): These are essentially slide notes. A reminder to the workshop presenter of the topics they should cover and the order to introduce them in in order to minimize confusion.

I initially set out to write a presenter's outline but found myself drifting into a written tutorial. In these early stages I really think we should develop presenter's outlines, and once we have oodles and oodles of time (as well as identified the need for them) we can create written tutorials. Or even Youtube tutorials. See, written tutorials might be invalidated by later decisions, but the presenter's outline will not change no matter what teaching medium we later choose. This is why we should create a presenter outline.

## M1: Overview of SolidWorks Principles

### Book Recommendation: SolidWorks Bible
1. Tell folks that Matt Lombard's book can be used as a complete resource if you're trying to learn a new function
2. SolidWorks has help, but make sure you're on the latest version
    1. Sometimes interfaces change
    2. Sometimes Google will serve up the 2014 version when there's a perfectly fine 2019 version
    
2. He has the following books (Physical AND ebooks can be borrowed from McGill Library)
    1. Mastering SolidWorks (2018)
    2. SolidWorks Bible (2015) - interfaces might change here and there but it's still useable

### Part vs Assembly vs Sketch: what are they?
Start here as it's the first thing they see.
Answers:
- Assembly: a collection of parts
- Part: a physical body that does not consist of other parts

You can think of Parts as lego pieces, and Assemblies as collections of lego pieces, put together in specific ways. 

- Sketch (from part): technical drawing.
    - a way to communicate info to others about your 3D object via 2D pieces of paper
    - traditionally used by engineers to tell machinists how to make things
    - low priority for us because the 3D printers read GCode instead of tech drawings
    - However, still useful for communicating info. e.g. Arduino standoff hole locations is given as tech drawing (show arduino tech drawing)

## Navigating SolidWorks
### Reference Geometry: What are they, and why are they useful?
This comes before Viewport commands because Standard Views is tied to reference planes.

1. Origin Point: usefulness and significance? (answers below)
    1. It's used as a reference point when importing into assemblies
    2. Reference planes all pass through the origin
    3. Plain ol' useful to have a reference point

2. Front/Top/Right Planes: usefulness and significance?
    1. Super super useful for mirroring geometry while sketching and saving time
    2. Can also be used in assembly for screw patterns and mirrors, or mirrored components in assembly

Examples: show several simple objects on-screen and discuss with students good places to put the origin for CADding
- e.g. a Star Destroyer
- A starterbot chassis
- a wheel


### Basic Viewport Commands
Recommend loading an interesting 3D model with hidden interior geometry (for using the cross-section tool)
1. How to Rotate, Zoom, and Pan

2. Standard views (front, top, and side) and how to access them
    1. They're tied to reference planes
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

## SolidWorks CADding Paradigms

### 2D Sketch to 3D Object Paradigm: What It Is
1. Primarily in SolidWorks you'll be sketching on a 2D plane and then "pushing" it into the 3rd dimension
    1. Show methods of going from 2D to 3D: extruded, extruded cut, revolved, swept, so many ways.
    2. We'll cover more of this after we cover sketching section (but you can choose to demonstrate extrude, extruded cut, and revolve if you want)
    
2. What's the difference between 3D mode vs Sketch mode vs Feature Mode? (answers):
    1. 3D mode is standard mode.
    2. Sketch mode is for drawing 2D sketches
    3. Feature mode is activated for e.g. extrusions, hole wizards, mirror, trim, any features from 3D or Sketch mode

3. How to tell which mode you're in
    1. Show how the menus change
    2. Point out existence of icons in top right: one saves work, one discards work

4. (Optional) Document Properties? not sure yet.

### Sequence of Operations: Rollback Bar, 2D Sketches, Features, etc
- On the left side of SolidWorks is the "Rollback Bar" - it stores the larger things you've done and the order you've done it.
    - You have access to undo/redo while within doing things within sketch
    - But for larger operations, you use the rollback bar (sketches, features, extrusions)
    - This will be obvious: you'll be able to see what's on the rollback bar
    - SolidWorks remembers everything you did, in the order you did it.

Notes on the Rollback Bar:
1. SW uses 2D sketches to drive Features
    1. Sketches are stored under features
    2. You can reuse the same sketch for multiple features
    1. You can edit this 2D sketches and it will automatically propagate to features
    2. Great way to make small changes
2. Breaking something upstream sometimes break everything that happens afterwards
    1. Rollback bar allows you to jump forward and jump back, fix the broken thing

### Parametric Modeling (e.g. Constraints)
- SolidWorks highly encourages defining geometry through logical relationships
    - e.g. can define a mirror 

## Sketching [TO-DO]
SETUP: Recommend having two files open when demonstrating this: one empty part, one existing part. You will be explaining various functions that change slightly in the two use cases - you'll see what I mean soon:

### Basics
1. Ways to Enter Sketching Mode
    1. Start on a reference plane (for empty file)
    2. Start on an existing plane
        1. Surface on existing model
        2. Reference geometry you create yourself (advanced shortcut, is optional)
    3. Open existing sketch
    4. Edit sketch of an existing feature
Once you're in Sketching Mode:
1. Most Common Commands are on RMB shortcut
    1. Right mouse click shortcut shows smart dim, line, box, circle (will explain shortly)
    2. Also their locations on the menu bars

2. Basic Commands: line, box, circle, arc, different methods
    1. Each geometry can be specified in different ways (e.g. box: corner-to-corner or centre-corner-corner)

### Why We Constrain and Dimension
3. Why We Dimension:
    1. Degrees of Freedom concept: in 2D plane, point needs two pieces of info to be defined
    2. a line thus needs four pieces: xy of first point, xy of second point
    3. there are a PLETHORA of ways to define these coordinates, only one of which is p1 = (0,0), p2 = (10,0)
    4. SolidWorks will tell you when things are undefined (Explain Blue vs Black vs yellow vs red lines)

#### Constraints
1. Explain that little squares show constraints
2. Talk briefly what horiz, vertical, coincident, distance, fixed etc are conceptually
3. Show the constraint editor: delete constraints, add them
4. Talk about concept: The way you define constraints will dictate how the part responds when you make mistakes and need to go back and make changes.
5. So if you're wise with your constraints you can save time when correcting errors
4. Fixed is thus a last-resort

#### Smart Dimension (most common method)
1. This is how you dimension lengths and angles
2. The way you click on the line will tell SolidWorks the type of dimension you wish to add
3. Dimension Editor is SMAART! You can input the following: 2mm + 3.5in/2 (SW will automatically convert and store single value)
4. (Advanced) can also drive these by equations (by adding equals sign, then values are stored)
5. (Can demonstrate global variables quickly but can skip)

### Powerful Sketching Features
1. Trim: combining two elementary objects into one (e.g. combining square and circle)
2. Mirror: can be done in sketch mode or 3d mode
3. Linear Pattern: circular, linear, the different directions
4. Offset: creating thin features


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
