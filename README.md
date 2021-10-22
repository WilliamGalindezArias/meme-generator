# meme-generator



# Project: Meme Generator

## Overview

The goal of this project is to build a "meme generator" – application to dynamically generate memes, 



## Instructions

We've provided some code and data to get you started. So the first step is to download the starter code and get generally familiar with what it includes.

-   Download the starter code.
-   Locate the smaple quotes and images of Xander the pup in src/\_data/.
-   There's a basic flask server that will consume your modules and make them usable through a web interface. Check out the main code for this flaks service in app.py.
-   Check out the HTML template files in templates/.
- install pdftext utility for your OS

### Quote Engine

The **Quote Engine** module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

```
"This is a quote body" - Author
```

This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other
fundamental programming principles.

#### Quote Format

Example quotes are provided in a variety of files. Take a moment to review the file formats in ./\_data/SimpleLines and ./\_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

#### Ingestors

An abstract base class, IngestorInterface should define two methods with the following class method signatures:

```
def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
```

Separate strategy objects should realize **IngestorInterface** for each file type (csv, docx, pdf, txt).

    TIP: pdftotext may not be installed on your local machine (Mac or Windows). If this is the case, you can
    install using the open source XpdfReader utility.

A final **Ingestor** class should realize the **IngestorInterface** abstract base class and encapsulate your helper
classes. It should implement logic to select the appropriate helper for a given file based on filetype.

    NOTE: Do not use the pdftotext PIP Library - we'd like you to demonstrate your understanding of the
    subprocess module.

The responsibility of this module is to load and parse quotes from files. Here's what you'll need to do to complete it:

-   Create a Python module(including **init**.py) in a directory called QuoteEngine.
-   Example quotes are provided in a varity of files. Take a moment to review the file
    formats in ./data/SimpleLines and ./data/DogQuotes.
-   Implement a simple QuoteModel class to encapsulate the body and author.
-   Implement an abstract base class, IngestorInterface. This class should define two
    methods with the following class method signatures: def can_ingest(cls, path) -> boolean
    and def parse(cls, path: str) -> List[QuoteModel].
-   Implement separate strategy objects that realize the IngestorInterface for each file
    type(csv, docx, pdf, txt).
-   Implement a final Ingestor class that realizes the IngestorInterface abstract class
    and encapsulates your helper classes. It should implement logic to select the appropiate
    helper for a given file, based on filetype.
-   If you file, you can check your work against the Quote Engine Module section of the **rubric**.
-   All Quote classes have clear, concise, and PEP compliant dosctrings.
-   All code is PEP-8 Compliant.
-   Common exceptions should be handled using **try-catch** blocks.

### Meme Engine Module

The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.

The class must implement code for:

-   Loading an image using Pillow (PIL)
-   Resizing the image so the width is at most 500px and the height is scaled proportionally.
-   Adding a quote body and a quote author to the image.
-   Save the manipulated image.
-   The class must implement this instance method signature, which returns the path to the manipulated image:

```
make_meme(self, img_path, text, author, width = 500) -> str
```

-   You can check your work against the **Meme Generator Module** section of the **rubric**.
-   All Meme Generator classes have clear, concise, and PEP compliant dosctrings.
-   All code is PEP-8 Compliant.
-   Common excpetions should be handled using **try-catch** blocks.

### Package your Application

Larger, complex systems need an interface for users to interact with. We'll package the project as a command line
tool and as a simple web service.

#### Create a Command-Line Interface tool

The project contains a simple cli app starter code in meme.py. This file contains @TODO tasks for you to complete.
The utility can be which can be run from the terminal by invoking python3 meme.py.

The script must take three optional CLI arguments:

-   --body a string quote body
-   --author a string quote author
-   --path an image path

The script returns a path to a generated image. If any argument is not defined, a random selection is used.



#### Ingestors sub-module

The submodule Ingestors parse any file (csv, txt, docx, pdf).

-   In the Ingestors interface file exists a class which represents an object and validates if exist the file.
-   The csv ingestor file reads the csv file and returns a parse.
-   The docx ingestor file reads the docx file and returns a parse.
-   The pdf ingestor file reads the pdf file and returns a parse.
-   The text ingestor file reads the text file and returns a parse.

The dependencies this sub-module uses are:

-   Pandas (read the csv file).
-   Docx (read the docx file).

#### Meme sub-module

The submodule Meme creates and generates the meme according to the
path, text, author, width passed.

-   The meme engine file returns the outfile, which the meme image is created and saved .
-   The meme generator file returns the path where the meme is generated with the Meme Engine class.

The dependencie this sub-module uses is:

-   PIL (adds image processing capabilities).

#### Models

The submodule models creates the class for the Quote and constructs the necessary attributes.

-   The quote model file creates the class Quote model and constructs it, returns a string version and a printable representation of the object.

This sub-module doesn't use dependencies.

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!).  Thank you to [makeareadme.com](https://gitlab.com/-/experiment/new_project_readme_content:a534b6e7d598e57ec312b79845a9033e?https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.





## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
MIT

## Project status
Passing tests

