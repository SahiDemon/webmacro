#SingleInstance, [force|ignore|prompt|off]
MsgBox, 64, suspended, >>Script Iniziated!<<, 1
XButton1::Send {left}
XButton2::Send {Right}

F12::
    Suspend, Toggle ; Toggle script execution on/off
    if (A_IsSuspended)
        MsgBox, 64, suspended, >>SCRIPT SUSPENDED<<, 1
    else
        MsgBox, 64, resumed, >>SCRIPT RESUMED<<, 1
    return
