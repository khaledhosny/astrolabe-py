#import "@preview/rubber-article:0.5.0": *

#set page(
  paper: "a4",
  numbering: (it, ..) => [
    _MAKE YOUR OWN MODEL ASTROLABE_ #h(1fr) #it
    #line(length: 100%)
  ],
  number-align: top,
  footer: align(
    center,
    text(size: 8pt, weight: "bold")[
      #sym.copyright 2010--#datetime.today().year() Dominic Ford.
      Distributed under the GNU General Public License, version 3.\
      Document downloaded from
      #link("https://in-the-sky.org/astrolabe/index.html")
    ],
  ),
)

#set heading(numbering: none)

//#set text(font: "sans-serif")
#set par(leading: .7em,  justify: true)
#set list(indent: 1em)

#show link: set text(blue)
#show ref: set text(blue)

#maketitle(
  title: "Make your own Model Astrolabe",
  authors: ("Dominic Ford",),
  date: [2010--#datetime.today().year()],
  metadata: true,
)

Astrolabes are elaborate astronomical instruments, combining a mechanical model
of the sky's rotation with a simple sight, which can be used to make
observations of the elevation of objects above the horizon.
Put together, these
tools allow the user to tell the time, identify objects in the sky, and predict
when objects will rise and set.
In the Middle Ages, astrolabes were the most sophisticated astronomical
instruments in widespread use, a position which they held for nearly two
thousand years, from the time of their invention by Hipparchus (c. 190--120
BCE) until the turn of the seventeenth century.
They only fell out of use
around the time that the telescope was invented in 1609, as astronomers began
to require more precise tools.
Today, the curious astronomer who wants to learn more about medieval observing
practice may find it hard to find a specimen to play with.
Historical examples
are highly valuable, and usually found only in glass cases in museums.
To solve
this problem, I have created a cardboard cut-and-glue kit which you can
download and print to make your own model astrolabe.
The design presented here is based upon one described by the English poet
Geoffrey Chaucer in his Treatise on the astrolabe, published in 1391. In a
series of three papers published in 1975--6, American historian Sigmund Eisner
provided detailed geometric instructions for recreating Chaucer's astrolabe,
which I follow closely.
The design of an astrolabe depends on the geographic location where it is to be
used, since different stars are visible from different places.
I have created
kits for use at a wide range of latitudes, which you can download from
#link("https://in-the-sky.org/astrolabe/")

The astrolabe presented in this document is designed for use at a latitude of
{latitude}.

= Assembly instructions
To build the model astrolabe, you need to print, Figures @mother_back[],
@mother_front[] and @rule[] onto separate sheets of paper, or more
preferably onto thin card.
Figure @rete[] should be printed onto a sheet of
transparent acetate.

The two sides of the _mother_ (Figures @mother_back[]
and @mother_front[]) should be glued rigidly back-to-back, perhaps
sandwiching a piece of card to given them added rigidity.
The _rete_,
printed onto transparent acetate#footnote[Historically, the rete would have
  been made of the same material as the rest of the astrolabe and marked with
  arrows showing the positions of prominent stars.
  As much of the material of the
  rete as possible would then have been cut away to allow the climate below to be
  seen.
  We use transparent plastic here because it is so much more practical than
  the traditional form of rete.], should be placed over the top of the _climate_,
on the front side of the astrolabe.
For simplicity, the climate is
incorporated into the front of the mother in this document, rather than as a
separate component.
The _rule_ and the _alidade_ should be placed on either side of the
astrolabe.
The rule, marked out with a declination scale, should rotate over
the front of the mother.
The alidade should rotate over the back of the mother.
The two tabs on the side of the alidade should be folded out to form a sight
used for measuring the elevations of objects above the observer's horizon.
The
whole construction may then finally be fastened together by placing a split-pin
paper fastener through the centre.

= How to use your astrolabe
For more information about your astrolabe, including step-by-step instructions
in how to use it, see the author's website,

#link("https://in-the-sky.org/astrolabe/")

= Customised astrolabes
This astrolabe kit was designed using a collection of Python scripts and the
pycairo graphics library.
If you would like to customise your astrolabe, you are
welcome to download the scripts from my GitHub account and modify them,
providing you credit the source:

#link("https://github.com/dcf21/astrolabe")

= References
- Ford, D.C., _J. Brit. astr. Ass._, 131(1), 33 (2012).
- Chaucer, G., _Treatise on the Astrolabe_, in _The Riverside Chaucer_, ed. L.D. Benson (Boston, 1987)
- Eisner, S., _J. Brit. astr. Ass._, *86*(1), 18-29 (1975)
- Eisner, S., _J. Brit. astr. Ass._, *86*(2), 125-132 (1976a)
- Eisner, S., _J. Brit. astr. Ass._, *86*(3), 219-227 (1976b)

#pagebreak()

#figure(
  image("{mother_back}"),
  caption: [The back of the mother of the astrolabe.],
) <mother_back>

#figure(
  image("{mother_front}"),
  caption: [The front of the mother of the astrolabe, with combined climate.
    Should a climate for a different latitude be required, you should download an alternative kit from the author's website.],
) <mother_front>

#figure(
  image("{rule}"),
  caption: [Left: The rule, which should be mounted on the front of the astrolabe.
    Right: The alidade, which should be mounted on the back of the astrolabe.],
) <rule>

#figure(
  image("{rete}"),
  caption: [The rete of the astrolabe, showing the stars of the night sky.
    This should be printed onto a piece of transparent plastic;
    most stationers should be able to provide acetate sheets for use on overhead projectors, which are ideal for this purpose.],
) <rete>
