# Mousetrap

Many X11 desktop environments are shipped with settings application. Their users are indulged with an easy-to-use GUI, where they can quickly configure their mouse. But what about the users whose
daily driver is not equipped with such a luxury as an desktop environment and its ability to quickly configure mouse. Or them, who just prefer a CLI approach over a GUI application. How to
adjust mouse sensitivity without tediously consulting rather low-level utilities such as `xset` and `xinput`?

That is the domain wher no simple yet universal solution seems exists. There may be some jury-rigged scripts living on someone's computer for their personal use, but not any that I am aware
of after a quick research with Google. Mousetrap aims to fill that gap, bringing abstraction over Xorg's low-level utilities. It will allow users to adjust the properties of their mouse in no time.
