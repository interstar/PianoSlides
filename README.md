# PianoSlides

HTML Slide Template with integrated MIDI Piano - VIBECODED

I gave a presentation on music theory and my [GoldenPond](https://github.com/interstar/golden-pond) library recently.

And I needed both some slides, and also one of those on-screen piano keyboards that lights up when you play an external MIDI keyboard.

It occurred to me that it would be really convenient to have the two combined. Ie. a MIDI responsive keyboard that lights up, IN the slides themselves.

So I got onto ChatGTP and vibe-coded this Reveal.js template with inbuilt MIDI responsive Piano keyboard.


### Quick Start

You write your slides in Markdown, separated by four-hyphens (----), in the slides.md file in the same directory as the template.html

These slides should be pretty much the reveal.js standard.

Then run

    python generate.py
    
    
This will create a new index.html with your slide-show.

### Hints

I've found that it's best to run the slide-show from a local webserver (eg. python -m http.server) 

You can keep images, mp3 files and other assets in the directory called assets/

There's a special notation for embedding audio files in slides (pretty important for music related slide-shows) 

    [audio:filename.mp3]
    
When initially connecting the keyboard I found there was a bit of faff getting the browser to receive data from it. That's why there are a couple of buttons like Start Audio and Test Audio and I've had to select the right MIDI input device a couple of times in the MIDI in drop down. But eventually I get it working and it does behave correctly. The keys light up and it plays sound in response to incoming MIDI data.

DON'T EXPECT THIS TO SOUND GOOD

The synthesized voices are awful.

It's also not very accurately responsive. Ie. if you play too many notes too fast it will lose track, it won't light up all the notes you want, and it may leave some notes you don't want lit up. It needs some improvement in this area.

But if you just want to demonstrate which are the notes of particular chords, and you play them in, slowly and deliberately, it does the job.

Sadly it won't work in Firefox. But that's Mozilla's fault for not supporting webmidi. I was using it in Chrome in Windows where it's OK.

### Vibe Coding Disclosure

I'm an experienced programmer. I also use AI assisted "vibe-coding". In some projects I mainly write code by hand. In others I have a mixture of handwritten code with some AI contributions. In some, like this template, I have barely glanced at the code. That's because this is a low-stakes, small, self-contained project. I find vibe-coding mostly useful for projects like this. Small, self-contained, low-stakes, very useful in a specific context. And I'm happy to use it for that. But I do not recommend vibe-coding as the solution to all your problems. Nor have I gone over this code in fine detail to check for major security implications etc. 

Here's the initial prompt and dialogue with ChatGPT : [https://chatgpt.com/share/68d66084-c0cc-8010-bf20-ac8a1b95ce21](https://chatgpt.com/share/68d66084-c0cc-8010-bf20-ac8a1b95ce21)

I've also included this dialogue as a pdf in this repo called pianoslide-chatgpt.pdf

If you are interested in the "prompt", then you can see it. But note the value is less in the initial prompt than the back and forward dialogue with the AI. Also note that this ChatGPT conversation does not lead to the final code. I then downloaded the code to my local machine and worked on it to tweak and fix bugs, using Cursor (ie Claude).

The final, more or less working, code is the result of starting in ChatGPT and then refining in Cursor. In my experience, the best results of "vibe-coding" are a fairly intense dialogue between human and often multiple AIs.

