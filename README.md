# Bluedrop Pelican Theme
Bluedrop is a responsive theme which adjusts itself to different screen and
window sizes, built on [Zurb Foundation](http://foundation.zurb.com/).
It is designed to look modern, but at the same time traditional,
using a serif font and darker colours. It features full
[Disqus](https://disqus.com/) integration and can be customized through
variables in your Pelican configuration file. See it live at
[my blog](http://ashwinvis.github.io/).

## Installation

```sh
pip install "pelican>=4.0.1"
pelican-themes -i theme/pelican-themes/backdrop
```

## Screenshots

<img src="https://raw.githubusercontent.com/ashwinvis/pelican-bluedrop/master/examples/demo/images/demo-desktop.png" width="70%">

This is an example of the same on a tablet.

<div>
<img src="https://raw.githubusercontent.com/ashwinvis/pelican-bluedrop/master/examples/demo/images/demo-tablet-top.png" width="35%"/>
<img src="https://raw.githubusercontent.com/ashwinvis/pelican-bluedrop/master/examples/demo/images/demo-tablet-bot.png" width="35%"/>
</div>

This is an example of the same on a mobile.
<div>
<img src="https://raw.githubusercontent.com/ashwinvis/pelican-bluedrop/master/examples/demo/images/demo-mobile-top.png" width="35%"/>
<img src="https://raw.githubusercontent.com/ashwinvis/pelican-bluedrop/master/examples/demo/images/demo-mobile-bot.png" width="35%"/>
</div>

I you want to customize Bluedrop, perhaps consider using
[Sass](http://sass-lang.com/) and [Grunt](http://gruntjs.com/), as I did when
originally designing it. See the
[backdrop-theme](https://github.com/ashwinvis/backdrop-theme) repository for
the source files.

## Compatible Plugins
The theme has been designed to use the [representative_image](https://github.com/getpelican/pelican-plugins/tree/master/representative_image) plugin. However,
websites will look fine without it. The
[tipue_search](https://github.com/getpelican/pelican-plugins/tree/master/tipue_search) plugin (which allows the website to be searched) should be used. In order
for this to work, `'search.html'` must be added to the `DIRECT_TEMPLATES`
variable. Bluedrop is also known to work with the
[render_math](https://github.com/getpelican/pelican-plugins/tree/master/render_math)
and [sitemap](https://github.com/getpelican/pelican-plugins/tree/master/sitemap)
plugins, but these work with all themes and Bluedrop is in no way special in
this regard.

## Theme Variables
Have a look at the `examples` directory to see which theme variables can be set
in your `pelicanconf.py` file in order to customize your website.


## Credits
Thanks to [Chris MacMackin](https://cmacmackin.github.io/) for the original
[backdrop-theme](https://github.com/cmacmackin/backdrop-theme).
