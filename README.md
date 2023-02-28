# Mousetrap

Many X11 desktop environments ship with a settings application. Their users are pleased with an easy-to-use GUI where they can quickly configure their mouse. But what about the users whose
daily driver does not come with such a luxury as a desktop environment. Not to mention its ability to configure the mouse? Or those who happen to prefer a CLI approach over a GUI application. How to
adjust mouse sensitivity without tediously consulting somewhat low-level utilities such as `xinput`?

That is the domain where no simple yet universal solution seems to exist. There may be jury-rigged scripts living on someone's computer for personal use. However, there seems to be little publicly available.
At least, that's what I discovered after a quick Google search. Mousetrap seeks to fill that void by providing an abstraction over Xorg's low-level utilities. It will allow users to adjust the properties of their mouse in no time.
