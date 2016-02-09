#SingleInstance, force
CoordMode, Mouse, Screen
SetDefaultMouseSpeed, 0
RControl & 1::
jumper(1, "Enter")
Return
RControl & 2::
jumper(2, "SingleClick")
Return

jumper(position, action)
{
MouseGetPos, xpos, ypos
sendInput {LWinDown}{b}{LWinUp}{Right %position%}{Enter}
Sleep, 100
if(action = "Enter")
{
}   
if(action = "SingleClick")
{
MouseClick, left
}
if(action = "DoubleClick")
{
MouseClick, left, , ,2
}   
if(action = "RightClick")
{
    MouseClick, right
}   
MouseMove %xpos%, %ypos%
}