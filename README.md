# EPUB to HTML Convertor + Style Injector

1. The conversion does:

   - extracting html library from .epub file ([inspired](https://github.com/casperlehmann/html-from-epub)).
   - injecting styles and logics

2. After the injection you get:

   - advanced collapsible toc ([inspired](#)).
   - dark/Light style button
   - you can open files via `localhost` or simply with `file manager`

## EPUB to HTML Convertor

### Install

```sh
git clone git@github.com:PaPa31/epub2html.git
```

### Usage

Run via python:

```sh
python /path/to/epub2html file.epub
```

or make bash alias...

#### Bash alias

Add to the end of `.bashrc`:

```sh
epub2html='python /path/to/epub2html'
```

... and, after restart your terminal, run:

```sh
epub2html file.epub
```

When converted, the location of the `injector files` (styles and javascript) is added to the `<head>` section of the extracted pages.

When you later open the page, this javascript will `inject` additional styles and additional javascript logic on the fly.

## Style Injector

You only need to clone the other repo correctly (to the right place):

```sh
git clone git@github.com:PaPa31/js-and-css.git
```

## Books root location

After conversion, html/xhtml files will look for `js` & `css` files in the root of the `Books` directory. Which is the default:

```sh
# Unix
file:///media/storage418Gb/Users/parsh/Documents/Books

# Windows
file:///F:/Users/parsh/Documents/Books
```

For now you must replace `my location` with `your location` of the `Books` folder.
