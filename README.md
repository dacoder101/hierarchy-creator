<h2>This project has been discontinued and I do not have any plans to revive it.</h2>

<h1>Hierarchy Creator</h1>

<h3>This project has been put on hold and will be completely redesigned.<br>I practically jumped up a skill level in the middle of the project, and wasn't satisfied at its current state <i>you could probably tell because i was suppost to complete may 1st</i><br>Anyway, I will be starting on pyos3 and returning to this later.</i>
<hr>
A python program allowing for custom hierarchies all from the CLI.

One of the most time consuming projects I've ever tried.
This will also be integrated into my upcoming "pyos3" project.
<hr>
<h3>Known Issues</h3>
<ul>
  <li>Random text sometimes appears at input and styled text.<br>This text is ASCII related to styling text.<br>I cannot fix this as I am using a module to make things much easier.<br>(Simply restart the program if you see such things, it doesn't usually happen on the released binaries.)</li>
  <li>Menu's and inputs don't output any response, or are entirely skipped.<br>For some reason, the key() function (for awaiting a keypress) is entirely ignored.<br>Can't fix because I'm using a module which allows this. Not sure why this would happen either.<br>(Simply restart the program. I have only seen this issue on Replit.)</li>
  <li>When deleting the last hierarchy, the No Hierarchy menu appears.<br>Tried fixing, ran into many errors.<br>Implementing this will make the already bad formatting even worse.</li>
  <li>Files and directories cannot have the same name.<br>I cannot fix this because of the way commands are written.<br>If you attempt to do so, you will be noted of this.</li>
  <li>Using " " and ' ' in arguments does NOT work as expected.<br>Because I use the .split() method to split spaces, using quotation marks will not allow you to have directories with spaces.<br>Along with that, using quotation marks as file names and directories is allowed (because I can't figure out how to fix it) but is extremely confusing.</li>
  <li>The code format is just bad in general.<br>I don't plan to revisit this after it is completed.<br>If you want to reformat the code (greatly appreciated), create a PR.</li>
</ul>
<hr>
<h3>SRC Confusion</h3>
<ul>
  <li>Why are try and except statements around inputs?<br>I did this as simply entering CTRL+D or etc. immediately crashes the program.<br>I wouldn't recommend doing this though as it is extremely annoying to debug.</li>
  <li>Why are variables of escape characters declared in func.py?<br>Because of limitations of f-strings, you are unable to use escape characters inside of arguments when calling functions in an f-string.<br>This is also why string arguments inside of f-strings are using ' ' instead of " ".</li>
  <li>When creating a Hierarchy object, why are both arguments the same value?<br>The name and dir parameters are similar in the fact that they are both using the hierarchies name, while dir is a directory that can be used for other operations.<br>But why not just pass the name into the dir automatically?<br>[I realized I should have done this now, but] incase I wanted to specifically start the directory within a folder in the hierarchy.</li>
</ul>
<hr>
<i>If you don't plan to use the release, run hierarchy.py with func.py in the same directory (preferably isolated in a folder).</i>
<i>You will also most likely need to install this package.</i>
<code>pip install console</code><br><br>
<b>Note! The source code uses operations designed for Unix (also works with macOS)!<br>Even though EXE releases are designed for Windows, if you plan to use the src you will need to convert the "clear" statement used in the cls() function in both hierarchy and func.py to your native terminals clear statement.<br>(This would be "cls" for Windows!)</b>
<hr>
<b>Plan to use PyInstaller yourself? You will likely run into an error.</b>
<b>For some reason, you need to install a package </b><code>pip install future-fstrings</code><b> which should stop any errors you are facing.</b>
<hr>
This project was developed on and can be found at <a href="https://replit.com/@bobbypac/Hierarchy-Creator" target="_blank">Replit</a>.

<i>Want to contribute or have a suggestion? Leave an issue or PR!</i>

<b>The next release is the FINAL release! Pyos3 will begin soon after.</b>
