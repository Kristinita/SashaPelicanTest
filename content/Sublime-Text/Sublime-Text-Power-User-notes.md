Title: Sublime-Text-Power-User-notes
Date: 2017-02-13 19:15:15
Author: Sasha Chernykh
Lang: en
Summary:
Pagetitle: “Sublime Text Power User” notes
Metacontent: Notes of book “Sublime Text Power User”
Pagecolors: programs
Asideimage: SashaChocolate
Iconleftorright: right
Tags: sublime-text
Category: Sublime Notes
Tooltipster: false
ClipboardJs: true
Noco: 1EBY

[Sacagawea](Sacagawea)

<h2>Preamble</h2>
<br /> All comments on <a href="http://jmp.sh/xasKD18">this</a> (<a href="https://docs.zoho.com/file/nqgo4e3473558e032489e9dc3bceb3db16723">alternate link</a>) version of the book «Sublime Text Power User», bold numbers — numbers of pages your book. I admit that many of my notes are not your mistakes and typos, and I do not understand something, or affect my poor knowledge of the English language, but I beg to review my notes. Please ask me for clarification if you do not understand the phrase in my bad English. I use Windows 10 Education, Sublime Text 3 Build 3114 and all my notes belong to Windows.
<br />
<br /> Many thanks for your huge work on writing of the book! Sincerely, <a href="http://ru.stackoverflow.com/tags/sublime-text/topusers">leader in Sublime Text tag rating on Russian Stack Overflow</a>, Sasha Chernykh.
<br />
<br />
<br /><br /><b>13</b>
<br /> I think we can talk about the final transition from Sublime Text 2 to 3.
<br /><br /><b>14</b>
<br />
<blockquote>1. Open the console by hitting the key combination
	<kbd>Ctrl + \</kbd>
</blockquote>
Now by default
<kbd>Ctrl+`</kbd>.
<br /><br /><b>16</b>
<br />
<br />
<img src="https://i.imgur.com/62uCZBa.png" alt="Alt attribute fish"><br />
If to use Portable version, it isn't necessary to specify
<dfn>%APPDATA%</dfn>.
<br /><br /><b>45</b>
<br /> On <a href="https://johnblackbourn.com/sublimecodeintel-st3">https://johnblackbourn.com/sublimecodeintel-st3</a> page now <a href="https://github.com/spectacles/CodeComplice">reccomend</a> CodeComplice use, but for me CodeComplice is some bugs and undesirable behavior, <a href="https://github.com/spectacles/CodeComplice/issues/51">example</a>.
<br /><br /><b>50</b>
<br />
<dfn>-(std in)</dfn> only for OSX users, see <a href="http://docs.sublimetext.info/en/latest/command_line/command_line.html#invocations">unofficial documentation</a>, but in the book of it it isn't specified.
<br /><br /><b>52</b>
<br />
<blockquote>
	<dfn>-a</dfn> or
	<dfn>--add</dfn>: Add the current file or folder to the active/last used sublime text window</blockquote>
This command is only for folders, but not for files, see <a href="http://docs.sublimetext.info/en/latest/command_line/command_line.html#options">unofficial documentation</a>.
<dfn>subl -a ExampleFolder</dfn> add folder
<dfn>ExampleFolder</dfn> in current window,
<dfn>subl ExampleFolder</dfn> in new window. But
<dfn>subl -a test.txt</dfn> =
<dfn>subl test.txt</dfn>, both of these commands open a test.txt file in a new tab of the active window. The example below is also incorrect.
<br />
<br /><br /><b>68</b>
<br /> This method does not work for me. It is necessary, or hold down the middle mouse button or
<kbd>Ctrl+Alt+↓/↑</kbd> . See <a href="https://forum.sublimetext.com/t/solved-how-to-quick-select-in-every-line-between-first-and-last-for-me/21688">forum thread</a>.
<br />
<br /><br /><b>77</b>
<br />
<blockquote>go to
	<kbd>Tools</kbd> —►
	<kbd>New snippet ...</kbd>
</blockquote>
In the <kbd>Tools</kbd> menu there is no point <kbd>New snippet ...</kbd> .
<br />
<br />
<img src="https://i.imgur.com/K3YqJ4S.png" alt="Alt attribute fish">
<br /><br /><b>80</b>
<br />
<blockquote>If you are having trouble finding the scope, an easy way to find it is to open your packages folder
	<kbd>Preferences</kbd> →
		<kbd>Browse Packages...</kbd> and find the folder associated with your language. Inside of that folder will be a
		<dfn>.tmLanguage </dfn> file.</blockquote>

1. Now use <a href="https://www.sublimetext.com/docs/3/syntax.html">sublime-syntax</a> files.
1. Not all folders programming languages can be found on the path

<kbd>Preferences</kbd> →
<kbd>Browse Packages...</kbd> .
<br /><br /><b>84</b>
<br /> Now
<kbd>Ctrl+G</kbd> is <dfn>Goto Line...</dfn> .
<br /><br /><b>92</b>
<br /> Empty section «Moving Lines and Code Blocks»
<br />
<br />
<img src="https://i.imgur.com/x1tF1mG.png" alt="Alt attribute fish">
<br /><br /><b>94</b>
<br />
<blockquote>Using
	<kbd>Ctrl+K</kbd> without the shift key will delete from the caret to the end of the current line.</blockquote>
Using
<kbd>Ctrl+K, Ctrl+K</kbd>.
<br /><br /><b>94</b>
<br /> On Windows forward delete words-by-words is
<kbd>Ctrl+Delete</kbd>.
<br /><br /><b>95</b>
<br />
<blockquote>Just press space and keep typing!</blockquote>
If you only press the spacebar,
<dfn>p</dfn> tag was removed.
	<br /><br /><b>95</b>
	<br />
	<kbd>Ctrl+↑/↓</kbd> on Windows is jump to the beginning/end of word, not line.
	<br />
	<br />
	<img src="https://i.imgur.com/u3zjnlJ.png" alt="Alt attribute fish">
	<br /><br /><b>96</b>
	<br /> All hotkeys in this image is not work for me.
	<br />
	<br />
	<img src="https://i.imgur.com/li2YjO9.png" alt="Alt attribute fish">
	<br /><br /><b>103</b>
	<br />
	<blockquote>(Windows users use
		<kbd>Ctrl+Shift</kbd>)</blockquote>
	Windows users use
	<kbd>Ctrl+Shift+[</kbd>.
	<br /><br /><b>104</b>
	<br />
	<blockquote>The keyboard shortcut for this is a little different. We need to hold down (
		<kbd>Ctrl</kbd> on Windows/Linux) and then tap
			<kbd>K</kbd>.</blockquote>
	Not working on Windows.
	<br /><br /><b>108</b>
	<br />
	<br />
	<img src="https://i.imgur.com/nlEMn8q.png" alt="Alt attribute fish"><br /> I think that once you have a slash at the beginning. Not
	<dfn>"path": "/Volumes/Macintosh HD/wesbos/Dropbox/0185-book"</dfn>, correct is
	<dfn>"path": "Volumes/Macintosh HD/wesbos/Dropbox/0185-book"</dfn>. For example, I have
	<dfn>User</dfn> folder, when is situated my
	<dfn>sublime-project</dfn> file and folder
	<dfn>Dictionary</dfn>. If I want to specify the path to the folder
	<dfn>Dictionary</dfn>, I must point
	<dfn>"Dictionaries"</dfn> or
	<dfn>"./Dictionaries"</dfn> or
	<dfn>"../User/Dictionaries"</dfn>, But I do not understand how to specify the relative path with a slash at the beginning of.
	<br /><br /><b>128</b>
	<br /> Incorrect example, see <a href="https://forum.sublimetext.com/t/not-automatic-change-of-build-system/21745">forum thread</a>.
	<br /><br /><b>142</b>
	<br /> Sublimerge 3 — paid plugin, I believe that it is necessary to specify in the book.
	<br /><br /><b>143</b>
	<br />
	<br />
	<img src="https://i.imgur.com/1Vfnz56.png" alt="Alt attribute fish">
	<br /> Hotkeys not work for me.
	<br /><br /><b>154</b>
	<br /> Not
	<dfn>c#badda55.3</dfn>, correct is
	<dfn>c#badda5.3</dfn>. Emmet still indicate the right color, but in my opinion, do not result in the book of incorrect examples.
	<br /><br /><b>155</b>
	<br /> Now
	<kbd>Ctrl+Shift+G</kbd>, not
	<kbd>Ctrl+W</kbd> by default.
	<br /><br /><b>158</b>
	<br /> Now
	<kbd>Ctrl+'</kbd>, not
	<kbd>Ctrl+Shift+D</kbd> by default.
	<br /><br /><b>161</b>
	<br /> Now
	<kbd>Ctrl+Alt+J</kbd>, not
	<kbd>Ctrl+Shift+T</kbd> by default.
	<br /><br /><b>165</b>
	<br /> Now
	<kbd>View in SublimeServer</kbd>, not
	<kbd>View This File in the Browser</kbd>.
	<br /><br /><b>175</b>
	<br /> Transmit Dosksend <a href="https://packagecontrol.io/packages/Transmit%20Docksend">only for Sublime Text 2 and OSX</a>.
	<br /><br /><b>176</b>
	<br /> Bower need <a href="https://github.com/benschwarz/sublime-bower#installation">Git</a> for Windows users.
	<br /><br /><b>180</b>
	<br /> «mode at a lang<b>ua</b>ge»
	<br /><br /><b>180</b>
	<br />
	<blockquote>You can also turn on Vintage mode at a langauge level by adding
		<dfn>"ignored_packages": []</dfn> to your language specific settings file — more on this in the settings section.</blockquote>
	Where is settings section?
	<br /><br /><b>183</b>
	<br /> Package CSS3 Syntax has been replaced by <a href="https://github.com/y0ssar1an/CSS3_Syntax#announcement-for-st3-users-this-package-has-been-replaced-by-css3-this-package-will-be-removed-some-time-after-sublime-text-3-is-released">CSS3</a>.
	<br /><br /><b>189</b>
	<br /> Pretty JSON <a href="https://github.com/dzhibas/SublimePrettyJson/issues/70">does not work</a> with files that contain comments. This is a serious drawback, in my opinion it is necessary to mention in the book.
	<br /><br /><b>197</b>
	<br /> By default in TOC will be
	<dfn>[about]</dfn> and
	<dfn>[growing-up]</dfn>, not
	<dfn>(#about)</dfn> and
	<dfn>(#growing-up)</dfn>, see gif:
	<br />
	<br />
	<img src="https://packagecontrol.io/readmes/img/b64bfa89d42bf72a062e070872a03f6832d62ae5.gif" alt="Alt attribute fish"><br /> To make as at you on the picture, it is necessary to add in the file
	<kbd>MarkdownTOC</kbd> →
	<kbd>Settings - User</kbd> line <dfn>{ "default_bracket": "round", }</dfn>.
	<br /><br /><b>198</b>
	<br /> SublimeTODO plugin wasn't updated long ago, TODO Review is <a href="https://github.com/robcowie/SublimeTODO">recommended</a> to use.
	<br /><br /><b>200</b>
	<br />
	<blockquote>If the language supports block commenting, add in
		<kbd>option/alt</kbd> into the mix to block comment multiple lines of selected code.</blockquote>
	Multi-line comments are added to the Windows hotkey
	<kbd>Ctrl+Shift+/</kbd>, <kbd>Alt</kbd> is not used.
	<br /><br /><b>201</b>
	<br /> You have not written, how to call Fullscreen Mode, in my opinion, you need to specify the hot keys —
	<kbd>Shift+F11</kbd>.
